from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "completed", "priority", "due_date", "due_time", "category"]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(
                Q(user=user) | Q(user__isnull=True)
            )

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
            'class': 'form-input',
            'required': 'true'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Simplify the username field and clear the default verbose Django validation help text
        self.fields['username'].help_text = ""
        self.fields['username'].label = "Username"
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter a simple username',
            'class': 'form-input'
        })
        
        # Clear help texts and set classes for password fields
        if 'password1' in self.fields:
            self.fields['password1'].help_text = "Must be at least 8 characters."
            self.fields['password1'].label = "Password"
            self.fields['password1'].widget.attrs.update({
                'placeholder': '••••••••',
                'class': 'form-input'
            })
        if 'password2' in self.fields:
            self.fields['password2'].help_text = "Confirm password."
            self.fields['password2'].label = "Confirm Password"
            self.fields['password2'].widget.attrs.update({
                'placeholder': '••••••••',
                'class': 'form-input'
            })

