from django import forms
from to_do_app.models import Task_Details
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Fieldset


class TasklistForms(forms.ModelForm):
    class Meta:
        model = Task_Details
        fields = ('Task_Id','Task_desc','Task_date_time','Task_status','Task_created','Task_modified')

class TaskupdateForms(forms.ModelForm):

    print('===============ITupdateForms>')
    class Meta:
        model = Task_Details
        fields = ('Task_Id','Task_desc','Task_date_time','Task_status','Task_created','Task_modified')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Details'))
        self.helper.add_input(Submit('cancel_button', u'Cancel'))

class TaskcreateForms(forms.ModelForm):
    class Meta:
        model = Task_Details
        fields = ('Task_Id','Task_desc','Task_date_time','Task_status','Task_created','Task_modified')
