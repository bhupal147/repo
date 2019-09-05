
from django.shortcuts import render,redirect

from .forms import registrationform,Loginform
from .models import Registration
from django.http.response import HttpResponse
def registration_view(request):
    if request.method=='POST':
        rform=registrationform(request.POST)
        if rform.is_valid():
            firstname=request.POST.get('first_name')
            lastname=request.POST.get('last_name')
            username=request.POST.get('username')
            password=request.POST.get('pwd')
            mobile=request.POST.get('mobile')
            data=Registration(fname=firstname,lname=lastname,username=username,password=password,mobile=mobile)
            data.save()
            rform = registrationform()
            return render(request, 'reg'
                                   '.html', {'rform': rform})


        else:
            return HttpResponse('invalid userdata')
    else:
        rform=registrationform()
        return render(request,'reg.html',{'rform':rform})
def login_view(request):
    if request.method=='POST':
        lform=Loginform(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('pwd')
            uname=Registration.objects.filter(username=username)
            pwd=Registration.objects.filter(password=password)
            if uname and pwd:
                return redirect('/home/')
            else:
                return HttpResponse('wrong details')

        else:
            return HttpResponse("invalid user data")

    else:
        lform=Loginform()
        return render(request,'login.html',{'lform':lform})
def sucess_view(request):
    return render(request,'sucess.html')

