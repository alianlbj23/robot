from django.core.checks import messages
from django.forms.widgets import PasswordInput
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
from django import forms
from robot import models, forms
from django.shortcuts import redirect
from .models import *
import pandas as pd

from django.contrib import messages
from .forms import SignupForm
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#分頁處理
from openpyxl import Workbook #創出EXCEL檔用
import openpyxl
from datetime import datetime,timezone,timedelta
import random
from random import choice, shuffle
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()
from time import time

#from django import forms

ans_register = list() #紀錄對或錯
timer_register = list()#紀錄時間
play_time_star = list()

def index(request, pk):
    '''
    path = './使用者資料/短期記憶/' + str(name) + '/' 
    print("aaaaaaaaaaaaaaaa")
    print(path + '短期記憶.xlsx')
    if not os.path.isdir(path):
        os.mkdir(path) #如果在短期記憶沒有此人的資料夾，就新建。
        excel_file = Workbook()
        sheet = excel_file.active
        sheet['B1'] = '姓名'
        sheet['C1'] = '1'
        sheet['D1'] = '2'
        sheet['E1'] = '3'
        sheet['F1'] = '4'
        sheet['G1'] = '5'
        sheet['H1'] = '時間'
        excel_file.save(path + '/短期記憶.xlsx' )
    '''
    individual = Userdata.objects.get(pk=pk)
    
    '''
    Game = UserName.objects.filter(name = str(name)) 
    if Game.count() == 0:
        Game = UserName.objects.create(name = str(name))
        Game.save()
    '''

    '''#實驗用
    test1 = UserName.objects.get(name = str(name)) 
    test2 = GameMod.objects.get(username=test1)
    test3 = GameData.objects.filter(mod=test2)
    '''
    n = 0
    return render(request, 'index.html', locals())

def login(request):
    userdatas = Userdata.objects.all()

    #管理者刪除檔案
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        dataPk = int(request.GET.get("dataPk"))
        deleteData = Userdata.objects.filter(pk=dataPk)
        #path = str(pathlib.Path(__file__).parent.absolute())
        path = str(os.getcwd()) + "\\media\\headshot\\"
        
        #dirlist = os.listdir(path)
        deleteDataUrl = list(deleteData.values('image'))[0]['image']
        deleteDataUrl = str(deleteDataUrl).split("headshot/")[1]
        deleteDataUrl = path + str(deleteDataUrl)
        print(deleteDataUrl)
        try:#不知為啥，圖片刪掉，網頁還能輸出圖片
            os.remove(deleteDataUrl)
        except:
            pass
        deleteData.delete()
    return render(request, 'Login.html', locals())

def logout(request):
    return redirect('/')

def signup(request):
    if request.method == 'POST': #如果收到表單提交
        signup_form = forms.SignupForm(request.POST, request.FILES)
        if signup_form.is_valid():#如果每個內容都有填入的話
            signup_name = request.POST['username'].strip() #.strip()代表去掉左右的空白(space)，怕使用者打密碼時案到空白建
            signup_year = request.POST['year']
            signup_month = request.POST['month']
            signup_day = request.POST['day']
            signup_gender = request.POST['gender']
            signup_image = request.FILES['Photos'] #取得表單(forms)中的內容
            print(signup_image.name) #於終端機輸出圖片名稱
            print(signup_image.size) #於終端機輸出圖片大小(bytes)
            print(signup_image)
            #test = request.FILES['cameraFileInput']
            #print("!!!!!!!!!!!!!", test)
            #fs = FileSystemStorage()
            #sfs.save(signup_image.name, signup_image) 這兩行會直接將圖片存在media底下
            try:
                user = models.Userdata.objects.get(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender)
                message = '帳號已存在'
            except:
                signup_password = str(signup_year) + str(signup_month) + str(signup_day)
                user = Userdata.objects.create(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender, password = signup_password, image = signup_image)
                user.save()
                return redirect('/')
                #messages.add_message(request, messages.WARNING, '無此帳號')
        else:
            message = '請檢查欄位'
            #messages.add_message(request, messages.INFO, '請檢查欄位')
    else:
        signup_form = forms.SignupForm() #若表單還沒提交，用signup_form存forms的SignupForm內容後交給html顯示
    return render(request, 'SignUp.html', locals())

