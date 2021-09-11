from web.models import Patient
from django.shortcuts import render

def index(request):
    context = {}
    context["patient"] = Patient.objects.all()
    return render(request, "index.html", context)

def detail(request, id):
    context = {}
    Patients = patient.objects.filter(id=id)
    for patient in patient:
        context["patient"] = patient

        return render(request, "detail.html", context)

def about(request):
    return render(request, "Physisian.html")

def contact(request):
    return render(request, "Patient.html")
