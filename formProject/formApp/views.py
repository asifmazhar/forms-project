from django.shortcuts import render


# Create your views here.
from . import forms
def form_name_views(request):
    form = forms.FormName()
     #check to see if we are getting a POST request back 
    if request.method == "POST":
        form = forms.FormName(request.POST)
          # tHEN WE CHECK to see f dthe form is valid this is an automatin validation 
        if form.is_valid():
          print("Form validation successful! See console for information:") 
          print("Name: "+form.cleaned_data['name'])
          print("email: "+form.cleaned_data['email'])
          print("message: "+form.cleaned_data['text'])
    return render(request, 'home.html',{'form':form})   