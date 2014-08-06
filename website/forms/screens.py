from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from website.models import Screen


class ScreenUploadForm(ModelForm):
    class Meta:
        model = Screen
        fields = ['caption', 'image', 'team']

    def __init__(self, *args, **kwargs):
        super(ScreenUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'screen-upload'
        self.helper.form_method = 'post'
        self.helper.form_action = 'screens:upload'
        self.helper.add_input(Submit('submit', 'Submit'))