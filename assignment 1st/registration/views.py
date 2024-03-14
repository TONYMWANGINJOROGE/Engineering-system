from django.shortcuts import render, redirect
from registration.forms import RegisterForm, employeekinForm
from django . contrib import messages


# Create your views here.
def regista(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()
            messages.success(request, 'user registered successfully!')
            return redirect('regista')
    else:
        form = RegisterForm()

    return render(request, 'regista.html', context={'form': form})


def employeedetails(request):
    form = employeekinForm
    if request.method == 'POST':
        form = employeekinForm (request.POST)
    if form .is_valid():
        form.save()
        form = employeekinForm()
        messages.success(request, 'registered successfully!')
        return redirect('employeedetails')
    else:
        form = employeekinForm()
    return render(request, '')
    return render(request, 'employeedetails.html', context={'form': form})



