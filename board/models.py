from django.db import models
from member.models import CustomUser

# Create your models here.
class Board(models.Model):
    # IS_OB_CHOICES = [
    #     ("X", "X"),
    #     ("O", "O"),
    # ]
    
    # SEOUL_CHOICES = [
    #     ('종로구', '종로구'), 
    #     ('중구', '중구'), 
    #     ('용산구', '용산구'), 
    #     ('성동구', '성동구'), 
    #     ('광진구', '광진구'), 
    #     ('동대문구', '동대문구'), 
    #     ('중랑구', '중랑구'),
    #     ('성북구', '성북구'), 
    #     ('강북구', '강북구'), 
    #     ('도봉구', '도봉구'), 
    #     ('노원구', '노원구'), 
    #     ('은평구', '은평구'), 
    #     ('서대문구', '서대문구'), 
    #     ('마포구', '마포구'), 
    #     ('양천구', '양천구'), 
    #     ('강서구', '강서구'), 
    #     ('구로구', '구로구'), 
    #     ('금천구', '금천구'), 
    #     ('영등포구', '영등포구'), 
    #     ('동작구', '동작구'), 
    #     ('관악구', '관악구'), 
    #     ('서초구', '서초구'), 
    #     ('강남구', '강남구'), 
    #     ('송파구', '송파구'), 
    #     ('강동구', '강동구')
    # ]
#, choices=SEOUL_CHOICES
#, choices=IS_OB_CHOICES

    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    ob = models.CharField(max_length=100) #산과여부
    textbox = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
