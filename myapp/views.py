from .models import StudentAvailability
from django.shortcuts import render, redirect
from .forms import StudentAvailabilityForm
from .serializers import StudentAvailabilitySerializer
from rest_framework import viewsets

def new_student_availability(request):
    if request.method == 'POST':
        form = StudentAvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_availability')
    else:
        form = StudentAvailabilityForm()
    return render(request, 'myapp/new_student_availability.html', {'form': form})


def student_availability(request):
    students = StudentAvailability.objects.all()
    return render(request, 'myapp/student_availability.html', {'students': students})

class StudentAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = StudentAvailability.objects.all()
    serializer_class = StudentAvailabilitySerializer