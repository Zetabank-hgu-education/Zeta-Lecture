import argparse
import sys

from jetson_inference import poseNet
from jetson_utils import videoSource, videoOutput, cudaFont

# parse the command line
# For our mission, We recieve the network name, and Camera name. 
# Set up argument parser, so that command line parameters can be read within the program
parser = argparse.ArgumentParser(description="Run pose estimation DNN on a camera stream.",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 epilog=poseNet.Usage() + videoSource.Usage() + videoOutput.Usage())


# Major Functionality parameters (required from the user)
parser.add_argument("input_CAMERA", type=str, default="", nargs='?', help="use csi://0 for Raspberry pi Camera")
parser.add_argument("--network", type=str, default="", help="pre-trained model to load")

# Minor Functionality parameters (optional)
parser.add_argument("--overlay", type=str, default="links,keypoints", help="pose overlay flags (e.g. --overlay=links,keypoints)\nvalid combinations are:  'links', 'keypoints', 'boxes', 'none'")
parser.add_argument("--threshold", type=float, default=0.15, help="minimum detection threshold to use") 

# If no parameter is given from the user, shut the program down
try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the pose estimation model
net = poseNet(opt.network, sys.argv, opt.threshold)

# create video sources & outputs
input = videoSource(opt.input_CAMERA, argv=sys.argv)
output = videoOutput("DISPLAY://0", argv=sys.argv)

# Initialize the overlay font
font = cudaFont()

# process frames until EOS or the user exits
while True:
    # capture the next image
    img = input.Capture()
    
    if img is None: # timeout
        continue
    
    # perform pose estimation (with overlay)
    poses = net.Process(img, overlay=opt.overlay)
  
    total_keypoints = 0
    for pose in poses:
        total_keypoints += len(pose.Keypoints)

    #overlay the number of detected objects with total number of keypoints on the frame
    font.OverlayText(img, img.width, img.height, "detected {:d} objects, with {:d} keypoints".format(len(poses), total_keypoints), 5, 5, font.White, font.Gray40)
    
    # render the image
    output.Render(img)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))
    
    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break
    