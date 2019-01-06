from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from datetime import date
import re
from IPython import embed

""" Manager Classes """
class CupManager(models.Manager):
    def batch_create(self, carrier, size):
        for i in range(size):
            cup = self.create(carrier_type='b', carrier=carrier)
            cup.save()
        return 

class Cup(models.Model):
    # TODO: RFID 
    objects = CupManager()

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('c', 'Cleaning'),
        ('a', 'Available'),
        ('n', 'Not in circulation')
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='a',
        help_text='Cup availability',
    )
    CARRIER_TYPES = (
        ('b', 'Business'),
        ('u', 'User'),
        ('a', 'Administration'),
        ('m', 'Machine')
    )
    carrier_type = models.CharField(max_length=1, choices = CARRIER_TYPES, default='a')
    carrier = models.ForeignKey('CupUser', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class CupUser(AbstractUser):
    username = models.CharField(
        error_messages={'unique': '有人使用這個名字了'}, 
        help_text='', 
        max_length=150, 
        unique=True, 
        validators=[UnicodeUsernameValidator()], 
        verbose_name='用戶名'
    )
    password    = models.CharField(max_length=128, verbose_name='密碼')
    last_name   = models.CharField(blank=True, max_length=150, verbose_name='姓氏')
    first_name  = models.CharField(blank=True, max_length=30, verbose_name='名字')
    email       =  models.EmailField(blank=True, max_length=254, verbose_name='email')
    title       = models.CharField(blank=True, null=True, max_length=300, verbose_name='公司稱號')
    address     = models.CharField(blank=True, null=True, max_length=300, verbose_name='地址')
    phone_number= models.CharField(blank=True, null=True, max_length=10, help_text='e.g. 0912345678', verbose_name='電話號碼')
    

    # staff(built-in), customer, business
    is_customer = models.BooleanField(default=False, verbose_name='customer status')
    is_business = models.BooleanField(default=False, verbose_name='business status')

    # 回傳用戶的名字
    # 如果使用者有姓有名，代表是顧客，回傳使用者姓名。
    # 如果使用者有稱號，代表是公司，回傳公司名號。
    # 如果都沒有提供，或是不完整，則回傳用戶名。
    @property
    def name(self):
        if self.first_name and self.last_name:
            english = r'(^[A-Za-z]+$)'
            if re.match(english, self.first_name+self.last_name):
                return ("%s %s" % (self.first_name, self.last_name))
            else:
                return self.last_name+self.first_name
        elif self.title:
            return self.title
        else:
            return self.username

    def __str__(self):
        return self.name


class Record(models.Model):
    cup = models.ForeignKey('Cup', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey('CupUser', related_name='user', on_delete=models.SET_NULL, blank=True, null=True) 
    source = models.ForeignKey('CupUser', related_name='source', on_delete=models.SET_NULL, blank=True, null=True) 
    destination = models.ForeignKey('CupUser', related_name='destination', on_delete=models.SET_NULL, blank=True, null=True)
    returned_at = models.DateTimeField(auto_now=True)        # record 被更新的時間就是杯子被還回來的時間
    loaned_out_at = models.DateTimeField(auto_now_add=True)  # 杯子被租出去的時間就是 record 建立的時間
    
    def __str__(self):
        if self.source and self.user:
            return ("from %s to %s" % (self.source.name, self.user.name))
        else:
            return self.id

    @property
    def duration(self):
        """ returns the duration of this renting period """
        if self.loaned_out_at and self.returned_at:
            return (self.returned_at - self.loaned_out_at).days
        return None

    class meta:
        ordering = ['-loaned_out_at']




