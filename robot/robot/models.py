from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.utils import timezone

class Userdata(models.Model):
    name = models.CharField(max_length=50) 
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    gender = models.CharField(max_length=10) 
    password = models.CharField(max_length=50)
    #將儲存圖片位置定義在設定放靜態檔(在setting中設定的media資料夾)，底下的image資料夾下
    #http://127.0.0.1:8000/media/image/~~~~~.jpg 可直接在網頁上顯示該資料夾底下的圖片
    image = models.ImageField(upload_to='headshot/', blank=False, null=False) 
    def __str__(self):
        return self.name



class game(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self):
        return self.title

class store_point(models.Model):
    topic = models.CharField(max_length=10)
    time = models.PositiveIntegerField()
    ans = models.BooleanField()


class UserName(models.Model):
    name = models.CharField(max_length=30) 
    def __str__(self):
        return self.name

class GameMod(models.Model):
    username = models.ForeignKey(Userdata, on_delete=models.CASCADE)
    game_mod = models.CharField(max_length=30) 
    def __str__(self):
        return self.game_mod
        
class Orientation(models.Model):
    mod = models.ForeignKey(GameMod, on_delete=models.CASCADE)
    correct_rate = IntegerField()
    costTime = IntegerField()
    add_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ["-add_time"]
    def __str__(self):
        return str(self.correct_rate)
#注意力
class Attention(models.Model):
    mod = models.ForeignKey(GameMod, on_delete=models.CASCADE)
    correct_rate = IntegerField()
    add_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ["-add_time"]
    def __str__(self):
        return str(self.correct_rate)

#這兩個都是短期記憶用的
'''
class Sort_term_memory(models.Model):
    mod = models.ForeignKey(GameMod, on_delete=models.CASCADE)
    one = models.BooleanField()
    add_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ["-add_time"]
    def __str__(self):
        return str(self.add_time)

class TimeStore(models.Model):
    sort_term_memory = models.ForeignKey(Sort_term_memory, on_delete=models.CASCADE)
    time_one = models.CharField(max_length=30)
    def __str__(self):
        return str(self.sort_term_memory)
'''
class Sort_term_memory(models.Model):
    mod = models.ForeignKey(GameMod, on_delete=models.CASCADE)
    correct_rate = models.IntegerField()
    costTime = IntegerField()
    add_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ["-add_time"]
    def __str__(self):
        return str(self.add_time)
#_____________________________________________________________

# Create your models here.
