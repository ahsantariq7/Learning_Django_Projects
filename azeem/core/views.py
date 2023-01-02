from email.message import EmailMessage
from unicodedata import name
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import StratContract1,Tourism_Apply_Form,Tourism,Route_From,Route_To
from .forms import SignUpForm, ProfileForm, StartContractForm,Tourism_Apply_Form1
from django.contrib.auth.models import User
from .models import Contact,Employee
from datetime import date, datetime
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse  
from django.contrib.auth.decorators import login_required
 

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'commons/profile.html'


def contact(request):
    if request.method == 'POST':
        
        name=request.POST['name']
        email=request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact=Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()

        #sendEmail
        email_send=EmailMessage(
            'Azeem EnterPrises',#subject
            f'Hi There{name}!\n, Thanksfor contacting us.\nThis is Your {phone} \n and {desc}\n\n Thanks For Contacting Us',
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_send.fail_silently=True
        email_send.send()



        messages.success(request, 'A Contact Message Received.')
    #return HttpResponse("This is Service page")
    #return HttpResponse("This is Contact page")
    return render(request, 'contact.html',{})     



def UploadFile(request):
   
    if request.method == 'POST':
        form = StartContractForm(request.POST,request.FILES)
        name=request.POST['name']
        
        email=request.POST['email']
        price=request.POST['price']
        phone=request.POST['phone']
        desc=request.POST['desc']
        
        if form.is_valid():
            form.save()
            
            #sendEmail
        email_send=EmailMessage(
            'Azeem EnterPrises',#subject
            f'Hi There{name}!\n, Thanks for contacting us.\n  \n and \n\nYourphone no. {phone} and Price You Mentioned {price}\n  and {desc} \n on date{datetime.today()}Thanks For Starting Contract With Us',
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_send.fail_silently=True
        email_send.send()
        return redirect('home')
    else:
        form = StartContractForm()
        context = {
            'form':form,
        }

    return render(request, 'upload.html', context)


def show_contact(request):
    
    all=Contact.objects.all()
    a=len(all)
    context={'all':all,'a':a}
    return render(request, 'showcontact.html',context)

def show_contract(request):
    all=StratContract1.objects.all()
    a=len(all)
    context={'all':all,'a':a,}
    return render(request, 'showcontract.html',context)


def pin(request):
    if request.method == 'POST':
        name=request.POST['name']
        if name=='0724':
            return redirect('dashboard')
    else:
        return render(request, 'pin.html')

    return render(request, 'pin.html')
    
def employee(request):
    all=Employee.objects.all()
    a=len(all)
    context={'all':all,'a':a,}
    return render(request, 'employee.html',context)


def dashboard(request):
    all1=Employee.objects.all()
    a1=len(all1)
    all2=StratContract1.objects.all()
    a2=len(all2)
    all3=Contact.objects.all()
    a3=len(all3)
    context={'all1':all1,'a1':a1,'all2':all2,'all3':all3,'a2':a2,'a3':a3}
    return render(request, 'dashboard.html',context)

    
def order_history(request):
     
    context = {}
    all = StratContract1.objects.filter(user__id=request.user.id)
    context['orders']=all
    
    
    
    return render(request, "orderhistory.html", context)

def tourism(request):
   
    if request.method == 'POST':
        form = Tourism_Apply_Form1(request.POST)
        name=request.POST['name']
        
        email=request.POST['email']
        
        phone=request.POST['phone']
        
        
        if form.is_valid():
            form.save()
            
            #sendEmail
        email_send=EmailMessage(
            'Azeem EnterPrises',#subject
            f'Hi There{name}!\n, Thanks for contacting us.\n  \n and \n\nYourphone no. {phone} and \n   \n on date{datetime.today()}Thanks For Starting Contract With Us',
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_send.fail_silently=True
        email_send.send()
        return redirect('home')
    else:
        form = Tourism_Apply_Form1()
        context = {
            'form':form,
        }

    return render(request, 'Tourism_apply_form.html', context)

def show_tourism(request):
    all1=Tourism_Apply_Form.objects.filter(user__id=request.user.id)
    a1=len(all1)

    context={'all1':all1,'a1':a1}

    return render(request, 'Tourism_apply_form_details.html', context)

def tourism_page(request):
    all1=Tourism.objects.all()
    a1=len(all1)
    all2=Route_From.objects.all()
    a2=len(all1)
    all3=Route_To.objects.all()
    a3=len(all1)

    context={'all1':all1,'a1':a1,"all2":all2,'a2':a2,'all3':all3,"a3":a3}

    return render(request, 'Tourism_page.html', context)