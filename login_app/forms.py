from django import forms
from .models import Posts, CustomUser, Thread
from django.contrib.auth.forms import UserCreationForm

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('thread_id', 'nickname', 'text')
        labels = {
            'thread_id': 'id',
            'nickname': '名前',
            'text': '本文',
        }
        widgets = {'text':forms.Textarea(attrs={'placeholder':'本文(300字以内)'}),'nickname':forms.TextInput(attrs={'placeholder':'名前(省略不可)'})}

class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('author','title')
        labels = {
            'author': '作成者',
            'title': 'スレッド名',
        }
        widgets = {'title':forms.TextInput(attrs={'placeholder':'30字以内'})}

class UesrCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['nickname'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'password1', 'password2')