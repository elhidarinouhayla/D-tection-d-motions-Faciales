import cv2
import os
import tensorflow as tf
import tensorflow.keras 
import matplotlib.pyplot as plt

model = tensorflow.keras.models.load_model("DL/emotion_cnn_model.keras")
classes_names = ('angry', 'disguasted', 'fearful', 'happy', 'neutral', 'sad', 'surprised')
facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread("C:/Users/hp/Pictures/Screenshots/im2.PNG")

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
face = cv2.resize(face, (48, 48))
face = face.astype('float32') / 255.0
face = tf.expand_dims(face, axis=0)

prediction = model.predict(face)
emotion = classes_names[tf.argmax(prediction[0])]
confidence = tf.reduce_max(prediction[0]) * 100 

text = f"{emotion} ({confidence:.2f}%)"
cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

