from django.shortcuts import render, get_object_or_404
from .models import Courses

def home(request):
    courses = Courses.objects.all()
    return render(request, 'index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    return render(request, 'course_detail.html', {'course': course})