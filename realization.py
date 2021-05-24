import face_recognition
import cv2
import numpy as np
from PIL import Image


def face_detect():
  video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
  video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
  video_capture.set(cv2.CAP_PROP_FPS, 30)
  
  tata_image = face_recognition.load_image_file("tata.jpg")
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
      for (top, right, bottom, left) in face_locations:
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
      cv2.imshow('Video', frame)
  video_capture.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detect()
