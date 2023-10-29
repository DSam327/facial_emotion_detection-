import tensorflow as tf
from keras.layers import *
from keras import layers , models, optimizers
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.optimizers import Adam
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
from mtcnn import MTCNN

def mlmodel():
    # create model structure
    emotion_model = Sequential()
    #emotion_model.add(data_augmentation) 
    emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(BatchNormalization())
    emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(BatchNormalization())
    emotion_model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(Flatten())
    emotion_model.add(Dense(256, activation='relu'))
    emotion_model.add(Dropout(0.5))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(Dense(128, activation='relu'))
    emotion_model.add(Dropout(0.5))
    emotion_model.add(BatchNormalization())
    
    emotion_model.add(Dense(7, activation='softmax'))
    
    emotion_model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001), metrics=['accuracy'])
    
    # load weights into model
    emotion_model.load_weights("C:/Users/HP/Documents/VideoSentiment_Analysis/interface/mymodel/emotion_model.h5")
    return emotion_model

def predict_video(video2, emotion_model):
    def boxing(img, emotion_count, detector):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        lis=detector.detect_faces(img)
        for i in lis:
            x,y,w,h=i["box"]
            gray_face = gray[y:y + h, x:x + w] 
            resized=cv.resize(gray_face, (48,48))
            image_tensor = tf.convert_to_tensor(resized, dtype=tf.float32)
            # Add dimension to match with input mode 
            image_tensor = tf.expand_dims(image_tensor, 2)
            image_tensor = tf.expand_dims(image_tensor, 0)
            image_tensor=image_tensor/255
            res=emotion_model.predict(image_tensor).argmax()
            emotion_count[res]+=1
    
    def emotion_detection(video_path):
        emotion_count=[0,0,0,0,0,0,0]
        detector = MTCNN()
        video = cv.VideoCapture(video_path)
        fps = video.get(cv.CAP_PROP_FPS)
        frame_count = int(video.get(cv.CAP_PROP_FRAME_COUNT))
        duration = math.floor(frame_count/fps)
        for i in range(0,duration):
            frame_id = int(fps*(i))
            video.set(cv.CAP_PROP_POS_FRAMES, frame_id)
            ret, frame = video.read()
            if ret==True:
                boxing(frame, emotion_count, detector)
        return emotion_count
    return emotion_detection(video2)