from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Book, Cart
from .serializers import BookSerializer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        Book.objects.create(title=title, author=author, price=price)
        return redirect('book_list')
    return render(request, 'add_book.html')

@api_view(['GET'])
def api_book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    cart, created = Cart.objects.get_or_create(pk=1)
    cart.books.add(book)
    return redirect('book_list')

