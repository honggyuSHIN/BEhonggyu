from rest_framework import serializers
from .models import Board

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'user', 'region', 'ob','textbox']