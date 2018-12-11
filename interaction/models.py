from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

""" Manager Classes """
class CupManager(models.Manager):
    def get_queryset(self):
        return super(CupManager, self).get_queryset().exclude(status='n')

class CupInBusinessManager(models.Manager):
    def get_queryset(self):
        return super(CupInBusinessManager, self).get_queryset().exclude(owner_type='b')   

class CupInUserManager(models.Manager):
    def get_queryset(self):
        return super(CupInUserManager, self).get_queryset().exclude(owner_type='u')  

class CupInMachineManager(models.Manager):
    def get_queryset(self):
        return super(CupInMachineManager, self).get_queryset().exclude(owner_type='m')   

class CupInAdminManager(models.Manager):
    def get_queryset(self):
        return super(CupInAdminManager, self).get_queryset().exclude(owner_type='a')   


class Cup(models.Model):
    # TODO: RFID 
    objects = models.Manager()
    in_circulation = CupManager()
    in_business = CupInBusinessManager()
    in_user = CupInUserManager()
    in_machine = CupInMachineManager()
    in_admin = CupInAdminManager()

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('c', 'Cleaning'),
        ('a', 'Available'),
        ('n', 'Not in circulation'),
        ('r', 'Returned, to be cleaned')
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='r',
        help_text='Cup availability',
    )
    OWNER_TYPES = (
        ('b', 'Business'),
        ('u', 'User'),
        ('a', 'Administration'),
        ('m', 'Machine')
    )
    owner_type = models.CharField(max_length=1, choices = OWNER_TYPES, default='a')
    owner_id = models.IntegerField(null = True, blank = True)

    def owner(self):
        if self.owner_type == 'b':
            return Business.objects.get(pk = self.owner_id)
        elif self.owner_type == 'u':
            return User.objects.get(pk= self.owner_id)
        elif self.owner_type == 'm':
            return Machine.objects.get(pk = self.owner_id)
        return None

    def __str__(self):
        return str(self.pk)
    
class Owner(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a business\' brand name or a user\'s name.')
    email = models.EmailField()
    phone = models.CharField(max_length=10, help_text='e.g. 0912345678')
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this owner."""
        return reverse('owner-detail', args=[str(self.id)])
    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Business(Owner):
    # objects = BusinessManager()
    address = models.CharField(max_length=300)

    def cups(self):
        return Cup.objects.filter(owner_type = 'b', owner_id = self.id)

class User(Owner):
    # objects = UserManager()
    def cups(self):
        return Cup.objects.filter(owner_type = 'u', owner_id = self.id)

class Machine(models.Model):
    # objects = MachineManager()
    location = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    
    def cups(self):
        return Cup.objects.filter(owner_type = 'm', owner_id = self.id)

