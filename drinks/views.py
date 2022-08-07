from django.shortcuts import render
from .models import Drink
from .serializers import DrinkSerializer
from django.http import JsonResponse

# Create your views here.

def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({ 'drinks': serializer.data })

