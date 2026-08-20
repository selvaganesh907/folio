from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactRecord
from django.contrib import messages

import json


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def education(request):
    return render(request, 'website/education.html')


def skills(request):
    return render(request, 'website/skills.html')


def projects(request):
    return render(request, 'website/projects.html')


def contact(request):
    return render(request, 'website/contact.html')




def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Automatically store form output in the database table
        ContactRecord.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            subject=subject,
            message=message
        )

        # Success message for JavaScript alert
        messages.success(request, 'Form submitted successfully! Record automatically saved and updated in the live table.')
        return redirect('contact')

    # Fetch live records to show automatically in the admin table section
    records = ContactRecord.objects.all().order_by('-created_at')
    return render(request, 'website/contact.html', {'records': records})



def psbutton(request):
    return render(request, 'psbutton.html')
