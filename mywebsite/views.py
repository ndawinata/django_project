from django.shortcuts import render

# method view

def index(request):
    context = {
        'judul': 'Halaman Home',
        'penulis': 'nanda winata',
        'nav': [
            ['/', 'Home'],
            ['blog/', 'Blog'],
            ['blog/recent/', 'Recent']
        ]
    }
    return render(request, 'index.html', context)

def dinda(request):
    return render(request, 'dinda/index.html')