from django.shortcuts import render , HttpResponse , redirect
from .models import Task
from .forms import  TaskForm
from django.views import View
# Create your views here.


class IndexView(View):
    def get(self, request):
        tasks =Task.objects.all()
        form = TaskForm()
        context = {'tasks': tasks , "form":form }
        return render(request,'index.html',context)
    def post(self,request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')




def edit(request,pk) :
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST': 
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'task':task , 'form' : form }

    return render(request,'update.html' ,context)


def delete(request,pk) :
    task = Task.objects.get(id=pk)


    if request.method == 'POST': 
        task.delete()
        return redirect('/')
    
    context = {'task':task  }

    return render(request,'delete.html' ,context)
    
