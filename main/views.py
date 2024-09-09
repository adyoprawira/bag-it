from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'BagIt',
        'name' : 'Adyo Arkan Prawira',
        'class' : 'KKI'
    }
