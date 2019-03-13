from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from datetime import datetime

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        topic = request.POST['topic']
        comment = request.POST['comment']

        contact = Contact(name=name, email=email ,topic=topic ,comment=comment ,submit_time=datetime.now())
        contact.save()
        messages.success(request, 'پیغام شما ارسال شد ، به زودی  برسی خواهد شد')
        return redirect('contact')
    else :
        return render(request,'pages/contact.html')





      


    
    
