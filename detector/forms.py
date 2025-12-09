from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({
                'class': 'w-full border rounded px-3 py-2 mt-1'
                })

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
class CustomLoginForm(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({
                'class': 'w-full border rounded px-3 py-2 mt-1'
            })
    
    class Meta:
        model = User
        fields = ('username', 'password')