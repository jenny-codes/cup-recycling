from interaction.forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

class CustomerSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number')
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save()
        user.is_customer = True
        group = Group.objects.get(name='Customers')
        if commit:
            user.save()
            group.user_set.add(user)
        return user

class BusinessSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('title', 'username', 'password1', 'password2', 'email', 'phone_number', 'address')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save()
        user.is_business = True
        group = Group.objects.get(name='Business')       
        if commit:
            user.save()
            group.user_set.add(user)
        return user

class CupUserChangeForm(UserChangeForm):
    class Meta:
        model = CupUser
        fields = ('username', 'email')