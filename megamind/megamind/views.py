from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def events(request):
    return render(request,'events.html')

def course_details(request):
    return render(request,'course-details.html')

def courses(request):
    return render(request,'courses.html')

def pricing(request):
    return render(request,'pricing.html')

def trainers(request):
    return render(request,'trainers.html')

def abacus_d(request):
    return render(request,'course-details/abacus-d.html')