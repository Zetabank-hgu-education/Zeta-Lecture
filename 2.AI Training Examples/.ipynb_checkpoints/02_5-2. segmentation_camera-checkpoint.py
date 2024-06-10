import argparse
import sys

from jetson_inference import segNet
from jetson_utils import videoSource, videoOutput, cudaOverlay, cudaDeviceSynchronize

from segnet_utils import *

# parse the command line
# For our mission, We recieve the network name, and Camera name. 
# Set up argument parser, so that command line parameters can be read within the program
parser = argparse.ArgumentParser(description="Segment a live camera stream using an semantic segmentation DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 epilog=segNet.Usage() + videoSource.Usage() + videoOutput.Usage())

# Major Functionality parameters (required from the user)
parser.add_argument("input_CAMERA", type=str, default="", nargs='?', help="use csi://0 for Raspberry pi Camera")
parser.add_argument("--network", type=str, default="", help="pre-trained model to load")

# Minor Functionality parameters (optional)
parser.add_argument("--filter-mode", type=str, default="linear", choices=["point", "linear"], help="filtering mode used during visualization, options are:\n  'point' or 'linear' (default: 'linear')")
parser.add_argument("--visualize", type=str, default="overlay,mask", help="Visualization options (can be 'overlay' 'mask' 'overlay,mask'")
parser.add_argument("--ignore-class", type=str, default="void", help="optional name of class to ignore in the visualization results (default: 'void')")
parser.add_argument("--alpha", type=float, default=150.0, help="alpha blending value to use during overlay, between 0.0 and 255.0 (default: 150.0)")
parser.add_argument("--stats", action="store_true", help="compute statistics about segmentation mask class output")


# If no parameter is given from the user, shut the program down
try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the segmentation network
net = segNet(opt.network, sys.argv)

# set the alpha blending value
net.SetOverlayAlpha(opt.alpha)

# create video sources & outputs
input = videoSource(opt.input_CAMERA, argv=sys.argv)
output = videoOutput("DISPLAY://0", argv=sys.argv)
# create buffer manager
buffers = segmentationBuffers(net, opt)

    
# process frames until the user exits
while output.IsStreaming():
    # capture the next image
    img = input.Capture()

    # allocate buffers for this size image
    buffers.Alloc(img.shape, img.format)

    # process the segmentation network
    net.Process(img, ignore_class=opt.ignore_class)

    # generate the overlay
    if buffers.overlay:
        net.Overlay(buffers.overlay, filter_mode=opt.filter_mode)

    # generate the mask
    if buffers.mask:
        net.Mask(buffers.mask, filter_mode=opt.filter_mode)

    # composite the images
    if buffers.composite:
        cudaOverlay(buffers.overlay, buffers.composite, 0, 0)
        cudaOverlay(buffers.mask, buffers.composite, buffers.overlay.width, 0)

    # render the output image
    output.Render(buffers.output)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))
