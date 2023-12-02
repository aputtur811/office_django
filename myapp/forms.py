from django import forms
from .models import StudentAvailability, StudentRankings, StudentSchedule, ProfessorOptions

class StudentAvailabilityForm(forms.ModelForm):
    class Meta:
        model = StudentAvailability
        fields = ['email', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

class StudentScheduleForm(forms.ModelForm):
    class Meta:
        model = StudentSchedule
        fields = ['email', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

class ProfessorOptionsForm(forms.ModelForm):
    class Meta:
        model = ProfessorOptions
        fields = ['email', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

class StudentRankingsForm(forms.ModelForm):
    class Meta:
        model = StudentRankings
        fields = ['email', 'first', 'second', 'third']
