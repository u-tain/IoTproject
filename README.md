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
v4l2-ctl --all
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
## Camera formats:
```
 v4l2-ctl —device=/dev/video0 —list-formats-ext
ioctl: VIDIOC_ENUM_FMT
Index : 0
Type : Video Capture
Pixel Format: 'YUYV'
Name : YUYV 4:2:2
Size: Discrete 640x480
Interval: Discrete 0.033s (30.000 fps)
Interval: Discrete 0.067s (15.000 fps)
Interval: Discrete 0.100s (10.000 fps)
Interval: Discrete 0.200s (5.000 fps)
Size: Discrete 160x120
Interval: Discrete 0.033s (30.000 fps)
Interval: Discrete 0.067s (15.000 fps)
Interval: Discrete 0.100s (10.000 fps)
Interval: Discrete 0.200s (5.000 fps)
Size: Discrete 176x144
Interval: Discrete 0.033s (30.000 fps)
Interval: Discrete 0.067s (15.000 fps)
Interval: Discrete 0.100s (10.000 fps)
Interval: Discrete 0.200s (5.000 fps)
Size: Discrete 320x240
Interval: Discrete 0.033s (30.000 fps)
Interval: Discrete 0.067s (15.000 fps)
Interval: Discrete 0.100s (10.000 fps)
Interval: Discrete 0.200s (5.000 fps)
Size: Discrete 352x288
Interval: Discrete 0.033s (30.000 fps)
Interval: Discrete 0.067s (15.000 fps)
Interval: Discrete 0.100s (10.000 fps)
Interval: Discrete 0.200s (5.000 fps)
```
## Cv2 info:
```
General configuration for OpenCV 4.1.1 =====================================
  Version control:               4.1.1-2-gd5a58aa75

  Platform:
    Timestamp:                   2019-12-13T17:25:11Z
    Host:                        Linux 4.9.140-tegra aarch64
    CMake:                       3.10.2
    CMake generator:             Unix Makefiles
    CMake build tool:            /usr/bin/make
    Configuration:               Release

  CPU/HW features:
    Baseline:                    NEON FP16
      required:                  NEON
      disabled:                  VFPV3

  C/C++:
    Built as dynamic libs?:      YES
    C++ Compiler:                /usr/bin/c++  (ver 7.4.0)
    C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
    C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
    C Compiler:                  /usr/bin/cc
    C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
    C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
    Linker flags (Release):      -Wl,--gc-sections  
    Linker flags (Debug):        -Wl,--gc-sections  
    ccache:                      NO
    Precompiled headers:         NO
    Extra dependencies:          dl m pthread rt
    3rdparty dependencies:

  OpenCV modules:
    To be built:                 calib3d core dnn features2d flann gapi highgui imgcodecs imgproc ml objdetect photo python2 python3 stitching ts video videoio
    Disabled:                    world
    Disabled by dependency:      -
    Unavailable:                 java js
    Applications:                tests perf_tests examples apps
    Documentation:               NO
    Non-free algorithms:         NO

  GUI: 
    GTK+:                        YES (ver 2.24.32)
      GThread :                  YES (ver 2.56.4)
      GtkGlExt:                  NO

  Media I/O: 
    ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.11)
    JPEG:                        /usr/lib/aarch64-linux-gnu/libjpeg.so (ver 80)
    WEBP:                        build (ver encoder: 0x020e)
    PNG:                         /usr/lib/aarch64-linux-gnu/libpng.so (ver 1.6.34)
    TIFF:                        /usr/lib/aarch64-linux-gnu/libtiff.so (ver 42 / 4.0.9)
    JPEG 2000:                   build (ver 1.900.1)
    HDR:                         YES
    SUNRASTER:                   YES
    PXM:                         YES
    PFM:                         YES

  Video I/O:
    FFMPEG:                      YES
      avcodec:                   YES (57.107.100)
      avformat:                  YES (57.83.100)
      avutil:                    YES (55.78.100)
      swscale:                   YES (4.8.100)
      avresample:                NO
    GStreamer:                   YES (1.14.5)
    v4l/v4l2:                    YES (linux/videodev2.h)

  Parallel framework:            TBB (ver 2017.0 interface 9107)

  Trace:                         YES (with Intel ITT)

  Other third-party libraries:
    Lapack:                      NO
    Eigen:                       YES (ver 3.3.4)
    Custom HAL:                  YES (carotene (ver 0.0.1))
    Protobuf:                    build (3.5.1)

  Python 2:
    Interpreter:                 /usr/bin/python2.7 (ver 2.7.15)
    Libraries:                   /usr/lib/aarch64-linux-gnu/libpython2.7.so (ver 2.7.15+)
    numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.13.3)
    install path:                lib/python2.7/dist-packages/cv2/python-2.7

  Python 3:
    Interpreter:                 /usr/bin/python3 (ver 3.6.9)
    Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.6m.so (ver 3.6.9)
    numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.13.3)
    install path:                lib/python3.6/dist-packages/cv2/python-3.6

  Python (for build):            /usr/bin/python2.7

  Java:                          
    ant:                         NO
    JNI:                         NO
    Java wrappers:               NO
    Java tests:                  NO

  Install to:                    /usr
```
