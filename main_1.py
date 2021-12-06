### TUBES ALPRO ### # 
#Import Modul-Modul 
import login_view, order_view, os, sys 
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem 
from PyQt5.uic import loadUi 

# Deklarasi variabel global yang dapat digunakan di semua kelas yang ada 
global menu 
global data_member 
global pesanan 
global no_member 
global total_harga 
menu = [] # Array menu dengan format [nama_menu, harga, jumlah ketersediaan] 
data_member = [] # Array data member dengan format [nama_member, username, password] 
pesanan = [] # Array untuk mendata pesanan yang berisi integer sepanjang menu 


### FUNGSI-FUNGSI ### 
# # Fungsi untuk membaca file yang bernama nama_file dan menaruhnya di dalam list_output sebagai sebuah array 
def baca_file(nama_file, list_output): 
    list_output.clear() # Mengosongkan isi list output 
    f = open(nama_file,"r") 
    for line in f: 
        list_output.append(line.strip("\n")) 
    f.close() 
    # Memisahkan elemen-elemen yang terpisahkan dengan , di dalam txt 
    for i in range(len(list_output)): 
        list_output[i] = list_output[i].split(",") 
    return list_output 
    
# Fungsi untuk menulis array ke dalam file nama_file 
def tulis_file(nama_file, list_input):
    f = open(nama_file,"w") 
    for elemen_baris in list_input: 
        for i in range(len(elemen_baris)): 
            if (i != len(elemen_baris)-1): 
                f.write(str(elemen_baris[i])+",") 
            else: 
                f.write(str(elemen_baris[i])) 
        f.write("\n") 
    f.close() 
    
# Fungsi untuk menuliskan output dari pesanan ke file 
def tulis_file_pesanan(nama_file, username, harga, list_pesanan): 
    f = open(nama_file,"a") 
    f.write(username+","+str(harga)+",") 
    for i in range(len(list_pesanan)): 
        if (i != len(list_pesanan)-1): 
            f.write(str(list_pesanan[i])+",") 
        else: 
            f.write(str(list_pesanan[i])) 
    f.write("\n") 
    f.close() 
      
# Fungsi untuk mencetak hasil pesanan 
def print_pesanan(pesanan,menu): 
    output = "" 
    index = 1 
    for i in range(len(pesanan)): 
        if pesanan[i] != 0: 
            output += f"{index}. {pesanan[i]} {menu[i][0]}\n" 
            index += 1
            return output 
            

#Fungsi untuk menampilkan pesan melalui sebuah pop window 
def pop_message(text): 
    msg = QtWidgets.QMessageBox() 
    msg.setText("{}".format(text)) 
    msg.exec_()


### GUI ### 
# # Kelas untuk page Login 
class Login(QtWidgets.QWidget, login_view.Ui_MainWindow ): 
    # Inisialisasi yang dijalankan saat memanggil kelas login 
    def __init__(self): 
        QtWidgets.QWidget.__init__(self) 
        self.setupUi(self) # Memanggil fungsi setupUi yang ada di login.py 
        #self.setFixedSize(439,582) 
        self.pushButton.clicked.connect(self.btn_login_handler) # Perintah yang dijalakan saat button login diklik 
        #self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password) # Membuat password menjadi tidak terlihat 
        self.lineEdit_2.returnPressed.connect(self.pushButton.click) # Membuat enter yang pada kolom password langsung terhubung dengan button login # 
        
    #Fungsi mengecek apakah username dan password terdapat di dalam array 
    def bool_check_username(self): 
        login_berhasil = False 
        username = self.lineEdit.text()# username yang diinput 
        password = self.lineEdit_2.text() # password yang diinput 
        for i in range(len(data_member)): 
            if data_member[i][1] == username: 
                if data_member[i][2] == password: 
                    login_berhasil = True 
                else: 
                    break 
        return login_berhasil, i # Mengembalikan boolean dan no_member dari pengguna
    
    # Fungsi yang dijalankan saat button login diklik 
    def btn_login_handler(self): 
        #global no_member 
        valid, no_member = self.bool_check_username() 
        if (valid): 
            self.close() # Menutup page login 
            self.menu = Pemesanan() # Inisialisasi page pemesanan 
            self.menu.show() # Menampilkan page pemesanan 
        else: 
            pop_message("Username atau password tidak valid") 
    #Fungsi yang dijalankan saat button sign up di klik        
    def btn_signup_handler(self):
        pass
