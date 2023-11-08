from rest_framework import serializers
from .models import Book


# class BookSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(max_length=None, use_url=True)
#
#     class Meta:
#         model = Book
#         fields = ['id', 'name', 'image', 'rating', 'description', 'category']

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'image', 'rating', 'description', 'category']

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)
        if 'request' in self.context and hasattr(self.context['request'], 'query_params'):
            page = self.context['request'].query_params.get('page')
            if page:
                try:
                    page = int(page)
                    data['next_page'] = page + 1 if instance.has_next() else None
                    data['previous_page'] = page - 1 if instance.has_previous() else None
                except ValueError:
                    pass

        return data
