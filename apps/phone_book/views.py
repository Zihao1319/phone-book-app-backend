from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.phone_book.serializers import ContactSerializer

from apps.phone_book.services.phone_book_service import PhoneBookService

# Create your views here.
class ContactListView(APIView):
    authentication_classes = []

    def get (self, request, *args, **kwargs):
        try:
            results = PhoneBookService().get_all_contacts(request)
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CreateContactView(APIView):
    authentication_classes = []
    serializer_class= ContactSerializer

    def post (self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                results = PhoneBookService().create_contact(request)
                return Response(results, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateContactView(APIView):
    authentication_classes = []
    serializer_class= ContactSerializer

    def post (self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                results = PhoneBookService().update_contact(request)
                return Response(results, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteContactView(APIView):
    authentication_classes = []
    serializer_class= ContactSerializer

    def post (self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                results = PhoneBookService().delete_contact(request)
                return Response(results, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchContactView(APIView):
    authentication_classes = []
    serializer_class= ContactSerializer

    def get (self, request, *args, **kwargs):
        try:
            results = PhoneBookService().search_contact(request)
            return Response(results, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

