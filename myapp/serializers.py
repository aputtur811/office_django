from rest_framework import serializers
from .models import StudentAvailability, StudentSchedule, ProfessorOptions, StudentRankings

class StudentAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAvailability
        fields = '__all__'

# Similarly, define serializers for other models
