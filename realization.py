import face_recognition
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
%matplotlib inline
def window(capture_width=3280, capture_height=2464, display_width=820, display_height=616, framerate=21, flip_method=0,):
  return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
         % (capture_width, capture_height, framerate, flip_method, display_width, display_height)
        )

def face_detect():
  video_capture = cv2.VideoCapture(window(), cv2.CAP_GSTREAMER)
  tata_image = face_recognition.load_image_file("tata.jpeg")
  tata_face_encoding = face_recognition.face_encodings(tata_image)[0]
  known_face_encodings = [
      tata_face_encoding
  ]
  known_face_names = [
      "Tatyana"
  ]
  face_locations = []
  face_encodings = []
  face_names = []
  if video_capture.isOpened():
    ret, frame = video_capture.read() 
    if not ret:
      break
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_small_frame = small_frame[:, :, ::-1]   
    image = rgb_small_frame
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    for face_location in face_locations:
      top, right, bottom, left = face_location
      face_image = image[top:bottom, left:right]
      pil_image = Image.fromarray(face_image)
      for face_encoding in face_encodings:
        results = face_recognition.api.compare_faces(known_face_encodings, face_encoding, 0.55)
        if True in results:
          first_match_index = results.index(True)
        if results[0]:
          print(known_face_names[first_match_index])
        else:
          print('Unknown',top)
          if face_names == []:
            print('Attention, stranger in the building')
          face_names.append(top)
          face_names = list(set(face_names))
          pil_image.save(f'{top}.jpg')
      for (top, right, bottom, left) in face_locations:
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
  video_capture.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detect()