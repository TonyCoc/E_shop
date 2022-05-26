from django import forms


class image_input(forms.Form):
    image = forms.ImageField(widget=forms.FileInput())

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    person_id = forms.IntegerField(widget=forms.HiddenInput)
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text == '':
            forms.ValidationError("نظر حداقل باید 2 کاراکتر باشد")
        return text