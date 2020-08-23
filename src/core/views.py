import boto3
import os

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializer import TaskSerializer
from core.s3_storage import Task

class TasksView(APIView):
    # 

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(Task(), data=request.data)
        if serializer.is_valid():
            serializer.save(serializer.validated_data)
        return Response()

    def get(self, request, *args, **kwargs):
        data = {
            'title': 'Task1',
            'content': 'test content' 
        }    

        # session = boto3.Session(profile_name='oort', region_name='ap-southeast-1')
        
        client = boto3.client('lambda')
        client.list_functions()
        return Response(os.getenv('AWS_ACCESS_KEY_ID'))
