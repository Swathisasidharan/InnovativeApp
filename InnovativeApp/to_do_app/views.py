from django.shortcuts import render
from to_do_app.forms  import TasklistForms,TaskupdateForms,TaskcreateForms
from django.views.generic   import ListView,UpdateView,CreateView
from to_do_app.models       import Task_Details
from django.urls            import reverse_lazy
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
import sqlite3

class TaskListView(ListView):
    model = Task_Details
    form_class = TasklistForms
    template_name = 'to_do_app/task_list.html'
    context_object_name = 'to_do_app'
    # success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task_Details
    form_class = TaskupdateForms
    template_name = 'to_do_app/Task_form.html'
    success_url = reverse_lazy('task_list')

class TaskCreateView(CreateView):
    model = Task_Details
    template_name = 'to_do_app/Task_form.html'
    fields = ('Task_Id','Task_desc','Task_date_time','Task_status','Task_created','Task_modified')
    success_url = reverse_lazy('task_list')


    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields['Task_Id'].required = True
        form.fields['Task_desc'].required = True
        form.fields['Task_date_time'].required = True
        form.fields['Task_status'].required = True
        form.fields['Task_created'].required = True
        form.fields['Task_modified'].required = True

        return form

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            form = TaskcreateForms(request.POST)
            if form.is_valid():
                task_field = [form.cleaned_data['Task_Id'],form.cleaned_data['Task_desc'],form.cleaned_data['Task_date_time'],form.cleaned_data['Task_status'],form.cleaned_data['Task_created'],form.cleaned_data['Task_modified']]
                print('======================employee field>',task_field)
                form.save()
                return redirect('task_list')
                #print(form)
        print('=================5>')
        print(form)
        return render(request, 'to_do_app/Task_form.html', {'form': form})

def query_with_fetchone():

    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT * FROM to_do_app_task_details")
        result1 = c.fetchall()
        print("-----------------------------------------")
        print("*********Display Entire Tables***********")
        print("-----------------------------------------\n")
        print(result1)

        print("")
        print("-----------------------------------------")
        print("******Based on ID, data has shown********")
        print("-----------------------------------------\n")
        c = conn.cursor()
        c.execute("SELECT * FROM to_do_app_task_details where Task_Id='TID002'")
        # c.execute("SELECT * FROM to_do_app_task_details where Task_Id=?",(Task_Id,))
        result2 = c.fetchall()
        print(result2)
        print(" ")
        conn.commit()
        c.close()
    except :
        print("Error in the database")

query_with_fetchone()
