from django import forms
from hello.models import LogMessage

class LogMessageForm(forms.ModelForm):
    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your message here...',
            'class': 'form-control',
            'rows': 3,
        }),
        label='Message',
        help_text='Maximum 300 characters.'
    )
    log_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
        }),
        label='Log Date',
        help_text='Select the date and time for logging the message.'
    )

    class Meta:
        model = LogMessage
        fields = ("message", "log_date")