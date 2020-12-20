from django.shortcuts import render

def accounts(request):
    context={}
    return render(request, '../templates/accounts.html', context)
