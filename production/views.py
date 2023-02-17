from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max,Min, Avg,F, DateTimeField,Count, Window
from django.db.models.functions import Trunc
from datetime import datetime,time
from django.db.models.functions import Cast
from django.db.models import FloatField
from django.utils.datastructures import MultiValueDictKeyError
from .models import Data,Process
from django.db.models.expressions import RawSQL




@login_required
def home(request):
    if request.method == 'POST':
        estimated = int(request.POST["one"])
        achived = int(request.POST["two"])
        result = round((achived/ estimated)* 100)
        user_id = request.user.id
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
            Time = time_str,
            user_id=user_id
        )
        return redirect('home')
    
    user_id = request.user.id
    data = Data.objects.filter(user_id=user_id)
    print(data,"me")
    if (data != ''):
         return render(request, 'index.html',{'datas':data})
    else:
         return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})
@login_required
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
@login_required
def deleteData(request,id):
    myData = Data.objects.get(id=id)
    myData.delete()
    return redirect('home')

@login_required
def dashboard(request):
    if request.method == 'POST':
        try:
            value = request.POST['datetime']
            shift = request.POST['shift']
            start_time = ''
            end_time = ''
            if shift == '6 AM to 12 PM':
                start_time = time(hour=6, minute=0)
                end_time = time(hour=12, minute=0)
            else :
                start_time = time(hour=13, minute=0)
                end_time = time(hour=18, minute=0)
            if not value:
                 print(shift,'shift')
                 now = datetime.now()
                 dt_string = now.strftime('%Y-%m-%d')
                 user_id = request.user.id
                 start_datetime = datetime.combine(datetime.strptime(dt_string, '%Y-%m-%d'), start_time)
                 end_datetime = datetime.combine(datetime.strptime(dt_string, '%Y-%m-%d'), end_time)
                 top_score = Data.objects.filter(Datetime=dt_string, user_id=user_id,Time__range=(start_datetime, end_datetime)).aggregate(Max('Score'))['Score__max']
                 low_score = Data.objects.filter(Datetime=dt_string,user_id=user_id ,Time__range=(start_datetime, end_datetime)).aggregate(Min('Score'))['Score__min']
                 all_order_data = Data.objects.filter(Datetime=dt_string,user_id=user_id,Time__gte=start_datetime.time(),Time__lte=end_datetime.time()).order_by('-Score')
                 chart_series = {
                'name': 'Scores',
                'data': [{'x': item.Datetime.strftime("%Y-%m-%d"), 'y': item.Score} for item in all_order_data],
                  }

                 send_data = {'top':top_score,'low':low_score,'allData':all_order_data,'chart_series': chart_series}
                 return render(request,'dashboard.html',{'topscore':send_data})

                 
            print(value, 'selected')
            print(shift,'shift')
            date = datetime.strptime(value, '%Y-%m-%d').date()
            print(date)
            user_id = request.user.id
            start_datetime = datetime.combine(date, start_time)
            end_datetime = datetime.combine(date, end_time)
            top_score = Data.objects.filter(Datetime=date,user_id=user_id ,Time__range=(start_datetime, end_datetime)).aggregate(Max('Score'))['Score__max']
            low_score = Data.objects.filter(Datetime=date,user_id=user_id ,Time__range=(start_datetime, end_datetime)).aggregate(Min('Score'))['Score__min']
            all_order_data = Data.objects.filter(Datetime=date,user_id=user_id,Time__gte=start_datetime.time(),Time__lte=end_datetime.time()).order_by('-Score')
            chart_series = {
            'name': 'Scores',
            'data': [{'x': item.Datetime.strftime("%Y-%m-%d"), 'y': item.Score} for item in all_order_data],
           }

            print(chart_series)
            send_data = {'top':top_score,'low':low_score,'allData':all_order_data,'chart_series': chart_series}
            return render(request,'dashboard.html',{'topscore':send_data})
        except MultiValueDictKeyError:
            pass
    else:
        user_id = request.user.id
        top_score = Data.objects.filter(user_id=user_id).aggregate(Max('Score'))['Score__max']
        low_score = Data.objects.filter(user_id=user_id).aggregate(Min('Score'))['Score__min']
        all_order_data = Data.objects.filter(user_id=user_id).order_by('-Score')
        chart_data = Data.objects.filter(user_id=user_id)
        chart_series = {
            'name': 'Scores',
            'data': [{'x': item.Datetime.strftime("%Y-%m-%d"), 'y': item.Score} for item in chart_data],
        }

        print(chart_series)
        send_data = {'top':top_score,'low':low_score,'allData':all_order_data,'chart_series': chart_series}
        return render(request,'dashboard.html',{'topscore':send_data})
@login_required
def cycle(request):
    avg_duration = Process.objects.annotate(duration_float=Cast('duration', FloatField())).aggregate(Avg('duration_float'))['duration_float__avg']
    print(avg_duration)
    unique_cycle_count = Process.objects.distinct('cycle_number').count()
    print(unique_cycle_count)
    data_store = Process.objects.all()
    print(data_store)
    result_object = {}
    for i in data_store:
        result_object[i.cycle_number] = i.duration
    print(result_object)
    cycleData = {'duration':round(avg_duration),'count':unique_cycle_count}
    return render(request,'cycle.html',{'cycle_data':cycleData})
def return_home(request) :
    return redirect('home')  