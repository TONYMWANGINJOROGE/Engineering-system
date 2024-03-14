from django.shortcuts import render
from Users.forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contact(request):
    form = RegistrationForm()
    return render(request, 'contacts.html',context={'form':form})
