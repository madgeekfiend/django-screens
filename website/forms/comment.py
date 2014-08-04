from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=255, label='Enter your comment')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'comment'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))