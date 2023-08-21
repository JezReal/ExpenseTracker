from django import forms
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from expensetracker.models import ExpenseItem


# Create your views here.

class ExpenseItemForm(forms.Form):
    item_name = forms.CharField(required=True)
    item_price = forms.FloatField(required=True, min_value=1)


def index(request):
    if request.method == 'GET':
        expenses = ExpenseItem.objects.all()
        context = {
            'expenses': expenses
        }

        return render(request, 'expensetracker/index.html', context=context)
    return render(request, 'expensetracker/index.html')


def get_expenses(request):
    expenses = ExpenseItem.objects.all()

    return HttpResponse()


@require_POST
def add_expense(request):
    data = ExpenseItemForm(request.POST)

    if data.is_valid():
        expense_item = ExpenseItem()
        expense_item.item_name = data.item_name
        expense_item.item_price = data.item_price
        expense_item.save()

        return HttpResponse('<p>A new item bruh</p>')

    return HttpResponseBadRequest()


def somewhere(request):
    return render(request, 'expensetracker/somewhere.html')


def about(request):
    return render(request, 'expensetracker/about.html')
