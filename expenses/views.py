from django.shortcuts import render, get_object_or_404, redirect
from .models import Expenses
from .forms import ExpenseForm

# Create your views here.

def expense_list(request):
    expenses = Expenses.objects.filter(user = request.user).order_by('category', '-date')
    total_expense = sum(expense.amount for expense in expenses)
    return render(request, 'expnese_list.html', {'expenses':expenses, 'total_expense': total_expense})

def expense_detail(request, pk):
    expense = get_object_or_404(Expenses, pk = pk, user= request.user)
    return render(request, 'expense_detail.html', {'expense': expense})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expenses, pk = pk , user = request.user)
    expense.delete()
    return redirect('expense_list')