# Kelas untuk page Pemesanan Menu 
class Pemesanan(QtWidgets.QWidget, order_view.Ui_MainWindow): 
    # Inisialisasi yang dijalankan saat memanggil kelas pemesanan 
    def __init__(self): 
        QtWidgets.QWidget.__init__(self) 
        self.setupUi(self) 
            # Penanganan Button SignOut 
#        self.pushButton_5.clicked.connect(Login())
 #       self.pushButton_6.clicked.connect(Login()) 
        
            # Penanganan Button Pesan 
        #self.pushButton.clicked.connect(self.btn_hapus_handler)  
    # Penanganan Button Hapus 
        #self.btn_selanjutnya.clicked.connect(self.btn_selanjutnya_handler) # Penanganan Button Selanjutnya 
    
    # Fungsi yang dijalankan saat button signout dipencet 
    """def btn_signout_handler(self): 
        # Inisialisasi ulang semua variabel global yang ada 
        global no_member 
        global pesanan 
        global total_harga 
        no_member = -1 
        pesanan = [0 for i in range(len(menu))] 
        total_harga = 0 
        baca_file("menu.txt",menu) 
        self.close() #Menutup page konfirmasi 
        self.login = Login() 
        self.login.show() #Membuka page login 
        
    # Fungsi yang dijalankan saat button pesan dipencet 
    def btn_pesan_handler(self): 
        global total_harga 
        no_menu = self.txt_id.text() 
        # Exception untuk mengecek apakah masukkan berupa angka atau tidak 
        try: 
            no_menu = int(no_menu) 
        except: 
            pop_message("Input yang ada harus berupa angka") 
            return #Langsung mengakhiri fungsi 
        # Exception untuk mengecek apakah masukkan valid atau ada di menu 
        try: 
            assert no_menu >= 0, "Tidak ada menu dengan nomor menu yang sesuai" 
            assert no_menu < len(menu), "Tidak ada menu dengan nomor menu yang sesuai" 
            assert int(menu[no_menu][2])>0, "Menu yang dipilih sudah sold out" 
            pesanan[no_menu] += 1 #Menambahkan elemen di array pesanan 
            total_harga += int(menu[no_menu][1]) #Menambahkan total harga dengan harga menu 
            menu[no_menu][2] = int(menu[no_menu][2])-1 #Mengurangkan jumlah yang tersedia

            pop_message("Berhasil Menambahkan Menu ke Pesanan") 
            
            self.table_daftarmenu.setItem(no_menu,3,QTableWidgetItem(str(menu[no_menu][2]))) #Update Kolom Jumlah Tersedia 

            self.table_daftarmenu.setItem(no_menu,4,QTableWidgetItem(str(pesanan[no_menu]))) #Update Kolom Jumlah Dipesan 
        except AssertionError as pesan: 
            pop_message(pesan) 
            
    # Fungsi yang dijalankan saat button hapus dipencet 
    def btn_hapus_handler(self): 
        global total_harga 
        no_menu = self.txt_id.text() 
    #Exception untuk mengecek apakah masukkan berupa angka atau tidak 
        try: 
            no_menu = int(no_menu) 
        except: 
            pop_message("Input yang ada harus berupa angka") 
            return
        #Langsung mengakhiri fungsi 
        #Exception untuk mengecek apakah masukkan valid atau ada di menu 
        try: 
            assert no_menu >= 0, "Tidak ada menu dengan nomor menu yang sesuai" 
            assert no_menu < len(menu), "Tidak ada menu dengan nomor menu yang sesuai" 
            assert int(pesanan[no_menu]) != 0, "Menu yang dipilih belum dipesan" 
            pesanan[no_menu] -= 1 #Mengurangkan elemen di array pesanan 
            total_harga -= int(menu[no_menu][1]) #Mengurangkan total harga dengan harga menu 
            menu[no_menu][2] = int(menu[no_menu][2])+1 #Menambahkan jumlah yang tersedia 
            pop_message("Berhasil Menghapus Menu dari Pesanan") 
            self.table_daftarmenu.setItem(no_menu,3,QTableWidgetItem(str(menu[no_menu][2]))) #Update Kolom Jumlah Tersedia 
            self.table_daftarmenu.setItem(no_menu,4,QTableWidgetItem(str(pesanan[no_menu]))) #Update Kolom Jumlah Dipesan 
        except AssertionError as pesan:    
            pop_message(pesan) 
        
# Fungsi yang dijalankan saat button selanjutnya dipencet 
def btn_selanjutnya_handler(self): 
    self.close() 
    self.konfirmasi = Konfirmasi() 
    self.konfirmasi.show() 
    """
