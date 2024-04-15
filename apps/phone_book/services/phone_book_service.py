
from posixpath import split
from apps.phone_book.models import Contact
from apps.phone_book.serializers import ContactSerializer
from phone_book_app.utils.http_utils import getPayload
from django.db.models import Q

class PhoneBookService():

    def create_contact(self, request):
        payload = getPayload(request)
        new_contact =  Contact.objects.create(
            name=payload["name"],
            phone=payload["phone"],
            address=payload["address"]
        )
        return ContactSerializer(new_contact).data

    def get_all_contacts(self, request):
        try:
            contacts= Contact.objects.all()
            return ContactSerializer(contacts, many=True).data

        except Contact.DoesNotExist:
            return Contact.objects.none

    def update_contact(self, request):
        payload = getPayload(request)
        id = payload["id"]

        try:
            contact_instance = Contact.objects.filter(id=id)
            contact_instance.name = payload["name"]
            contact_instance.phone =payload["phone"]
            contact_instance.address = payload["address"]
            contact_instance.save()

        except Contact.DoesNotExist as e:
            raise e

    def delete_contact(self, request):
        payload = getPayload(request)
        id = payload["id"]

        try:
            contact = Contact.objects.get(id=id)
            contact.delete()
            return ContactSerializer(contact).data

        except Contact.DoesNotExist as e:
            raise e


    def search_contact(self, request):
        search_prompt = request.query_params.get('q')
        split_prompt = search_prompt.split('+')

        contacts = []
        if len(split_prompt) == 1 and split_prompt[0] == "":
            contacts = Contact.objects.order_by('created_by')[:10]

        else:
            search = Q()
            for prompt in split_prompt:
                search |= Q(name__icontains=prompt)
                search |= Q(phone__icontains=prompt)
                search |= Q(address__icontains=prompt)
            contacts = Contact.objects.filter(search)

        return ContactSerializer(contacts, many=True).data
