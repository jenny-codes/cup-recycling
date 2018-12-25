from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CupUser, Cup, Group
from IPython import embed

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
        
    @transaction.atomic
    def save(self, commit=True):
        print('forms/save')
        user = super().save(commit=False)
        user.is_customer = True
        group = Group.objects.get(name='Customers')
        if commit:
            user.save()
            group.user_set.add(user)
        return user

class BusinessSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('title','username', 'email', 'phone_number', 'address')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_business = True
        group = Group.objects.get(name='Business')       
        if commit:
            user.save()
            group.user_set.add(user)
        return user

class BusinessRequestCupsForm(forms.Form):
    cups_needed = forms.IntegerField(label='需要杯子的數量')

class BusinessReceiveCupsForm(forms.Form):
    cup_received = forms.IntegerField(label='收到杯子的 ID')

# FIX
class CupUserChangeForm(UserChangeForm):

    class Meta:
        model = CupUser
        fields = ('username', 'email')

    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
