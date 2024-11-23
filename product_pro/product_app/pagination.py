from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    ''' on every page 100 objects retrive '''
    page_size = 100
    