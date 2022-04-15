from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import LoginForm, PatientForm
from .models import Doctor, Patient


# Create your views here.
def login(request):
    global userentry
    userentry = '\0'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userentry = form.cleaned_data['username']
            passentry = form.cleaned_data['password']
            data = Doctor.objects.filter(username=userentry).filter(password=passentry)
            if len(data) == 1:
                return redirect(reverse('doctor:homepage'))
    else:
        form = LoginForm()

    return render(request, 'doctor/login.html', context={'form': form})


def homepage(request):
    data = Doctor.objects.get(username=userentry)
    return render(request, 'doctor/homepage.html', context={'data': data})


def addrecord(request):  # ADD PATIENT
    data = Doctor.objects.get(username=userentry)
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor:listpatients'))
    else:
        form = PatientForm()

    return render(request, 'doctor/patient_form.html', context={'form': form})


class PatientListView(ListView):
    model = Patient
    queryset = Patient.objects.order_by('pk')
    context_object_name = 'patientlist'


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('doctor:listpatients')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('doctor:listpatients')
