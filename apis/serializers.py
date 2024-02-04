from rest_framework import serializers
from books.models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")