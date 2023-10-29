from django.shortcuts import render, redirect
from .forms import VideoUploadForm  # Import your VideoUploadForm
from .model_loading import mlmodel, predict_video  # Import your model loading function
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Video
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings

def send_analysis_email(email, analysis):
    tot_sum=sum(analysis)
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
    subject = 'Result of the Sentiment Analysis of '
    message = 'Here are the analysis results of the video you requested\n'
    for i in range(len(analysis)):
        message+=emotion_dict[i]+': ' + str((analysis[i]*100)/tot_sum) + '\n'
    from_email = 'samrathsingh313@gmail.com'  # Your Gmail email address
    recipient_list = [email]  # The recipient's email address

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES['video']  # Get the video file
            email = form.cleaned_data['email']  # Get the email

            # Save the video to the database
            #video = Video(video_file=video_file, email=email)
            #video.save()
            # Define the path to save the temporary video file
            video_path = os.path.join(settings.MEDIA_ROOT, 'videos', video_file.name)
            with open(video_path, 'wb') as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)

            # Save the temporary video file to the defined path
            # Perform predictions using your loaded model
            loaded_model = mlmodel()  # Load your machine learning model
            analysis = predict_video(video_path, loaded_model)  # Implement a function to make predictions
            send_analysis_email(request.POST.get('email'), analysis)  # Implement a function to send an email
            return HttpResponse('Analysis is being sent to your email.')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_form.html', {'form': form})
