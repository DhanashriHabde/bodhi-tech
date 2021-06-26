from django.shortcuts import render,redirect
from homepage.models import Carousel,Services,Client,About
# Create your views here.
from django.core.mail import BadHeaderError,send_mail
from django.contrib import messages
from homepage.forms import ContactForm
from django.conf import settings as conf_set
from socket import gaierror
from smtplib import SMTPAuthenticationError, SMTPDataError


def home(request):
    carou=Carousel.objects.all()
    ser=Services.objects.all()
    cli=Client.objects.all()
    abt=About.objects.all()
    context={
        'carou':carou,
        'ser':ser,
        'cli':cli,
        'abt':abt,
        }
    return render(request,'webpages/index.html',context)

def web_application(request):
    return render(request,'webpages/web_application.html')




def contact(request):

    if request.method == 'GET':

        form = ContactForm()
    else:

        form = ContactForm(request.POST)
        if form.is_valid():

            name=form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message_send="\n Name : "+name+"\n Message : "+message+"\n User Email : "+user_email
            from_email=conf_set.EMAIL_HOST_USER
            try:

                send_mail(subject,message_send,from_email, ['adityasunchal@gmail.com'])
            except (BadHeaderError,gaierror,SMTPAuthenticationError,SMTPDataError):
                
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('contact_dh')
            messages.success(request,"Thank you for contacting")
            return redirect('contact_dh')
            
    context = {
        'form': form
    }        
    return render(request, "webpages/contact.html",context)





def django(request):
    return render(request,'webpages/django.html')

def java(request):
    return render(request,'webpages/java.html')

def mobile_application(request):
    return render(request,'webpages/mobile_application.html')


def pythonpage(request):
    return render(request,'webpages/python.html')

