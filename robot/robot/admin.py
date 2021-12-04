from django.contrib import admin
from robot.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
admin.site.register(game, GameAdmin)

class UserdataAdmin(admin.ModelAdmin):
    list_display = ['name',  'year', 'month', 'day', 'gender', 'password', 'image']

admin.site.register(Userdata, UserdataAdmin)

class UserNameAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(UserName, UserNameAdmin)

class GameModAdmin(admin.ModelAdmin):
    list_display = ['username', 'game_mod']
admin.site.register(GameMod, GameModAdmin)

#class Sort_term_memoryAdmin(admin.ModelAdmin):
#    list_display = ['mod', 'two', 'three', 'four', 'five', "add_time"]
#admin.site.register(Sort_term_memory, Sort_term_memoryAdmin)
#admin.site.register(Sort_term_memory)

class Sort_term_memoryAdmin(admin.ModelAdmin):
    list_display = ['mod', 'correct_rate', "costTime", "add_time"]
admin.site.register(Sort_term_memory, Sort_term_memoryAdmin)



class AttentionAdmin(admin.ModelAdmin):
    list_display = ['mod','correct_rate', "add_time"]
admin.site.register(Attention, AttentionAdmin)

class OrientationAdmin(admin.ModelAdmin):
    list_display = ['mod','correct_rate', "costTime","add_time"]
admin.site.register(Orientation, OrientationAdmin)