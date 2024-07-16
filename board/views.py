from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Board
from rest_framework.response import Response
from .serializers import BoardListSerializer, BoardDetailSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly

@api_view(['GET','POST']) 
#@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticatedOrReadOnly])
def board_list(request):
    if request.method =='GET':
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BoardDetailSerializer(data=request.data)
        if serializer.is_valid():
            board = serializer.save(user = request.user)
            result = BoardDetailSerializer(board)
            return Response(result.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)   
'''
한 블로그 조회
'''
@api_view(['GET','PUT','DELETE'])
#@authentication_classes([JWTAuthentication])
#@permission_classes([IsOwnerOrReadOnly])
def board_detail(request, pk):
    try: 
        board = Board.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = BoardDetailSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method =='PUT':
            serializer = BoardDetailSerializer(board, data=request.data)
            if serializer.is_valid():
                board = serializer.save(user = request.user)
                result = BoardDetailSerializer(board)
                return Response(result.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.method =='DELETE':
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Board.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def board_region(request, region):
        boards = Board.objects.filter(region=region)
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
