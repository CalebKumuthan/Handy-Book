from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'message': "User created successfully", 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'message': e.details, 'data': serializer.data})



