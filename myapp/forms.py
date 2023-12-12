from django import forms
from django.utils import timezone  # Add this import
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'notes']

    def save(self, commit=True):
        contact = super().save(commit=False)
        contact.created_time = timezone.now()
        if commit:
            contact.save()
        return contact