# Kelas untuk page Konfirmasi Pesanan 
"""
class Konfirmasi(QtWidgets.QWidget, konfirmasi.Ui_Konfirmasi): 
    #Inisialisasi yang dijalankan saat memanggil kelas pemesanan 
    def __init__(self): 
        global total_harga 
        QtWidgets.QWidget.__init__(self) 
        self.setupUi(self) 
        harga_sebelum = total_harga # Harga sebelum didiskon 
        total_harga -= hitung_diskon(total_harga, data_member[no_member][3] == "True") 
        total_harga = int(total_harga) # Harga setelah didiskon 
        self.labelPesanan.setText("Pesanan:\n" + print_pesanan(pesanan,menu)+ "\n\nHarga Sebelum Diskon :"+" Rp. "+ str(harga_sebelum)+ "\nTotal Harga :"+" Rp." + str(total_harga)) # Menambahkan Tulisan ke Label Pesanan 
        self.btn_signout.clicked.connect(self.btn_signout_handler) # Penanganan Button SignOut 
        self.btn_kembali.clicked.connect(self.btn_kembali_handler) # Penanganan Button Kembali 
        self.btn_konfirmasi.clicked.connect(self.btn_konfirmasi_handler) # Penanganan Button Konfirmasi 
    #fungsi untuk pop_message pembayaran
    def pembayaran ():
        pay_msg = QMessageBox()
        pay_msg.setWindowTitle("Pembayaran")

    #Fungsi yang dijalankan saat button signout dipencet 
    def btn_signout_handler(self): 
        #Inisialisasi ulang semua variabel global yang ada 
        global no_member 
        global pesanan 
        global total_harga 
        no_member = -1 
        pesanan = [0 for i in range(len(menu))] 
        total_harga = 0 
        baca_file("menu.txt",menu)
        self.close() #Menutup page konfirmasi 
        self.login = Login() 
        self.login.show() #Membuka page login 
        
    #Fungsi yang dijalankan saat button kembali dipencet 
    def btn_kembali_handler(self): 
        self.close() 
        self.pemesanan = Pemesanan() 
        self.pemesanan.show() 
        
    #Fungsi yang dijalankan saat button konfrimasi dipencet 
    def btn_konfirmasi_handler(self): 
        global pesanan 
        global total_harga 
        if total_harga != 0: # Kalau pesanan yang ada tidak kosong 
            pop_message("Pesanan berhasil disimpan!") 
            tulis_file("menu.txt",menu) # Memperbarui file menu.txt 
            
            tulis_file_pesanan("pesanan.txt",data_member[no_member][1],total_harga,pesanan) # Memperbarui file pesanan.txt 

            pesanan = [0 for i in range(len(menu))] # Inisialisasi ulang array pesanan 
            total_harga = 0 # Inisialisasi ulang total harga 
        else: 
            pop_message("Belum ada menu yang dipesan") 
        self.close() 
        self.pemesanan = Pemesanan() 
        self.pemesanan.show() """
### Program Utama ### 
if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    baca_file("member.txt",data_member) 
    # Membaca input dari file member.txt dan menyimpannya ke dalam array 
    baca_file("menu.txt", menu) # Membaca input dari file menu.txt dan menyimpannya ke dalam array 
    pesanan = [0 for i in range(len(menu))] # Array untuk mendata pesanan yang berisi integer sepanjang menu 
    total_harga = 0 #Inisialisasi total harga di awal 
    login = Login() #Page yang pertama dibuka ketika program dijalankan 
    login.show()
    sys.exit(app.exec_()) #Keluar dari program apabila tombol x ditekan pada layar