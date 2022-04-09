from django.db import models


# Create your models here.
class NFT(models.Model):
    tx_hash = models.CharField(max_length=200)
    unique_hash = models.CharField(max_length=20)
    media_url = models.CharField(max_length=200)
    owner =  models.CharField(max_length=200)