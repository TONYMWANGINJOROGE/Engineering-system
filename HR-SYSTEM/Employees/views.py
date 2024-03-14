from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Employees.form import EmployeesForm
from Employees.models import Employees


# Create your views here.
def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeesForm()
        else:
            employees = Employees.objects.get(pk=id)
            form = EmployeesForm(instance=employees)
        return render(request, 'employee_form.html', {'form': form})

    else:
        if id == 0:
            form = EmployeesForm(request.POST)
        else:
            employees = Employees.objects.get(pk=id)
            form = EmployeesForm(request.POST, instance=employees)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    return render(request, 'employee_form.html', {'form': form})


def employee_list(request):
    context = {'employees_list': Employees.objects.all()}
    return render(request, 'employee_list.html', context)


def employee_delete(request, id):
    employee = Employees.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')
