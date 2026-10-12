from rest_framework.pagination import PageNumberPagination



class ContactPagination(PageNumberPagination):
    page_size = 3

