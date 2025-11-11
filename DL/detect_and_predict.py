import cv2
import os
import tensorflow as tf
import tensorflow.keras 
import matplotlib.pyplot as plt

model = tensorflow.keras.models.load_model("DL/emotion_cnn_model.keras")
classes_names = ('angry', 'disguasted', 'fearful', 'happy', 'neutral', 'sad', 'surprised')
facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread("C:/Users/hp/Desktop/D-tection-d-motions-Faciales/new.JPG")
gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)

faces = facecascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
if facecascade.empty()==True:
    print("le fishier n'est pa charge:", facecascade.empty())
else:
    print("le fishier est charge")

faces = facecascade.detectMultiScale(image, scaleFactor=1.1 , minNeighbors=5, minSize=(10,10)) 

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

face = image[y:y+h, x:x+w]
face = image[y:y+h, x:x+w]
face = cv2.resize(face, (48, 48))
face = face.astype('float32') / 255.0
face = tf.expand_dims(face, axis=-1)
face = tf.expand_dims(face, axis=0)
prediction = model.predict(face)
emotion = classes_names[tf.argmax(prediction[0])]
print(emotion)

cv2.imwrite("new.JPG", image)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

# plt.imshow(image, cmap='gray')
# plt.show()





# # model = k3.models.load_model("DL/emotion_cnn_model.keras")
# # classes_names = ('angry', 'disguasted', 'fearful', 'happy', 'neutral', 'sad', 'surprised')
# facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# image = cv2.imread("./data/test_image.png")
# # gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# if facecascade.empty()==True:
#     print("le fishier n'est pa charge:", facecascade.empty())
# else:
#     print("le fishier est charge")
# faces = facecascade.detectMultiScale(image, scaleFactor=1.1 , minNeighbors=5, minSize=(10,10)) 

# for (x,y,w,h) in faces:
#     cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
# print("c'est tout bon")

# cv2.imwrite("output_path", image)
#     # face = gris[y:y+h, x:x+w]
#     # visage = cv2.resize(visage, (48,48))
#     # visage = visage.astype('float32') / 255.0
#     # visage = tf.expand_dims(visage, axis=-1)
#     # visage = tf.expand_dims(visage, axis=0)
#     # emotion = classes_names[tf.argmax(model.predict(visage)[0])]
#     # print(emotion)


# # plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY))
# # plt.show()
