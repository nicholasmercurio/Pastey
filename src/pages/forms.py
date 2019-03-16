from django import forms
from pastes.models import Paste
from django.db.models import Q
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    SYNTAX_CHOICES = {
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    }

    class Meta:
        model       = Paste
        fields      = ('title', 'content', 'syntax', 'public')
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"})}

class ShareForm(forms.Form):
    username = forms.CharField(help_text = "username or email")

    def clean_username(self):
        value = self.cleaned_data["username"]
        if User.objects.filter(Q(username=value)|Q(email=value)).count() ==1:
            return value
        else:
            raise forms.ValidationError("Could not find user! " + value)
