import pickle
file_data = 'namasiswa.data'
nama_siswa = ['nanda','winata','risma']
f = open(file_data, 'wb')
pickle.dump(nama_siswa, f)
f.close()