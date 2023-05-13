from django.db import models

class User(models.Model):
    
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', max_length=100)
    phone = models.IntegerField('電話番号', blank=True, null=True)

    # def __str__(self):
    #     return self.name