# Create your models here.
# app/models.py
from django.db import models
import uuid

class Voter(models.Model):
    firstname = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    dob = models.DateField(verbose_name='Date of birth')
    email = models.EmailField()
    GENDER_CHOICES = [('M','Male'),('F','Female'),('O','Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=30)
    MARITAL = [('S','Single'),('M','Married'),('D','Divorced'),('W','Widowed')]
    marital_status = models.CharField(max_length=1, choices=MARITAL)
    rc_number = models.CharField(max_length=50, unique=True, verbose_name='RC Number', null=True, blank=True)
    unique_voter_number = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    mine_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate unique voter number if not already set
        if not self.unique_voter_number:
            import random
            while True:
                num = str(random.randint(100000000000, 999999999999))
                if not Voter.objects.filter(unique_voter_number=num).exists():
                    self.unique_voter_number = num
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firstname} {self.surname}"


class Farmer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    votes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.firstname} voted for {self.farmer.name}"