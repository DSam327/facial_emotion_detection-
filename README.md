# Emotion Detector

## Description
The model aims to take in video as an input and give the statistics for each emotion throughout the video. Uses the FER-2013 dataset for training and employs CNN layers to train the model.

Also employs backend to send the results on mail, although the video after being uploaded is stored on the local engine and this requires setting up gmail id and password to send the mail to the recipient

## Information
The model used for this task is a a simple CNN model that use Conv2D, Max Pooling and Batch Normalization layers with the model eventually being flattened and used as classifier
### Accuracy
Training-94.45%

Testing-62.97%

## Screenshot
#### Uploading the video along with email
<img width="960" alt="Screenshot 2023-10-29 193015" src="https://github.com/DSam327/facial_emotion_detection-/assets/113661235/d30ac46d-00dc-43f1-bb7e-ae7b96ec4b6f">

#### Getting the result on mail
<img width="960" alt="Screenshot 2023-10-29 193015" src="https://github.com/DSam327/facial_emotion_detection-/assets/113661235/13d34e0e-289f-47fc-8b45-2255706c9d28">

