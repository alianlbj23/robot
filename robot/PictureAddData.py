import pathlib
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()
from robot.models import Sort_term_memory 

path = str(pathlib.Path(__file__).parent.absolute()) + '\media\stm_picture' #取得現在這個py檔的絕對路徑之後再加上放圖片的位置
dirlist = os.listdir(path) #取得path路徑下的所有檔案 
pictruesdb = Sort_term_memory.objects.all()
pictruesdb.delete() #刪除位於資料庫所有的照片
count = 1
for i in dirlist:  
    pictrue_link = 'stm_picture/' + str(i) #圖片的url
    print(pictrue_link)
    print(pictrue_link) #用來自己看的
    pictruesdb = Sort_term_memory.objects.create(image = pictrue_link, number = count)
    pictruesdb.save()
    count += 1