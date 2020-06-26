from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    context={
        'judul':'Halaman Home',
        'penulis':'nanda winata',
        'nav':[
            ['/','Home'],
            ['about/','About'],
            ['blog/','Blog'],
            ['blog/recent/','Recent']
        ]
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('ini about')