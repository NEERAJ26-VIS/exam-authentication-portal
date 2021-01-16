from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myapp.forms import SignupForm
def home(request):
    return render(request,'myapp/home.html')
@login_required
def java(request):
    return render(request,'myapp/javaexams.html')
@login_required
def python(request):
    return render(request,'myapp/pythonexam.html')
@login_required
def aptitude(request):
    return render(request,'myapp/aptitudeexam.html')
def logout(request):
    return render(request,'myapp/logout.html')
def Signup(request):
    f=SignupForm()
    if request.method=='POST':
        f=SignupForm(request.POST)
        user=f.save()
        user.set_password(user.password)
        user.save()
        return redirect("/accounts/login")
    d={'form':f}
    return render(request,'myapp/signup.html',d)

