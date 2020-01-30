from tkinter import *
import tkinter as tk 
from tkinter import messagebox

def kirim():
	messagebox.showinfo('submit','sukses !')
def keluar():
	messagebox.askquestion('quit','Anda yakin ingin keluar?')
	window.destroy()

window = tk.Tk()
#memberikan judul pada Halaman aplikasi desktop
window.title('daftar Mahasiswa')

#kolom -1
label = tk.Label(window,text = 'Nama:')
label.grid(row = 0,column = 1)
label2 = tk.Label(window,text = 'Tempat:')
label2.grid(row = 1,column =1)
label3 = tk.Label(window,text ='tanggal:')
label3.grid(row = 2,column =1)
label4 = tk.Label(window,text ='Bulan ')
label4.grid(row = 3,column =1)
label5 = tk.Label(window,text = 'Tahun')
label5.grid(row = 4,column =1)
label6 = tk.Label(window,text = 'Pekerjaan:')
label6.grid(row =5,column =1)

#kolom ke 2
isian1 = tk.Entry(window,bg ='green',fg ='white',justify ='left',width =19)
isian1.grid(row = 0,column =2)
isian2 = tk.Entry(window,bg ='green',fg ='white',justify ='left',width =19)
isian2.grid(row =1,column =2)
isian3 = tk.Spinbox(window,from_ = 1,to =12 ,bg ='green',fg ='white',justify ='right',width =18)
isian3.grid(row =3,column =2)

#spinbox berisi kotak tanda panah kecil untuk memilih atas atau bawah
spinbox1 = tk.Spinbox(window,from_=1,to=31,justify ='right',bg ='green',fg ='white',width =18)
spinbox1.grid(row =2,column =2)
spinbox2 = tk.Spinbox(window, from_ =1991,to=2020,justify ='right',bg ='green',fg ='white',width =18)
spinbox2.grid(row =4,column =2)

isian4 = tk.Entry(window,bg ='green',fg ='white',justify ='left',width =19)
isian4.grid(row =5 ,column =2)

#tombol
tombol = tk.Button(window,text = 'submit',bg ='navy',fg ='white',command = kirim)
tombol.grid(row = 7,column =1)
tombol2 = tk.Button(window,text = 'quit',bg ='red',fg ='white',command = keluar)
tombol2.grid(row =7,column = 2)


window.mainloop()