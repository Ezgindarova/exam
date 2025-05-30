from django.shortcuts import render
from .models import iexam

def  veexam_view(request):
    exams = iexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'title': 'Езгиндарова Варвара, группа 231-365'
    }
    return render(request, 'exam_app/iexam.html', context)