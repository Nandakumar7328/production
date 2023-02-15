from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from .models import Data
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max,Min

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
    print(data,"me")
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

def dashboard(request):
    if request.method == 'POST':
        selected_date_str = request.POST.get('date')
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
        print(selected_date)
        top_score = Data.objects.filter(Datetime=selected_date).aggregate(Max('Score'))['Score__max']
        low_score =  Data.objects.filter(Datetime=selected_date).aggregate(Min('Score'))['Score__min']
        all_order_data = Data.objects.order_by('-Score')
        send_data = {'top':top_score,'low':low_score,'allData':all_order_data}
        return render(request,'dashboard.html',{'topscore':send_data})
    else:
        top_score = Data.objects.aggregate(Max('Score'))['Score__max']
        low_score = Data.objects.aggregate(Min('Score'))['Score__min']
        all_order_data = Data.objects.order_by('-Score')
        chart_data = Data.objects.all()
        import datetime
        chart_series = {
            'name': 'Scores',
            'data': [{'x': item.Datetime.strftime("%Y-%m-%d"), 'y': item.Score} for item in chart_data],
        }

        print(chart_series)
        send_data = {'top':top_score,'low':low_score,'allData':all_order_data,'chart_series': chart_series}
        return render(request,'dashboard.html',{'topscore':send_data})

def return_home(request) :
    return redirect('home')    