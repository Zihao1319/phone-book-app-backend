
from rest_framework import serializers
from apps.phone_book.models import Contact

class PhoneBookListSerializer(serializers.ModelSerializer):
    pass

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