import pathlib
def SortTermMemoryGame(request, pk, n, gameName):
    tmp = Userdata.objects.get(pk=pk)
    
    new = GameMod.objects.filter(username = tmp, game_mod="SortTermMemoryGame") 
    if new.count() == 0:#如果玩家沒有短期記憶的資料這裡新增一個
        new = GameMod.objects.create(username = tmp, game_mod="SortTermMemoryGame")
        new.save()
    path = '.\\media\\stm_picture2'
    allFileList = os.listdir(path)#抓此目錄底下的檔案(陣列格式)
    shuffle(allFileList)
    first_picture_url =list()
    file_record = list()#紀錄哪幾個資料夾被選了
    file_record2 = list()#紀錄另外兩個資料夾
    for i in range(len(allFileList)):
        file_record.append(allFileList[i])
        url = path+'\\'+str(allFileList[i])
        filelist = os.listdir(url)
        shuffle(filelist)
        url = url+'\\'+str(filelist[0])
        first_picture_url.append(url[1:len(url)])#避開存到的逗點
        if i == 5:
            break
    pic1_first = first_picture_url[0]
    pic2_first = first_picture_url[1]
    pic3_first = first_picture_url[2]

    pic4_first = first_picture_url[3]
    pic5_first = first_picture_url[4]
    print("test!!!", pic4_first, pic5_first)
    pic_change_total = [pic1_first, pic2_first, pic3_first, pic4_first, pic5_first]
    shuffle(pic_change_total)
    
    '''
    picture = Sort_term_memory.objects.all()
    top_number = picture.count()
    first_list = []
    for i in range(3):#選三張
        id = random.randint(1, top_number) #1到最尾端隨機
        while id in first_list:
            id = random.randint(1, top_number)
        first_list.append(id)
    first_list_copy = list(first_list)#複製list
    for i in range(2):#補齊5張
        id = random.randint(1, top_number)
        while id in first_list or id in first_list_copy:#如果id有存在一開始要顯示的list，或現在這個補5張的有重複
            id = random.randint(1, top_number)
        first_list_copy.append(id)
    
    pic1_first = picture.get(number = first_list[0])
    pic2_first = picture.get(number = first_list[1])
    pic3_first = picture.get(number = first_list[2])#一開始那三張
    pic_first_total = [pic1_first, pic2_first, pic3_first]
    pic1_change = picture.get(number = first_list_copy[0])
    pic2_change = picture.get(number = first_list_copy[1])
    pic3_change = picture.get(number = first_list_copy[2])
    pic4_change = picture.get(number = first_list_copy[3])
    pic5_change = picture.get(number = first_list_copy[4])#後面要呈現的五張

    pic_change_total = [pic1_change, pic2_change, pic3_change, pic4_change, pic5_change]
    shuffle(pic_change_total)
    '''
    
    n += 1
    if n == 2:
        return redirect('/settlement/'+str(pk)+'/'+"SortTermMemoryGame/")
    return render(request, 'sort_term_memory.html',locals())

def sort_term_memory_ajax(request, pk):
    c_total = list()
    key = 0
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        score = 0
        answer1 = request.GET.get('answer1')
        answer2 = request.GET.get('answer2')
        answer3 = request.GET.get('answer3')
        count = request.GET.get('count')
        c1 = request.GET.get('c1')
        c2 = request.GET.get('c2')
        c3 = request.GET.get('c3')
        c4 = request.GET.get('c4')
        c5 = request.GET.get('c5')
        c_total = [c1, c2, c3, c4, c5]
        ans_total = [answer1, answer2, answer3]
        target = None
        while target in c_total:#將所有的None移除
            c_total.remove(target) 
        for i in c_total: #確認有沒有全對
            if i in ans_total:
                key += 1
        
        if key == 1:
            score = 33
        elif key == 2:
            score = 66
        elif key == 3:
            score = 100
        else:
            score = 0
        userdata = Userdata.objects.get(pk=pk)
        
        gamemod = GameMod.objects.get(username=userdata, game_mod="SortTermMemoryGame")
        
        New = Sort_term_memory.objects.create(mod=gamemod, correct_rate=score, costTime=int(count))
        New.save()

        
    return JsonResponse(answer1, safe=False)

