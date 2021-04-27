# IotTproject
Here we solve the problem of creating a face recognition system and sending notifications to the user.
## Steps to implement face recognition using Jetson Nano:
1. Clone github
   ```
   git clone https://github.com/u-tain/IotTproject.git
   ```
2. Open repository 
   ```
   cd IotTproject
   ```
3. Upload libs
   ```
   sudo apt install python3-numpy
   sudo apt install libcanberra-gtk-module
   sudo pip3 -v install Cython face_recognition
   ```
4. Upload file
   ```
   python3 realization.py
   ```
## if you want to test your camera:
```
gst-launch-1.0 nvarguscamerasrc sensor_id=0 ! \
   'video/x-raw(memory:NVMM),width=3280, height=2464, framerate=21/1, format=NV12' ! \
   nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=720' ! \
   nvvidconv ! nvegltransform ! nveglglessink -e
```
