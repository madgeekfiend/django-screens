from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ScreenUploadForm(forms.Form):
    caption = forms.CharField(label='Caption for the screen shot', max_length=200)
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(ScreenUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'screen-upload'
        self.helper.form_method = 'post'
        self.helper.form_action = 'screens:upload'

        self.helper.add_input(Submit('submit', 'Submit'))