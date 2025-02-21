from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _iter_(self):
        yield {"length": self.length}
        yield {"width": self.width}

def rectangle_view(request):
    rect = Rectangle(10, 5)
    return JsonResponse(list(rect), safe=False)