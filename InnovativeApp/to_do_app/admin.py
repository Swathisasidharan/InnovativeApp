from django.contrib import admin
from django.contrib.auth.models import Group
from to_do_app.models import Task_Details
from to_do_app.actions import export_as_csv_action

# admin.site.register(Task_Details)

class to_proxy(Task_Details):
    #print('Employee1_proxy')
    class Meta:
        proxy = True
        verbose_name = 'Task Id'
        verbose_name_plural = 'Task ids'

# class Toutline(admin.ModelAdmin):
#     inlines = [
#     ]
#     list_display = ('Task_Id', 'Task_created',)
#     search_fields = ['Task_Id']
#
# admin.site.register(to_proxy,Toutline)

# class TaskAdmin(admin.ModelAdmin):
#     search_fields = ('Task_Id',)
#
# admin.site.register(Task_Id,TaskAdmin)

class case_proxy(Task_Details):
    #print('Employee1_proxy')
    class Meta:
        proxy = True
        verbose_name = 'Case'
        verbose_name_plural = 'For Export'

class CaseAdmin(admin.ModelAdmin):
    actions = [export_as_csv_action("CSV Export", fields=['Task_Id', 'Task_created'])]
    list_display = ('Task_Id', 'Task_created',)
    search_fields = ['Task_Id']
admin.site.register(case_proxy,CaseAdmin)
