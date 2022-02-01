# USAGE
# python detect_mask_video.py

# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os

font = cv2.FONT_HERSHEY_TRIPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX_SMALL
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font4 = cv2.FONT_HERSHEY_SIMPLEX

def detect_and_predict_mask(frame, faceNet, maskNet):
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (150, 150),
		(104.0, 177.0, 123.0))

	faceNet.setInput(blob)
	detections = faceNet.forward()

	faces = []
	locs = []
	preds = []

	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]

		if confidence > 0.5:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			face = np.expand_dims(face, axis=0)

			faces.append(face)
			locs.append((startX, startY, endX, endY))

	if len(faces) > 0:
		preds = maskNet.predict(faces)

	return (locs, preds)

print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join(["face_detector", "deploy.prototxt"])

weightsPath = os.path.sep.join(["face_detector",
	"res10_300x300_ssd_iter_140000.caffemodel"])

faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

print("[INFO] loading face mask detector model...")
maskNet = load_model("mask_detector.model")

print("[INFO] starting video stream...")

vs = VideoStream(src="nvarguscamerasrc ! video/x-raw(memory:NVMM), " \
	"width=(int)1280, height=(int)720,format=(string)NV12, " \
	"framerate=(fraction)10/1 ! nvvidconv ! video/x-raw, " \
	"format=(string)BGRx ! videoconvert ! video/x-raw, " \
	"format=(string)BGR ! appsink").start()

time.sleep(2.0)

while True:
	frame = vs.read()

	cv2.putText(frame, "AI Mask Detection System for COVID-19", (15, 30), font4, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

	frame = imutils.resize(frame, width=800)

	(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

	for (box, pred) in zip(locs, preds):
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		if mask > withoutMask :
			label = "Mask"
			color = (0, 255, 0)
			cv2.putText(frame, "ACCESS GRANTED, MASK ON", (10, 50), font4, 0.8, color, 2, cv2.LINE_AA)
		else:
			label = "No Mask"
			color = (0, 0, 255)
			cv2.putText(frame, "ACCESS DENIED, No FACE-MASK", (10, 50), font4, 0.8, color, 2, cv2.LINE_AA)

		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
