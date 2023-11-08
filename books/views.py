from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from django.core.paginator import Paginator, Page, EmptyPage
from rest_framework import generics
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer
# Create your views here.

# class BookViewSet(viewsets.ModelViewSet):
#     serializer_class = BookSerializer
#
#     def list(self, request, *args, **kwargs):
#         page_size = request.query_params.get('page_size', 5)  # You can set a default value if needed
#         page = request.query_params.get('page', 1)
#
#         try:
#             page_size = int(page_size)
#             page = int(page)
#         except ValueError:
#             return Response({'detail': 'Invalid page_size or page parameter.'}, status=status.HTTP_400_BAD_REQUEST)
#
#         queryset = Book.objects.all()
#         paginator = Paginator(queryset, page_size)
#
#         try:
#             page_data = paginator.page(page)
#         except EmptyPage:
#             return Response({'detail': 'Page not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = BookSerializer(page_data, many=True)
#
#         return Response({
#             'results': serializer.data,
#             'count': paginator.count,
#             'next_page': page_data.next_page_number() if page_data.has_next() else None,
#             'previous_page': page_data.previous_page_number() if page_data.has_previous() else None
#         })

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']  # Add other fields you want to search by here

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset


# class FavoriteViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.filter(category='fantasy')
#     serializer_class = BookSerializer
#
#
# class HistoryViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.filter(category='history')
#     serializer_class = BookSerializer
