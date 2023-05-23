import time
from pathlib import Path
import cv2 as cv
import depthai as dai
import os

# 1. Run DepthAI UVC Mode (under Misc)
# 2. Run Program
# Note: Sometimes, you get "RuntimeError: Failed to connect to device, error message: X_LINK_DEVICE_NOT_FOUND" under the code
#       "dai.Device(pipeline) as device: ". To resolve this error, check ethernet connection (i.e. try plug/unplug it!).

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

# Create pipeline
pipeline = dai.Pipeline()

camRgb = pipeline.create(dai.node.ColorCamera)
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_4_K)

xoutRgb = pipeline.create(dai.node.XLinkOut)
xoutRgb.setStreamName("rgb")
camRgb.video.link(xoutRgb.input)


xin = pipeline.create(dai.node.XLinkIn)
xin.setStreamName("control")
xin.out.link(camRgb.inputControl)

# Properties
videoEnc = pipeline.create(dai.node.VideoEncoder)
videoEnc.setDefaultProfilePreset(1, dai.VideoEncoderProperties.Profile.MJPEG)
camRgb.still.link(videoEnc.input)

# Linking
xoutStill = pipeline.create(dai.node.XLinkOut)
xoutStill.setStreamName("still")
videoEnc.bitstream.link(xoutStill.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=30, blocking=False)
    qStill = device.getOutputQueue(name="still", maxSize=30, blocking=True)
    qControl = device.getInputQueue(name="control")

    # Make sure the destination path is present before starting to store the examples
    dirName = "rgb_data"
    Path(dirName).mkdir(parents=True, exist_ok=True)

    currentFrames = 0
    while True:
        inRgb = qRgb.tryGet()  # Non-blocking call, will return a new data that has arrived or None otherwise
        if inRgb is not None:
            frame = inRgb.getCvFrame()
            # 4k / 4
            # frame = cv.pyrDown(frame)
            # frame = cv.pyrDown(frame)
            cv.imshow("rgb", frame)

            # FIXME: manipulate files here or somewhere else
            name = './data/frame' + str(currentFrames) + '.jpg'
            print ('Creating...' + name)
  
            # writing the extracted images
            cv.imwrite(name, frame)
            currentFrames += 1

        if qStill.has():
            fName = f"{dirName}/{int(time.time() * 1000)}.jpeg"
            with open(fName, "wb") as f:
                f.write(qStill.get().getData())
                print('Image saved to', fName)
        
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            ctrl = dai.CameraControl()
            ctrl.setCaptureStill(True)
            qControl.send(ctrl)
            print("Sent 'still' event to the camera!")