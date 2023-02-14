from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from .models import Data
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist



def home(request):
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
        
        Data.objects.create(
            Estimated_target = estimated,
            Achieved_target = achived,
            Score = result,
            Bonus = bonus,
            Datetime = dt_string,
            Time = time_str
        )
        return redirect('home')
    
    
    data = Data.objects.all() 
    if (data != ''):
         return render(request, 'index.html',{'datas':data})
    else:
         return render(request, 'index.html')
     
# def addData(request):
#     if request.method == 'POST':
#         estimated = int(request.POST["one"])
#         achived = int(request.POST["two"])
#         result = round((achived/ estimated)* 100)
#         bonus = 0 
#         if result > estimated :
#             bonus = result - estimated 
#         now = datetime.now()
#         dt_string = now.strftime('%Y-%m-%d')
#         time_str = now.strftime( '%H:%M:%S')
        
#         Data.objects.create(
#             Estimated_target = estimated,
#             Achieved_target = achived,
#             Score = result,
#             Bonus = bonus,
#             Datetime = dt_string,
#             Time = time_str
#         )
#         return redirect('home')
#     return render(request,'index.html')

def updateData(request,id):
    myData = Data.objects.get(id=id)
    if request.method == "POST":
        estimated = int(request.POST["Estimated"])
        achived = int(request.POST["Achieved"])
        result = round((achived/ estimated)* 100)
        bonus = 0 
        if result > estimated :
            bonus = result - estimated 
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%d')
        time_str = now.strftime( '%H:%M:%S')
        myData = Data.objects.filter(id=id).update(
            Estimated_target = estimated ,
            Achieved_target = achived ,
            Score = result ,
            Bonus = bonus ,
            Datetime = dt_string,
            Time = time_str
        )
        
        return redirect('home')
        
    return render(request,'update.html',{'datas':myData})

def deleteData(request,id):
    myData = Data.objects.get(id=id)
    myData.delete()
    return redirect('home')