from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Bank

def bank_list (request):
    banks = Bank.objects.all()
    context = {
        'banks': banks
    }
    return render(request, template_name='bank/bank_list.html', context=context)
