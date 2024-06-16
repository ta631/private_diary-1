from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    
