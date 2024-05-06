import cv2
import numpy as np
from keras.models import load_model
from AlarmSystem import speak

model = load_model("Load your trained model")
def detect_fire(frame, threshold=0.5):
    preprocess_frame = cv2.cvtColor(cv2.resize(frame,(48,48)), cv2.COLOR_BGR2GRAY)
    preprocess_frame = np.expand_dims(preprocess_frame, axis=0)
    preprocess_frame = np.expand_dims(preprocess_frame, axis=-1)
    preprocess_frame = preprocess_frame.astype("float32")/255

    prediction = model.predict(preprocess_frame)
    if prediction[0][1] >= threshold:
        return True
    else:
        return False
    
cap = cv2.VideoCapture(r"path to fire video or non fire video to test model or instantiate zero to open webcam")
if not cap.isOpened():
    print("Error: could not open video file")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if detect_fire(frame):
        speak("Fire Alarm!!, Please Evacuate Immediately")
        cv2.rectangle(frame, (100,100),(frame.shape[1]-100, frame.shape[0]-100),(0,0,255),2)
        cv2.putText(frame, "Warning, fire is detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




