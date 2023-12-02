from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from myapp import views
from myapp.views import StudentAvailabilityViewSet, StudentRankingsViewSet, StudentScheduleViewSet, ProfessorOptionsViewSet

router = DefaultRouter()
router.register(r'student_availability', StudentAvailabilityViewSet)
router.register(r'student_schedule', StudentScheduleViewSet)
router.register(r'professor_options', ProfessorOptionsViewSet)
router.register(r'student_rankings', StudentRankingsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # your existing paths
    path('student_availability/', views.student_availability, name='student_availability'),
    path('new_student_availability/', views.new_student_availability, name='new_student_availability'),
    path('student_rankings/', views.student_availability, name='student_rankings'),
    path('new_student_rankings/', views.new_student_availability, name='new_student_rankings'),
    path('student_schedule/', views.student_availability, name='student_schedule'),
    path('new_student_schedule/', views.new_student_availability, name='new_student_schedule'),
    path('professor_options/', views.student_availability, name='professor_options'),
    path('new_professor_options/', views.new_student_availability, name='new_professor_options'),
]
