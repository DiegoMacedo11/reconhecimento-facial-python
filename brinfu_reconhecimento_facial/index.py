import face_recognition

eu_image = face_recognition.load_image_file("eu.jpg")
eu_image2 = face_recognition.load_image_file("eu2.jpg")

eu_encoding = face_recognition.face_encodings(eu_image)[0]
eu2_encoding = face_recognition.face_encodings(eu_image2)[0]

result = face_recognition.compare_faces([eu_encoding], eu2_encoding)

if result[0]:
    print("As imagens são da mesma pessoa!!")
else:
    print("As imagens são pessoas diferentes!!")
