from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20, null=True)


class Thread(models.Model):
    class Meta():
        db_table = 'thread'

    author = models.CharField(verbose_name='作成者', max_length=30, null=True)
    title = models.CharField(verbose_name='スレッド名', max_length=30)
    created_at = models.DateField(verbose_name='作成日', default=timezone.now)
    def __str__(self):
        return '(' + str(self.id) + ') ' + str(self.title) + " | " + str(self.created_at)


class Posts(models.Model):    
    class Meta():
        db_table = 'posts'

    thread_id = models.ForeignKey('Thread', on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(verbose_name='名前', max_length=15, null=True, default="名無しさん")
    text = models.CharField(verbose_name='本文', max_length=300)
    posted_at = models.DateTimeField(verbose_name='投稿日', default=timezone.now)
    response_id = models.PositiveIntegerField(null=True, blank=True,)
    def __str__(self):
        return str(self.thread_id) + ". " + str(self.text)+ " 返信id="+str(self.response_id) + " ID="+ str(self.id)

