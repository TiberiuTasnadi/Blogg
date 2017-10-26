from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ContactForm(forms.Form):
    nameSurnames = forms.CharField(
        label='Name and surnames',
        error_messages={'required': 'Please enter your name'},
        widget=forms.TextInput(
            attrs={
                'class':'form-control col-sm-12'},
        )
    )
    email = forms.EmailField(
        error_messages={
            'required':'Please enter your email.',
            'invalid':'The email is invalid.'},
        widget=forms.EmailInput(
            attrs={
                'placeholder':'example@email.com',
                'class':'form-control col-sm-12'},
        )
    )
    problem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'class':'form-control col-sm-12'},
        )
    )
