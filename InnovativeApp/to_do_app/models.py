from django.db import models
import datetime

# Create your models here.
class Task_Details(models.Model):

    in_progress = 'progress'
    completed   = 'completed'
    pending     = 'pending'

    Status = (
        (in_progress,   'In Progress'),
        (completed,     'Completed'),
        (pending,       'Pending'),
    )

    Task_Id         = models.CharField(unique=True,max_length=10,verbose_name='Task ID')
    Task_desc       = models.CharField(max_length=200,verbose_name='Task Description')
    Task_date_time  = models.DateField(("Current Date"), default=datetime.date.today)#,verbose_name='Resignation Date')
    Task_status     = models.CharField(max_length=10,choices=Status,default=in_progress,)
    Task_created    = models.DateField(("Created Date"), default=datetime.date.today)#,verbose_name='Resignation Date')
    Task_modified   = models.DateField(("Modified Date"), default=datetime.date.today)#,verbose_name='Resignation Date')

    def __str__(self):
            return ''
