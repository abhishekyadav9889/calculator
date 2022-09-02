from django.contrib import admin
from.models import * 
from sample.models import username

# Register your models here.
class userinfoadmin(admin.ModelAdmin):
    list_display =('id', 'name')



admin.site.register (username,userinfoadmin)