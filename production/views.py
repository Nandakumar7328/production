from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from .models import Data
from django.shortcuts import redirect


def home(request):
    myData = Data.objects.all()
    if (myData != ''):
        return render(request,'index.html',{'datas':myData})
    else:
        return render(request,'index.html')


def addData(request):
    if request.method == 'POST':
        estimated = int(request.POST["one"])
        achived = int(request.POST["two"])
        result = round((achived/ estimated)* 100)
        bonus = 0 
        if result > estimated :
            bonus = result - estimated 
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%d')
        time_str = now.strftime( '%H:%M:%S')
        
        obj = Data()
        obj.Estimated_target = estimated
        obj.Achieved_target = achived 
        obj.Score = result
        obj.Bonus = bonus
        obj.Datetime = dt_string
        obj.Time = time_str
        obj.save()
        myData = Data.objects.all()
        return redirect('home')
    return render(request,'index.html')

def updateData(request,id):
    myData = Data.objects.get(id=id)
    if request.method == "POST":
        estimated = int(request.POST["Estimated"])
        achived = int(request.POST["Achieved"])
        result = int(request.POST["Score"])
        bonus = int(request.POST["Bonus"])
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%d')
        time_str = now.strftime( '%H:%M:%S')
        myData.Estimated_target = estimated 
        myData.Achieved_target = achived 
        myData.Score = result 
        myData.Bonus = bonus 
        myData.Datetime = dt_string 
        myData.Time = time_str
        myData.save() 
        
        return redirect('home')
        
    return render(request,'update.html',{'datas':myData})


def deleteData(request,id):
    myData = Data.objects.get(id=id)
    myData.delete()
    return redirect('home')