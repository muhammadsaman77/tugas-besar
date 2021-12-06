### TUBES ALPRO ### # 
#Import Modul-Modul 
import login_view, order_view,confirm_view, os, sys,signup_view 
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QLabel, QMessageBox, QTableWidgetItem, QWidget 
from PyQt5.uic import loadUi 

#menu = [] # Array menu dengan format [nama_menu, harga, jumlah ketersediaan] 

data_member = [] # Array data member dengan format [nama_member, username, password] 
pesanan = [] # Array untuk mendata pesanan yang berisi integer sepanjang menu 
harga_total_perbarang_list = []
jumlah_barang_list = []
nama = []

### FUNGSI-FUNGSI ### 
# # Fungsi untuk membaca file yang bernama nama_file dan menaruhnya di dalam list_output sebagai sebuah array 
def daftar_akun(nama_file,email,username,password,no_hp):
    f = open(nama_file,"+")
    f.write(f"[{email},{username},{password},{no_hp}],\n") 
    f.close()
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
# Fungsi untuk menuliskan output dari pesanan ke file 
def tulis_file_pesanan(nama_file, username, list_pesanan,banyak, harga,harga_keseluruhan): 
    f = open(nama_file,"a") 
    f.write(f"{username},{str(list_pesanan)},{banyak},{harga},{harga_keseluruhan}\n") 
    f.close()
#Fungsi untuk menampilkan pesan melalui sebuah pop window 
def pop_message(text): 
    msg = QtWidgets.QMessageBox() 
    msg.setText("{}".format(text)) 
    msg.exec_()


### GUI ###
## Kelas untuk page Signup
class Signup (QtWidgets.QWidget, signup_view.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_signup_handler)
        self.pushButton_2.clicked.connect(self.btn_login_handler)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
    def btn_signup_handler (self):
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        no_hp = self.lineEdit_4.text()
        daftar_akun("member.txt",email,username,password,no_hp)
        pop_message("Sign Up telah berhasil")
        self.close()
        self.login = Login()
        self.login.show()
    def btn_login_handler (self):
        self.close()
        self.login = Login()
        self.login.show()        

## Kelas untuk page Login 
class Login(QtWidgets.QWidget, login_view.Ui_MainWindow ): 
    # Inisialisasi yang dijalankan saat memanggil kelas login 
    def __init__(self): 
        QtWidgets.QWidget.__init__(self) 
        self.setupUi(self) # Memanggil fungsi setupUi yang ada di login.py  
        nama.clear()
        pesanan.clear()
        jumlah_barang_list.clear()
        
        self.pushButton.clicked.connect(self.btn_login_handler) # Perintah yang dijalakan saat button login diklik 
        self.lineEdit_2.returnPressed.connect(self.pushButton.click) # Membuat enter yang pada kolom password langsung terhubung dengan button login # 
        self.pushButton_2.clicked.connect(self.btn_signup_handler)
    #Fungsi mengecek apakah username dan password terdapat di dalam array 
    def bool_check_username(self): 
        global no_member
        login_berhasil = False 
        username = self.lineEdit.text()# username yang diinput 
        password = self.lineEdit_2.text() # password yang diinput 
        for i in range(len(data_member)): 
            if data_member[i][1] == username: 
                if data_member[i][2] == password: 
                    nama.append(username)   
                    login_berhasil = True 
                else: 
                    break 
        return login_berhasil, i # Mengembalikan boolean dan no_member dari pengguna
    
    # Fungsi yang dijalankan saat button login diklik 
    def btn_login_handler(self): 
        valid = self.bool_check_username() 
        if (valid): 
            self.close() # Menutup page login 
            self.menu = Pemesanan() # Inisialisasi page pemesanan 
            self.menu.show() # Menampilkan page pemesanan 
        else: 
            pop_message("Username atau password tidak valid") 
    #Fungsi yang dijalankan saat button sign up di klik        
    def btn_signup_handler(self):
        self.close()
        self.signup = Signup()
        self.signup.show()
