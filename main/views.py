from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Aplikasi Pengelola Donasi',
        'name': 'Ratu Nadya A.',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)