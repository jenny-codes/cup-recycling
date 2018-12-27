from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import AbstractUser, Group
from datetime import date
import re

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
    phone_number = models.CharField(blank=True, null=True, max_length=10, help_text='e.g. 0912345678')
    address = models.CharField(blank=True, null=True, max_length=300)
    title = models.CharField(blank=True, null=True, max_length=300)

    # staff(built-in), customer, business
    is_customer = models.BooleanField(default=False, verbose_name='customer status')
    is_business = models.BooleanField(default=False, verbose_name='business status')

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




