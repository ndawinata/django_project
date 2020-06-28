from django.shortcuts import render
import os
import pickle

def index(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'model.pkl')
    f = open(file_path, 'rb')
    model = pickle.load(f)
    f.close()
    print(model.predict([[6,148,72,35,0,33.6,0.627,50]]))
    
    

    context = {
        'judul': 'Halaman Home',
        'penulis': 'nanda winata',
        'banner': 'img/logo.jpg',
        'nav': [
            ['/', 'Home'],
            ['blog/', 'Blog'],
            ['blog/recent/', 'Recent']
        ],
    }
    # print(request.method)
    if request.method == 'POST':
        preg = request.POST['pregnancies']
        gluc= request.POST['glucose']
        blood = request.POST['bloodPressure']
        skin = request.POST['skin']
        insul = request.POST['insulin']
        bmi = request.POST['bmi']
        diab = request.POST['diabetesPedigreeFunction']
        age = request.POST['age']
        context['hasil'] = model.predict([[preg,gluc,blood,skin,insul,bmi,diab,age]])

    return render(request, 'index.html', context)


def dinda(request):
    return render(request, 'dinda/index.html')
