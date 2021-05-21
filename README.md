# IoTproject
Here we solve the problem of creating a face recognition system and sending notifications to the user.
## Steps to implement face recognition using Jetson Nano:
1. Clone github
   ```
   git clone https://github.com/u-tain/IoTproject.git
   ```
2. Open repository 
   ```
   cd IoTproject
   ```
3. Upload libs
   ```
   sudo apt-get update
   sudo apt install python3-numpy
   sudo apt install libcanberra-gtk-module
   sudo apt install python3-opencv
   sudo apt-get -y install python3-pip
   pip3 -v install Cython face_recognition
   pip3 install face_recognition
   python3 -m pip install --upgrade pip
   python3 -m pip install --upgrade Pillow
   ```
4. Upload file
   ```
   python3 realization.py
5. To the exit press: ```ctrl+C``` or q
## If you want to test your CSI-camera:
```
gst-launch-1.0 nvarguscamerasrc sensor_id=0 ! \
   'video/x-raw(memory:NVMM),width=3280, height=2464, framerate=21/1, format=NV12' ! \
   nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=720' ! \
   nvvidconv ! nvegltransform ! nveglglessink -e
```
## If you want to test your USB-camera:
```
nvgstcapture-1.0 --camsrc=0 --cap-dev-node=/dev/video1 node
$ video-viewer --input-width=640--input-height=480--input-codec=YUYV /dev/video0

```
## our usb camera info:
```
Driver Info (not using libv4l2):
	Driver name   : uvcvideo
	Card type     : USB2.0 PC CAMERA
	Bus info      : usb-70090000.xusb-2.4
	Driver version: 4.9.201
	Capabilities  : 0x84200001
		Video Capture
		Streaming
		Extended Pix Format
		Device Capabilities
	Device Caps   : 0x04200001
		Video Capture
		Streaming
		Extended Pix Format
Priority: 2
Video input : 0 (Camera 1: ok)
Format Video Capture:
	Width/Height      : 640/480
	Pixel Format      : 'YUYV'
	Field             : None
	Bytes per Line    : 1280
	Size Image        : 614400
	Colorspace        : Default
	Transfer Function : Default (maps to Rec. 709)
	YCbCr/HSV Encoding: Default (maps to ITU-R 601)
	Quantization      : Default (maps to Limited Range)
	Flags             : 
Crop Capability Video Capture:
	Bounds      : Left 0, Top 0, Width 640, Height 480
	Default     : Left 0, Top 0, Width 640, Height 480
	Pixel Aspect: 1/1
Selection: crop_default, Left 0, Top 0, Width 640, Height 480
Selection: crop_bounds, Left 0, Top 0, Width 640, Height 480
Streaming Parameters Video Capture:
	Capabilities     : timeperframe
	Frames per second: 30.000 (30/1)
	Read buffers     : 0
                     brightness 0x00980900 (int)    : min=0 max=255 step=1 default=110 value=110
                       contrast 0x00980901 (int)    : min=0 max=255 step=1 default=150 value=150
                     saturation 0x00980902 (int)    : min=0 max=255 step=1 default=60 value=60
                            hue 0x00980903 (int)    : min=-127 max=127 step=1 default=0 value=0
                          gamma 0x00980910 (int)    : min=1 max=8 step=1 default=4 value=4
                           gain 0x00980913 (int)    : min=0 max=65535 step=1 default=16 value=16
           power_line_frequency 0x00980918 (menu)   : min=0 max=2 default=1 value=1
                      sharpness 0x0098091b (int)    : min=0 max=255 step=1 default=1 value=1
```
