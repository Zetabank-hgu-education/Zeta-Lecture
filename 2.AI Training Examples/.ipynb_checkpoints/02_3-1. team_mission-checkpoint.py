from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont


net = imageNet("CHANGEME")
camera = videoSource("CHANGEME") # Raspberry Pi Camera
display = videoOutput("CHANGEME") # Jetson Nano Display

font = cudaFont()


# process frames until the user exits
while display.IsStreaming():
    
    # Capture each of the frames of camera
    img = camera.Capture()

    # Classify the image
    class_id, confidence = net.Classify(img)

    # find the object description
    class_desc = net.GetClassDesc(class_id)

    #overlay the result on the frame
    font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), 5, 5, font.White, font.Gray40)

    # render the image
    display.Render(img)

    # update the title bar
    display.SetStatus("Image Recognition | Network {:.0f} FPS".format(net.GetNetworkFPS()))
