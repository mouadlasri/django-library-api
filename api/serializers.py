from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

        # database fields we want to expose
        fields = ('title', 'subtitle', 'author', 'isbn')