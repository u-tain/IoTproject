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
   sudo apt install python3-numpy
   sudo apt install libcanberra-gtk-module
   sudo apt install python3-opencv
   sudo apt-get -y install python3-pip
   pip3 -v install Cython face_recognition
   pip3 install face_recognition
   ```
4. Upload file
   ```
   python3 realization.py
5. To the exit press: ```ctrl+C``` or q
## If you want to test your camera:
```
gst-launch-1.0 nvarguscamerasrc sensor_id=0 ! \
   'video/x-raw(memory:NVMM),width=3280, height=2464, framerate=21/1, format=NV12' ! \
   nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=720' ! \
   nvvidconv ! nvegltransform ! nveglglessink -e
```
