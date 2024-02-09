from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import FormParser, MultiPartParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from uuid import uuid4

class GetBookSerializer(serializers.Serializer):
    bookid = serializers.CharField(required=True)

class UpdateBookSerialzer(serializers.Serializer):
    bookid = serializers.CharField(required=True)
    title = serializers.CharField(required=False, allow_blank=False)
    author = serializers.CharField(required=False, allow_blank=False)
    description = serializers.CharField(required=False, allow_blank=True)
    cover = serializers.ImageField(required=False)

class AnalyzeBookSerializer(serializers.Serializer):
    bookid = serializers.CharField(required=True)

class OverwriteBookSerializer(serializers.Serializer):
    bookid = serializers.CharField(required=True)
    file = serializers.FileField(required=True)

class DeleteBookSerializer(serializers.Serializer):
    bookid = serializers.CharField(required=True)

class BooksBookidView(APIView):
    parser_classes = (FormParser, MultiPartParser)

    serializer_class = UpdateBookSerialzer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetBookSerializer
        elif self.request.method == 'PATCH':
            return UpdateBookSerialzer
        elif self.request.method == 'PUT':
            return AnalyzeBookSerializer
        elif self.request.method == 'DELETE':
            return DeleteBookSerializer
        return super().get_serializer_class()

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data={"bookid": kwargs.get('bookid')})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        # TODO: IMPLEMENT LOGIC

        return Response(validated_data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        data = request.data
        data['bookid'] = kwargs.get('bookid')
        serializer = serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        # TODO: IMPLEMENT LOGIC

        return Response(validated_data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data={"bookid": kwargs.get('bookid')})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        # TODO: IMPLEMENT LOGIC

        return Response(validated_data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        data = request.data
        data['bookid'] = kwargs.get('bookid')
        serializer = serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        # TODO: IMPLEMENT LOGIC

        return Response(validated_data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data={"bookid": kwargs.get('bookid')})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        # TODO: IMPLEMENT LOGIC

        return Response(validated_data, status=status.HTTP_200_OK)