def AttentionGame(request, pk, n, gameName):
    tmp = Userdata.objects.get(pk=pk)
    new = GameMod.objects.filter(username = tmp, game_mod="AttentionGame") 
    if new.count() == 0:#如果玩家沒有注意力的資料這裡新增一個
        new = GameMod.objects.create(username = tmp, game_mod="AttentionGame")
        new.save()
    return render(request, 'attention2.html',locals())

def AttentionGameAjax(request, pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        ans1 = int(request.GET.get("ans1"))
        ans2 = int(request.GET.get("ans2"))
        ans3 = int(request.GET.get("ans3"))
        #先將資料傳入外部資料結構
        ans_register = [ans1, ans2, ans3]
        print(ans_register)
        correct = 0
        correct_list = [6, 9, 12]
        correct_slow_list = [7, 10, 13]
        for i in range(3):
            if ans_register[i] in correct_list:
                correct += 33
            if ans_register[i] in correct_slow_list:
                correct += 23
        if correct == 99:
            correct = 100

        userdata = Userdata.objects.get(pk=pk)
        gamemod = GameMod.objects.get(username=userdata, game_mod="AttentionGame")
        NewAttentionData = Attention.objects.create(mod=gamemod, correct_rate=correct)
        NewAttentionData.save()
        
        #-----------------------資料庫測試
        '''
        username = UserName.objects.get(name=str(name))
        gamemod = GameMod.objects.get(username=username, game_mod="attention")
        new = Attention.objects.create(mod=gamemod, correct_rate=correct)
        new.save()
        '''
        return JsonResponse(ans1, safe=False)



def settlement(request, pk, gameMod):
    #try:
    tmp = Userdata.objects.get(pk=pk)
    gameModData = GameMod.objects.get(username=tmp, game_mod=gameMod)
    count = 0;
    #短期記憶的設計要等到資料都有了才寫進資料庫，故在結算時才將資料寫入
    if gameMod == "SortTermMemoryGame":
        sorttermmemory = Sort_term_memory.objects.filter(mod=gameModData).first()
        count = Sort_term_memory.objects.filter(mod=gameModData).count()
    if gameMod == "AttentionGame":
        attention = Attention.objects.filter(mod=gameModData).first()
        count = Attention.objects.filter(mod=gameModData).count()
    if gameMod == "OrientationGame":
        OrientationGame = Orientation.objects.filter(mod=gameModData).first()
        count = Orientation.objects.filter(mod=gameModData).count()
    #except:
        #return redirect('/index/'+str(pk)+'/')
    return render(request, 'settlement.html', locals())
    
def introduction(request, pk, gameName):
    #將外部資料結構數值重製，避免輸出到前一個或未完成的遊戲數據
    ans_register.clear()
    timer_register.clear()
    play_time_star.clear()
    key = 0
    game_data = game.objects.get(title = gameName)
    if gameName == "短期記憶遊戲":
        title = "SortTermMemoryGame"
        key = 1
    if gameName == "注意力遊戲":
        title = "AttentionGame"
        key = 2
    if gameName == "定向力遊戲":
        title = "OrientationGame"
        key = 3
    n = 0
    return render(request, 'introduction.html', locals())


def OrientationGame(request, pk, n, gameName):
    tmp = Userdata.objects.get(pk=pk)
    new = GameMod.objects.filter(username = tmp, game_mod="OrientationGame") 
    if new.count() == 0:#如果玩家沒有注意力的資料這裡新增一個
        new = GameMod.objects.create(username = tmp, game_mod="OrientationGame")
        new.save()
    randomColor = ["#ff6384", "#36a2eb", "#ffce56", "#9966ff"]
    shuffle(randomColor)    
    return render(request, 'Orientation2.html', locals())

def OrientationAjax(request, pk):
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        correct = int(request.GET.get("correct"))
        costtime = int(request.GET.get("count_number"))
        userdata = Userdata.objects.get(pk=pk)
        gamemod = GameMod.objects.get(username=userdata, game_mod="OrientationGame")
        score = 0
        if correct == 0:
            score = 0
        elif correct == 1:
            score = 33
        elif correct == 2:
            score = 66
        elif correct == 4:
            score = 100
        
        newOrientationData = Orientation.objects.create(mod=gamemod, correct_rate=score, costTime=costtime)
        newOrientationData.save()
        return JsonResponse(correct, safe=False)

def OrientationPadGame(request, pk, n, gameName):
    tmp = Userdata.objects.get(pk=pk)
    new = GameMod.objects.filter(username = tmp, game_mod="OrientationGame") 
    if new.count() == 0:#如果玩家沒有注意力的資料這裡新增一個
        new = GameMod.objects.create(username = tmp, game_mod="OrientationGame")
        new.save()
    randomColor = ["#ff6384", "#36a2eb", "#ffce56", "#9966ff"]
    shuffle(randomColor)
    colors = ["#ff6384", "#36a2eb", "#ffce56", "#9966ff"]
    return render(request, 'OrientationPad2.html', locals())
# Create your views here.

def historyEnterPage(request, pk):
    return render(request, 'historyEnterPage.html', locals())

from datetime import datetime
import time
def historyYear(request, pk, gameName):
    YearNow = int(time.strftime('%Y', time.localtime()))
    yearList = list(range(2021,YearNow+1))
    return render(request, 'historyYear.html', locals())

def historyMonth(requset, pk, gameName, year):
    monthList = list(range(1, 13))
    return render(requset, 'historyMonth.html', locals())

import calendar
def historyDay(request, pk, gameName, year, month):
    monthList = list(range(1, 13))
    day = calendar.monthrange(int(year), int(month))
    day = int(day[1])
    dayList = list(range(1,day+1))
    return render(request, 'historyDay.html', locals())

from datetime import date
def historyChart(request, pk, gameName, year, month, day):
    userdata = Userdata.objects.get(pk=pk)
    gamemode = GameMod.objects.get(username=userdata,game_mod=gameName)
    if gameName == "SortTermMemoryGame":
        key = 1
    if gameName == "AttentionGame":
        key = 2
    if gameName == "OrientationGame":
        key = 3
    if year!=0 and month!=0 and day!=0:#要找某天的
        title = str(year)+"年"+str(month)+"月"+str(day)+"日"
        if key == 1:
            totalData = Sort_term_memory.objects.filter(mod=gamemode)
            totalData = totalData.filter(add_time__month=month,add_time__day=day).order_by("add_time")
        elif key == 2:
            totalData = Attention.objects.filter(mod=gamemode)
            totalData = totalData.filter(add_time__month=month,add_time__day=day).order_by("add_time")
        elif key == 3:
            totalData = Orientation.objects.filter(mod=gamemode)
            totalData = totalData.filter(add_time__month=month,add_time__day=day).order_by("add_time")

    elif year != 0 and month != 0 and day == 0:
        title = str(year)+"年"+str(month)+"月"
        if key == 1:
            totalData = Sort_term_memory.objects.filter(mod=gamemode)
            totalData = totalData.filter(add_time__month=month).order_by("add_time")
        elif key == 2:
            totalData = Attention.objects.filter(mod=gamemode)
            totalData = totalData.filter(add_time__month=month).order_by("add_time")
        elif key == 3:
            totalData = Orientation.objects.filter(mod=gamemode)
            totalData = totalData.filter(add_time__month=month).order_by("add_time")
    totalNumber = totalData.count()
    
    
    return render(request, 'historyChart.html', locals())

