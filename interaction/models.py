from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Cup(models.Model):

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('d', 'Discarded'),
        ('r', 'Returned, to be cleaned')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='r',
        help_text='Cup availability',
    )
    
    OWNER_TYPE = (
        ('b', 'Business'),
        ('u', 'User'),
        ('a', 'Administration')
    )

    business = models.ForeignKey(
                    'Business',
                    models.SET_NULL,
                    blank=True,
                    null=True,
                )

    user = models.ForeignKey(
                'User',
                models.SET_NULL,
                blank=True,
                null=True,
            )

    # A cup is either in an user's or a business' hand
    owner_type = models.CharField(
        max_length=1,
        choices=OWNER_TYPE,
    )

    def get_owner(self, owner_type, pk):
        switcher = {
            'b': Business.filter(id=pk),
            'u': User.filter(id=pk)
        }
        return switcher.get(owner_type, None)

    def __str__(self):
        return self.id
        

class Owner(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a business\' brand name or a user\'s name.')
    email = models.EmailField()
    phone = models.CharField(max_length=10, help_text='e.g. 0912345678')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this owner."""
        return reverse('owner-detail', args=[str(self.id)])

    class Meta:
        abstract = True


class Business(Owner):

    address = models.CharField(max_length=300)

    def count_cups(self):
        """Returns the respective number of available/returned cups currently at this place."""
        cups = {
            'a': self.cup.filter(status__exact='a').count(),
            'r': self.cup.filter(status__exact='r').count(),
        }
        return cups

class User(Owner):
    pass

