from django.shortcuts import render,HttpResponse,redirect
from htmlapp.models import DisplayData


def home(request):
    return render(request, 'home.html')

def name(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        DisplayData(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            age=request.POST.get('age'),
            add=request.POST.get('add')
        ).save()
        return HttpResponse('success')

def dis(request):
    af=DisplayData.objects.all()
    return render(request,'show.html',{'af':af})


def delete(request,id):
    employee = DisplayData.objects.get(id=id)
    employee.delete()
    return redirect('add')  


# def update(request,id):
#     emp=DisplayData.objects.get(id=id)
#     emp.name=request.POST.get('name')
#     emp.email=request.POST.get('email')
#     emp.age=request.POST.get('age')
#     emp.add=request.POST.get('add')
#     emp.save()
#     return redirect('add')


# this update function is not working as expected so you can ty next time whwn you free thank you for comeing here



