from django import forms
from pastes.models import Paste

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
