from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contacts(request):
    return render(request, 'contacts.html')
def register(request):
    return render(request, 'register.html')
def logout(request):
    return render(request, 'logout.html')

