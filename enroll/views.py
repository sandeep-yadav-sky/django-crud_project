from django.shortcuts import render,HttpResponseRedirect
from . import views
from .forms import sregistration
from .models import User


def main(request):
    if(request.method == 'POST'):
        fm = sregistration(request.POST)
        if(fm.is_valid()):
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pm)
            reg.save()
    else:
        fm = sregistration()
    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu':stu})

def Delete(request,id):
    if request.method == 'POST':
        do=User.objects.get(pk=id)
        do.delete()
        return HttpResponseRedirect('/')

def Edit(request,id):
    if request.method == 'POST':
        eo = User.objects.get(pk=id)
        fm = sregistration(request.POST, instance=eo)
        if fm.is_valid():
            fm.save()
    else:
        eo = User.objects.get(pk=id)
        print("deepeu")
        fm = sregistration(instance=eo)
    return render(request, 'enroll/update.html', {'form': fm,'st':eo})
