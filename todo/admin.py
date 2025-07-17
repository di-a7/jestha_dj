from django.contrib import admin
from .models import Todolist
# Register your models here.

@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
   list_display = ('id','title','status')
   list_filter = ('status',)                 # todolist.objects.filter(status="Yes", title="ndf,sn")
   search_fields = ('title','description')
   list_per_page = 5
   list_editable = ('status',)

# admin.site.register(Todolist, TodolistAdmin)