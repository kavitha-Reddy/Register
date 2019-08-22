from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration
from . forms import Registration2,Login
from django.core.mail import send_mail
from random import randint

def register(request):
    form=Registration2()
    if request.method=='POST':
        form=Registration2(request.POST)
        if form.is_valid():
            n='KV'
            for i in range(0,4):
                n=n+str(randint(0,9))
            reg_id=n
            name=form.cleaned_data['name']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            cno=form.cleaned_data['cno']
            k=Registration(reg_id=reg_id,name=name,password=password,email=email,cno=cno)
            k.save()
            reg_id=request.session['id']=k.reg_id
            sub="registration success"
            sender='kavipy2@gmail.com'
            msg="Hello Mr/Ms."+request.POST['name']+"\n"+"register_id:"+reg_id+"\n"+"\n""Password:"+request.POST['password']+"\n"+"your application submited successfully."+"\n"+"- It is auto genrated yahoo mail."
            # msg2="Thank you for register"+"\n"+"it is auto generated mail"
            to=request.POST['email']
            send_mail(sub,msg,sender,[to]) 
    return render(request,'register.html',{'form':form})
def login(request):
    form=Login()
    if request.method=='POST':
        form=Login(request.POST)
        if form.is_valid():
            reg_id=form.cleaned_data['reg_id']
            password =form.cleaned_data['password']
            user=Registration.objects.filter(reg_id=reg_id,password=password)
            if not user:
                return HttpResponse("""login failed""")
            else:
                return HttpResponse("""login successfully""")
    return render(request,'login.html',{'form':form})    