# Kelas untuk page Pemesanan Menu 
class Pemesanan(QtWidgets.QWidget, order_view.Ui_MainWindow): 
    # Inisialisasi yang dijalankan saat memanggil kelas pemesanan 
    row_number = 0
    total_harga= 0
    
    def __init__(self): 
        QtWidgets.QWidget.__init__(self) 
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.btn_pesan_handler)
        self.pushButton_5.clicked.connect(self.btn_signout_handler)
        self.pushButton_6.clicked.connect(self.btn_signout_handler)
        self.pushButton_4.clicked.connect(self.btn_ulangi_handler)
        self.pushButton_7.clicked.connect(self.btn_konfirmasi)
    #menu
    
    # Fungsi yang dijalankan saat button pesan dipencet 
    def btn_pesan_handler(self): 
        kode_barang = self.lineEdit.text()
        jumlah_barang = self.lineEdit_2.text()
        try:
            if kode_barang == "BK":
                barang = "Brokoli"
                harga = "9000"
            elif kode_barang == "KK":
                barang = "Kangkung"
                harga = "4000"
            elif kode_barang == "WTL":
                barang = "Wortel"
                harga = "20000"        
            elif kode_barang == "TRG":
                barang = "Terong"
                harga = "7000"
            elif kode_barang == "Apel":
                barang = "Apel"
                harga = "23000"
            elif kode_barang == "PSG":
                barang = "Pisang"
                harga = "12000"
            elif kode_barang == "SMK":
                barang = "Semangka"
                harga = "24000"
            elif kode_barang == "AB":
                barang = "Ayam Bumbu"
                harga = "34000"
            elif kode_barang == "IB":
                barang = "Ikan Bumbu"
                harga = 32000
            elif kode_barang == "UB":
                barang = "Udang Bumbu"
                harga = 48000

            harga_total_perbarang = int(harga) * int(jumlah_barang)
            self.tableWidget_2.setItem(Pemesanan.row_number,0,QTableWidgetItem(str(kode_barang)))
            self.tableWidget_2.setItem(Pemesanan.row_number,1,QTableWidgetItem(str(barang)))
            self.tableWidget_2.setItem(Pemesanan.row_number,2,QTableWidgetItem(str(harga)))
            self.tableWidget_2.setItem(Pemesanan.row_number,3,QTableWidgetItem(str(jumlah_barang)))
            self.tableWidget_2.setItem(Pemesanan.row_number,4,QTableWidgetItem(str(harga_total_perbarang)))
            harga_total_perbarang_list.append(harga_total_perbarang)
            pesanan.append(barang)
            jumlah_barang_list.append(jumlah_barang)
            Pemesanan.total_harga +=  harga_total_perbarang
            Pemesanan.row_number += 1
            pop_message("Barang telah dimasukkan kedalam pesanan")        
        except:
            pop_message("Masukkan kode produk yang sesuai")
         
    # Fungsi yang dijalankan saat button signout dipencet 
    def btn_signout_handler(self): 
        # Inisialisasi ulang semua variabel global yang ada  
        global pesanan 
        global total_harga 
        global nama
        total_harga = 0 
        pesanan = []  
        nama.clear()
        Pemesanan.row_number = 0
        #baca_file("menu.txt",menu) 
        self.close() #Menutup page konfirmasi 
        self.login = Login() 
        self.login.show() #Membuka page login 
    
    #fungsi yang dijalankan ketika btn ulangi pemesanan di klik
    def btn_ulangi_handler(self):
        global pesanan
        for row_delete in range (0,10):
            self.tableWidget_2.setItem(row_delete,0,QTableWidgetItem(""))
            self.tableWidget_2.setItem(row_delete,1,QTableWidgetItem(""))
            self.tableWidget_2.setItem(row_delete,2,QTableWidgetItem(""))
            self.tableWidget_2.setItem(row_delete,3,QTableWidgetItem(""))
            self.tableWidget_2.setItem(row_delete,4,QTableWidgetItem(""))
        Pemesanan.row_number = 0
        pesanan= []
    #Fungsi yang akan dijalankan saat btn Konfirmasi dijalankan
    def btn_konfirmasi(self):
        self.close()
        self.konfirmasi = Konfirmasi()
        self.konfirmasi.show()


# Kelas untuk page Konfirmasi Pesanan 
class Konfirmasi(QtWidgets.QWidget, confirm_view.Ui_MainWindow): 
    #Inisialisasi yang dijalankan saat memanggil kelas pemesanan 
    def __init__(self): 
        QtWidgets.QWidget.__init__(self) 
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.btn_ok_handler)
        self.pushButton_2.clicked.connect(self.btn_cancel_handler)
        #self.treeWidget.topLevelItem(0).setText(0,f"Total harga yang harus dibayar adalah {total_harga}")
        #self.treeWidget.topLevelItem(1).setText(1,f"Apakah anda ingin melanjutkan konfirmasi?")
    #fungsi yang dijalankan saat btn cancel di pencet
    def btn_cancel_handler(self):
        self.close() 
        self.pemesanan = Pemesanan() 
        self.pemesanan.show()
    #Fungsi yang dijalankan saat button Ok di page konfirmasi diklik 
    def btn_ok_handler(self):          
        tulis_file_pesanan("pesanan.txt",nama,pesanan,jumlah_barang_list,harga_total_perbarang_list,Pemesanan.total_harga) # Memperbarui file pesanan.txt
        pop_message(f"""-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=\n
Nama Pelanggan : {nama}\n
Total Pembayaran : {Pemesanan.total_harga}\n
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n
TERIMA KASIH TELAH BERBELANJA\n
MENGGUNAKAN JASA KAMI :)\n""")
        Pemesanan.row_number = 0
        self.close()
        self.login = Login()
        self.login.show()
### Program Utama ### 
if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    baca_file("member.txt",data_member) 
    # Membaca input dari file member.txt dan menyimpannya ke dalam array  
    pesanan = [] # Array untuk mendata pesanan yang berisi integer sepanjang menu 
    total_harga = 0 #Inisialisasi total harga di awal 
    login = Login() #Page yang pertama dibuka ketika program dijalankan 
    login.show()
    sys.exit(app.exec_()) #Keluar dari program apabila tombol x ditekan pada layar