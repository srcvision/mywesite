from django.shortcuts import render
from datetime import datetime
from .models import Submission


def home(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'home.html', {'time': current_time})

def submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        submission = Submission(name=name, email=email)
        submission.save()
        return render(request, 'submitted.html', {'name': name, 'email': email})
    return render(request, 'home.html')

def submissions(request):
    all_submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': all_submissions})
