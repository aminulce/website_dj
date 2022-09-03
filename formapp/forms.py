from django import forms
from .models import Snippet
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#STACOVERFLOW PAGE ON HELP FOR CRISPY FORMS
#https://stackoverflow.com/questions/13098954/use-crispy-form-with-modelform
class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('form')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Submit'))
    your_name = forms.CharField(widget=forms.Textarea,label='Your name', max_length=100)

class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('snippet')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Submit'))
    class Meta:
        model = Snippet
        fields = ('job', 'resume')
