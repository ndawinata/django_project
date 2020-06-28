from django.shortcuts import render
import os
import pickle

def index(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'namasiswa.data')
    f = open(file_path, 'rb')
    nama_siswa = pickle.load(f)
    f.close()
    print(nama_siswa)
    context = {
        'judul': 'Halaman Home',
        'penulis': 'nanda winata',
        'banner': 'img/logo.jpg',
        'nav': [
            ['/', 'Home'],
            ['blog/', 'Blog'],
            ['blog/recent/', 'Recent']
        ],
        # 'nama': nama_siswa,
    }
    return render(request, 'index.html', context)


def dinda(request):
    return render(request, 'dinda/index.html')
