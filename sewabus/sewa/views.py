from django.shortcuts import render, redirect
from . import models
from pengguna.models import DataBus, Images
# from .forms import PesanForm
from .models import Sewa
from pengguna.views import tabel 
from sewa.form import PesanForm

def index(req):
    # task = models.Pasien.objects.all()
    # return render(req, 'sewa/index.html')
    tampil = DataBus.objects.all()   
    return render(req,'sewa/index.html',{'tampil':tampil}) 

    
def detail(req, id):
    tampil = DataBus.objects.filter(pk=id)
    image = Images.objects.all()
    data = {
        'data':tampil,
        'image' : image,
    }   
    return render(req,'sewa/detail.html',data) 

# def pesan(req):
#     form = PesanForm(req.POST or None, req.FILES or None)
#     if req.method == 'POST':
#         if form.is_valid():
#             form.save()
#         return redirect('index')
#     return render(req, 'sewa/pesan.html',{
#         'form': form,
#     })

def tambah(req):
    if req.POST:
        models.Sewa.objects.create(
        nama_pemesan=req.POST['nama_pemesan'],
        no_ktp=req.POST['no_ktp'],
        no_hp=req.POST['no_hp'],
        email=req.POST['email'],
        tanggal_mulai=req.POST['tanggal_mulai'],
        tanggal_selesai=req.POST['tanggal_selesai'],
        tujuan=req.POST['tujuan'],
        waktu=req.POST['waktu'],
        sewa=req.POST['sewa'],
        titik_penjemputan=req.POST['titik_penjemputan'],
        
        
        )
        return redirect('tambah')
    task = models.Sewa.objects.all()
    return render(req, 'sewa/tambah.html',
    { 'data' : task,
    })

# def tambah(request):
#     if request.POST:
#         form = PesanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PesanForm()
#             pesan = 'Data Berhasil di Simpan'
#             konteks = {
#                 'form':form,
#                 'pesan':pesan
#             }
#             return render(request, 'sewa/pesan.html', konteks)
#     else:
#         form = PesanForm()
#         konteks = {
#             'form':form,
#         }
#         return render(request, 'sewa/tambah.html', konteks)

def pesan(req, id):
    task = models.Sewa.objects.filter(pk=id).first()
    return render(req, 'sewa/pesan.html',
    { 'data' : task,
    })