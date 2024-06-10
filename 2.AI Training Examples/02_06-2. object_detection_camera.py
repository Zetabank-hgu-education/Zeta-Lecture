import sys
import argparse

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

# parse the command line
# For our mission, We recieve the network name, and Camera name. 
# Set up argument parser, so that command line parameters can be read within the program
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=detectNet.Usage() + videoSource.Usage() + videoOutput.Usage())
# Major Functionality parameters (required from the user)
parser.add_argument("input_CAMERA", type=str, default="", nargs='?', help="use csi://0 for Raspberry pi Camera")
parser.add_argument("--network", type=str, default="", help="pre-trained model to load")

# Minor Functionality parameters (optional)
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 


# If no parameter is given from the user, shut the program down
try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# create video sources and outputs
input = videoSource(opt.input_CAMERA, argv=sys.argv)
output = videoOutput("DISPLAY://0", argv=sys.argv)
	
# load the object detection network
net = detectNet(opt.network, sys.argv, opt.threshold)

# note: to hard-code the paths to load a model, the following API can be used:
#
# net = detectNet(model="model/ssd-mobilenet.onnx", labels="model/labels.txt", 
#                 input_blob="input_0", output_cvg="scores", output_bbox="boxes", 
#                 threshold=args.threshold)

# process frames until EOS or the user exits
while True:
    # capture the next image
    img = input.Capture()
    
    if img is None: # timeout
        continue
    
    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=opt.overlay)
    
    # render the image
    output.Render(img)
    
    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))
    
    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break



