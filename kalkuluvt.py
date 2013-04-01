#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# 
# kalkuluvt.py
#
# Copyright 2013 Universitas Virtual Terbuka
#
# Referensi program:
# 1. http://code.google.com/p/calculator-using-pygtk
# 2. http://code.google.com/p/calculator-python-glade
# 3. http://zetcode.com/gui/pygtk/layout
# 
# Program ini buat pembelajaran di Universitas Virtual Terbuka

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk, sys
except:
    print("GTK Not Available")
    sys.exit(1)

license = """Kalkulator UVT is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License(GPL v3) as published by
the Free Software Foundation.

Kalkulator UVT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Kalkulator UVT; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA."""

authors = ["Raviyanto Ahmad", "Rajeswari Seetharaman", "Jan Bodnar"]

class Kalkulator:
    def __init__(self):
        self.jendela = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.jendela.set_size_request(350, 450)
        self.jendela.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#8A0886"))
        self.jendela.set_resizable(True)
        self.jendela.set_position(gtk.WIN_POS_CENTER)
        self.jendela.set_border_width(20)
        self.jendela.set_title("Kalkulator UVT")
        
        try:
            self.jendela.set_icon_from_file("/usr/share/kalkuluvt/gambar/kalkulator.png")
        except Exception, e:
            print e.message
                        
        self.gambar()
        self.tombol()
        self.menu()
        #self.fiks()
        self.tabel()
        self.masukan()
        self.kotak()
        self.konek()
        self.jendela.show_all()

    def gambar(self):
        self.sama_dengan = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/sama_dengan.png")
        self.gambar_sama_dengan = gtk.Image()
        self.gambar_sama_dengan.set_from_pixbuf(self.sama_dengan)

        self.nool = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/nool.png")
        self.gambar_nool = gtk.Image()
        self.gambar_nool.set_from_pixbuf(self.nool)

        self.kosong = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/kosong.png")
        self.gambar_kosong = gtk.Image()
        self.gambar_kosong.set_from_pixbuf(self.kosong)

        self.silang = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/silang.png")
        self.gambar_silang = gtk.Image()
        self.gambar_silang.set_from_pixbuf(self.silang)

        self.bagi = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/bagi.png")
        self.gambar_bagi = gtk.Image()
        self.gambar_bagi.set_from_pixbuf(self.bagi)

        self.tambah = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/tambah.png")
        self.gambar_tambah = gtk.Image()
        self.gambar_tambah.set_from_pixbuf(self.tambah)

        self.kurang = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/kurang.png")
        self.gambar_kurang = gtk.Image()
        self.gambar_kurang.set_from_pixbuf(self.kurang)

        self.persen = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/persen.png")
        self.gambar_persen = gtk.Image()
        self.gambar_persen.set_from_pixbuf(self.persen)

        self.tutup = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/tutup.png")
        self.gambar_tutup = gtk.Image()
        self.gambar_tutup.set_from_pixbuf(self.tutup)

        self.satu = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/satu.png")
        self.gambar_satu = gtk.Image()
        self.gambar_satu.set_from_pixbuf(self.satu)

        self.dua = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/dua.png")
        self.gambar_dua = gtk.Image()
        self.gambar_dua.set_from_pixbuf(self.dua)

        self.tiga = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/tiga.png")
        self.gambar_tiga = gtk.Image()
        self.gambar_tiga.set_from_pixbuf(self.tiga)

        self.empat = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/empat.png")
        self.gambar_empat = gtk.Image()
        self.gambar_empat.set_from_pixbuf(self.empat)

        self.lima = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/lima.png")
        self.gambar_lima = gtk.Image()
        self.gambar_lima.set_from_pixbuf(self.lima)

        self.enam = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/enam.png")
        self.gambar_enam = gtk.Image()
        self.gambar_enam.set_from_pixbuf(self.enam)

        self.tujuh = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/tujuh.png")
        self.gambar_tujuh = gtk.Image()
        self.gambar_tujuh.set_from_pixbuf(self.tujuh)

        self.delapan = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/delapan.png")
        self.gambar_delapan = gtk.Image()
        self.gambar_delapan.set_from_pixbuf(self.delapan)

        self.sembilan = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/sembilan.png")
        self.gambar_sembilan = gtk.Image()
        self.gambar_sembilan.set_from_pixbuf(self.sembilan)

        self.nol = gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/nol.png")
        self.gambar_nol = gtk.Image()
        self.gambar_nol.set_from_pixbuf(self.nol)

        
    def tombol(self):
        #self.tombol_ihwal = gtk.Button("Ihwal")
        #self.tombol_ihwal.set_size_request(80, 30)
        
        self.tombol_kosong = gtk.Button()
        self.tombol_kosong.add(self.gambar_kosong)
                

        self.tombol_persen = gtk.Button()
        self.tombol_persen.add(self.gambar_persen)
       
        self.tombol_nool = gtk.Button()
        self.tombol_nool.add(self.gambar_nool)
       
        self.tombol_tutup = gtk.Button()
        self.tombol_tutup.add(self.gambar_tutup)
        
        self.tombol_tujuh = gtk.Button()
        self.tombol_tujuh.add(self.gambar_tujuh)        

        self.tombol_delapan = gtk.Button()
        self.tombol_delapan.add(self.gambar_delapan)

        self.tombol_sembilan = gtk.Button()
        self.tombol_sembilan.add(self.gambar_sembilan)

        self.tombol_bagi = gtk.Button()
        self.tombol_bagi.add(self.gambar_bagi)

        self.tombol_empat = gtk.Button()
        self.tombol_empat.add(self.gambar_empat)

        self.tombol_lima = gtk.Button()
        self.tombol_lima.add(self.gambar_lima)

        self.tombol_enam = gtk.Button()
        self.tombol_enam.add(self.gambar_enam)

        self.tombol_silang = gtk.Button()
        self.tombol_silang.add(self.gambar_silang)
   
        self.tombol_satu = gtk.Button()
        self.tombol_satu.add(self.gambar_satu)

        self.tombol_dua = gtk.Button()
        self.tombol_dua.add(self.gambar_dua)

        self.tombol_tiga = gtk.Button()
        self.tombol_tiga.add(self.gambar_tiga)

        self.tombol_kurang = gtk.Button()
        self.tombol_kurang.add(self.gambar_kurang)
   
        self.tombol_nol = gtk.Button()
        self.tombol_nol.add(self.gambar_nol)

        self.tombol_titik = gtk.Button(".")

        self.tombol_sama_dengan = gtk.Button()
        self.tombol_sama_dengan.add(self.gambar_sama_dengan)

        self.tombol_tambah = gtk.Button()
        self.tombol_tambah.add(self.gambar_tambah)


    def menu(self):
        self.papan_menu = gtk.MenuBar()
        
        self.pilihan = gtk.Menu()

        self.tentang = gtk.Menu()

        self.keluar = gtk.MenuItem("Keluar")
        
        self.pilihan.append(self.keluar)

        self.keterangan = gtk.MenuItem("Keterangan")

        self.tentang.append(self.keterangan)

        self.pokok_pilihan = gtk.MenuItem("Berkas")

        self.pokok_tentang = gtk.MenuItem("Ihwal")

        self.pokok_pilihan.set_submenu(self.pilihan)

        self.pokok_tentang.set_submenu(self.tentang)

        self.papan_menu.append(self.pokok_pilihan)

        self.papan_menu.append(self.pokok_tentang) 

    #def fiks(self):
        #self.tetap = gtk.Fixed()
        #self.tetap.put(self.tombol_ihwal, 275, 5)
        
    def masukan(self):
        self.masukan_angka = gtk.Entry()
    
    def tabel(self):
        self.tabel_kalkulator = gtk.Table(rows = 5, columns = 4, homogeneous = True)
        self.tabel_kalkulator.set_row_spacings(1)
        self.tabel_kalkulator.set_col_spacings(1)
        self.tabel_kalkulator.attach(self.tombol_kosong, 0, 1, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_persen, 1, 2, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_nool, 2, 3, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_tutup, 3, 4, 0, 1)

        self.tabel_kalkulator.attach(self.tombol_tujuh, 0, 1, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_delapan, 1, 2, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_sembilan, 2, 3, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_bagi, 3, 4, 1, 2)

        self.tabel_kalkulator.attach(self.tombol_empat, 0, 1, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_lima, 1, 2, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_enam, 2, 3, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_silang, 3, 4, 2, 3)

        self.tabel_kalkulator.attach(self.tombol_satu, 0, 1, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_dua, 1, 2, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_tiga, 2, 3, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_kurang, 3, 4, 3, 4)

        self.tabel_kalkulator.attach(self.tombol_nol, 0, 1, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_titik, 1, 2, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_sama_dengan, 2, 3, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_tambah, 3, 4, 4, 5)

    
    def kotak(self):
        self.kotak_vertikal = gtk.VBox(spacing = 20)
        
        self.kotak_horizontal_1 = gtk.HBox(spacing = 10)
        #self.kotak_horizontal_1.pack_start(self.tetap)       
        self.kotak_horizontal_1.pack_start(self.papan_menu)
        
        self.kotak_horizontal_2 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_2.pack_start(self.masukan_angka)

        self.kotak_horizontal_3 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_3.pack_start(self.tabel_kalkulator)

        self.kotak_vertikal.pack_start(self.kotak_horizontal_1)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_2)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_3)

        self.jendela.add(self.kotak_vertikal)

    def konek(self):
        #self.tombol_ihwal.connect("clicked", self.ihwal)
        self.keluar.connect("activate", gtk.main_quit)
        self.keterangan.connect("activate", self.ihwal)
        
        self.tombol_tutup.connect("clicked", self.panggilan_keluar)
        self.jendela.connect("destroy", self.panggilan_keluar)
        
        self.tombol_satu.connect("clicked", self.cetak_karakter, "1")    
        self.tombol_dua.connect("clicked", self.cetak_karakter, "2")
        self.tombol_tiga.connect("clicked", self.cetak_karakter, "3")
        self.tombol_empat.connect("clicked", self.cetak_karakter, "4")
        self.tombol_lima.connect("clicked", self.cetak_karakter, "5")

        self.tombol_enam.connect("clicked", self.cetak_karakter, "6")
        self.tombol_tujuh.connect("clicked", self.cetak_karakter, "7")
        self.tombol_delapan.connect("clicked", self.cetak_karakter, "8")
        self.tombol_sembilan.connect("clicked", self.cetak_karakter, "9")
        self.tombol_nol.connect("clicked", self.cetak_karakter, "0")
        self.tombol_titik.connect("clicked", self.cetak_karakter, ".")
        
        self.tombol_nool.connect("clicked", self.hitung, "Nol")
        self.tombol_kosong.connect("clicked", self.hitung, "Hapus") 
        self.tombol_silang.connect("clicked", self.hitung, "x")
        self.tombol_bagi.connect("clicked", self.hitung, ":")
        self.tombol_tambah.connect("clicked", self.hitung, "+")
        self.tombol_kurang.connect("clicked", self.hitung, "-")
        self.tombol_persen.connect("clicked", self.hitung, "%")
        self.tombol_sama_dengan.connect("clicked", self.hitung, "=")

    def ihwal(self, a):
        self.tentang = gtk.AboutDialog()
        self.tentang.set_program_name("Kalkulator UVT")
        self.tentang.set_version("0.1")
        self.tentang.set_license(license)
        self.tentang.set_copyright("(c) 2013 UVT")
        self.tentang.set_authors(authors)
        self.tentang.set_comments("Kalkulator Sederhana")
        self.tentang.set_website("http://universitas-virtual-terbuka.blogspot.com")
        self.tentang.set_logo(gtk.gdk.pixbuf_new_from_file("/usr/share/kalkuluvt/gambar/kalkulator.png"))
        self.tentang.run()
        self.tentang.destroy()
    
    def cetak_karakter(self, a, b):
        self.masukan_angka.insert_text(b, position = 20)

    def hitung(self, a, b):
        if b == "Hapus":
            self.masukan_angka.set_text("")
	elif b == "Nol":
	    self.masukan_angka.set_text("0")		
	elif b == "+":
	    self.tanda = 1
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "-":
	    self.tanda = 2
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "x":
	    self.tanda = 3
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == ":":
	    self.tanda = 4
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "%":
	    self.tanda = 5
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "=":
	    self.angka_kedua = self.masukan_angka.get_text()
	    jumlah1 = float(self.angka_pertama)
	    jumlah2 = float(self.angka_kedua)
	    if self.tanda == 1:
	        hasil = jumlah1 + jumlah2
	    elif self.tanda == 2:
	        hasil = jumlah1 - jumlah2
	    elif self.tanda == 3:
	        hasil = jumlah1 * jumlah2
	    elif self.tanda == 4:
	    	if jumlah2 == 0.0:
                    try:
		        hasil = jumlah1 / jumlah2
		    except:						
			hasil = "Maaf, angka kedua nol!"
		else:
	            hasil = jumlah1 / jumlah2
	    elif self.tanda == 5:
	        jumlah1 = int(jumlah1)
		jumlah2 = int(jumlah2)	
		hasil = jumlah1 % jumlah2
	    self.masukan_angka.set_text(str(hasil))
        
    def panggilan_keluar(self, a):
        gtk.main_quit()

if __name__ == "__main__":
    Kalkulator()
    gtk.main()

    
        


       
