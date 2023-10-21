from django import forms
# create the FormName class
class FormName(forms.Form):
      name = forms.CharField()
      email = forms.EmailField()
      text = forms.CharField(widget = forms.Textarea)