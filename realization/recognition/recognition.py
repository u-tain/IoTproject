import face_recognition
import cv2
import numpy as np
from PIL import Image
import io 
import requests
import base64
import os


def face_detect():
  url = 'http://6fda4688bc81.ngrok.io'
  
  video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
  video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
  video_capture.set(cv2.CAP_PROP_FPS, 30)
  
  tata_image = face_recognition.load_image_file("tata.jpg")
  tata_face_encoding = face_recognition.face_encodings(tata_image)[0]
  vlada_image = face_recognition.load_image_file("vlada.jpg")
  vlada_face_encoding = face_recognition.face_encodings(vlada_image)[0]
  
  known_face_encodings = [
      tata_face_encoding,
      vlada_face_encoding
  ]
  known_face_names = [
      "Tatyana",
      "Vladislava"
  ]
  face_locations = []
  face_encodings = []
  face_names = []
  While video_capture.isOpened():
    ret, frame = video_capture.read() 
    if not ret:
      break
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
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
          data={}
          with open(f'/home/iot/IoTproject/{top}.jpg', mode='rb') as file:
               img = file.read()
          data['img'] =  base64.b64encode(img)
          rs = requests.post(url, files=data)  
          path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{top}.jpg')
          os.remove(path)   
  video_capture.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detect()
