from .models import Budget
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import HttpResponse
def serialize_model(data):
    return serializers.serialize('json', data)
def all_budgets(request):
    budgets = Budget.objects.filter(owner=request.user)
    data = serializers.serialize('json',budgets)
    return HttpResponse(data)
def get_budget(id):
    budget = Budget.objects.get(pk=id)
