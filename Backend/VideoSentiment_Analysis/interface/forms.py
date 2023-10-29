from django import forms

class VideoUploadForm(forms.Form):
    video = forms.FileField(
        label='Upload Video',
        help_text='Only .mp4 files are allowed.',
        widget=forms.ClearableFileInput(attrs={'accept': '.mp4'})
    )
    email = forms.EmailField(
        label='Email',
        help_text='Enter your email address',
        widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'})
    )
