from django.db import models

# Create your models here.
MEMBER_CHOICES = (
    ('silver','SILVER'),
    ('gold', 'GOLD'),
    ('platinum','PLATINUM'),
)

class MemberData(models.Model):
    member = models.CharField(max_length=12, choices=MEMBER_CHOICES, default='silver')
    price = models.FloatField()