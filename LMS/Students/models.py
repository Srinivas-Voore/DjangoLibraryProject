from django.db import models
from django.utils import timezone

DEPT_CHOICES = [
    ('CSE', 'CSE'),
    ('BT', 'BT'),
    ('CE', 'CE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('Mech.', 'Mech.')
]

CATEGORY_CHOICES = [
    ('Book', 'Book'),
    ('Journal', 'Journal'),
    ('Article', 'Article')
]
# Create your models here.

class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=55)
    short_name = models.CharField(max_length=55)
    bquantity = models.IntegerField()
    department = models.CharField(choices=DEPT_CHOICES, max_length=15)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    date_access = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.bname)

class Journal(models.Model):
    jid = models.AutoField(primary_key=True)
    jname = models.CharField(max_length=55)
    jyear=models.IntegerField(max_length=5)

    def __str__(self):
        return '%s' % (self.jname)
