from django.urls import path
from apps.phone_book.views import *

urlpatterns = [
    path('list', ContactListView.as_view(), name="contact-list"),
    path('search', SearchContactView.as_view(), name='search-contact'),
    path('create', CreateContactView.as_view(), name='create-contact'),
    path('update', UpdateContactView.as_view(), name='update-contact'),
    path('delete', DeleteContactView.as_view(), name='delete-contact'),
]