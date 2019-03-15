from django import forms
from pastes.models import Paste

#class HomeForm(forms.Form)
class PostForm(forms.ModelForm):
    SYNTAX_CHOICES = {
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    }

#    content     = forms.CharField(max_length=10000)
#    title       = forms.CharField(max_length=30)
#    syntax      = forms.ChoiceField(choices=SYNTAX_CHOICES, widget=forms.Select(), required=True)
#    public      = forms.BooleanField(required=False)
    #generated_url = forms.CharField(max_length=6)

    class Meta:
        model       = Paste
        fields      = ('content', 'title', 'syntax', 'public')
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"})}
