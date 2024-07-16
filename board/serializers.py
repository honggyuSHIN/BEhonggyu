from rest_framework import serializers
from .models import Board

class BoardListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = ['id', 'user', 'region', 'hospital_name','textbox']
    def get_user(self, obj):
        return obj.user.nickname

class BoardDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = ['id','user','hospital_name','region','ob','textbox']
    def get_user(self, obj):
        return obj.user.nickname
