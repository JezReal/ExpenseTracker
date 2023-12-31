from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST, require_GET

from expensetracker.models import ExpenseItem


# Create your views here.

class ExpenseItemForm(forms.Form):
    item_name = forms.CharField(required=True)
    item_price = forms.FloatField(required=True, min_value=1)


def index(request):
    return render(request, 'expensetracker/index.html')


def get_expenses(request):
    expenses = ExpenseItem.objects.all()
    expenses_html = []
    for expense in expenses:
        expenses_html.append(render_to_string('components/card.html', context={'expense_data': expense}))
    return HttpResponse("\n".join(expenses_html))


@require_POST
def add_expense(request):
    data = ExpenseItemForm(request.POST)
    if data.is_valid():
        expense_item = ExpenseItem()
        expense_item.item_name = data.cleaned_data['item_name']
        expense_item.item_price = data.cleaned_data['item_price']
        expense_item.save()

        context = {
            'expense_data': expense_item
        }
        return render(request, 'components/card.html', context=context)
    else:
        return render(request, data)


@require_GET
def expenses_chart(request):
    return render(request, 'expensetracker/chart.html')


@require_GET
def about(request):
    return render(request, 'expensetracker/about.html')
