import getpass, os, time, sys

def login () :
    batas = 3
    for a in range (batas) :
        print("*"*25)
        print("\tLogin User")
        print("*"*25)
        get_user = input("Masukkan Username Anda : ")
        get_password = getpass.getpass()
        proses_login()
        sukses = False
        file = open('D:\Project\login_terminal\database.txt','r')
        for i in file :
            nama,username,password = i.split(",")
            password = password.strip()

            if(get_user == username) and (get_password == password) :
                sukses = True
                break
        if (sukses):
            print("\nAnda Berhasil Login, Selamat Datang %s "%(nama))
            time.sleep(5)
            opsi = input("Apakah Anda Ingin Kembali Ke Menu Utama ? (Y/N) ")
            if opsi.lower() == 'y' :
                print("\nAnda Akan Dialihkan Ke Menu Utama Mohon Tunggu Sebentar")
                time.sleep(2)
                os.system("cls")
                pilih()
            elif opsi.lower() == 'n' :
                time.sleep(2)
                print("\nAnda Akan Tetap Berada Di Halaman Ini")
                time.sleep(120)
                exit()
            else :
                print("\nMohon Maaf Pilihan Tidak Tersedia")
            break
        else :
            print("\nMohon Maaf Username dan Password Yang Anda Masukkan Salah\nSilahkan Periksa Kembali")
            a -=1
            time.sleep(2)
            os.system("cls")
    else :
        print("Mohon Maaf Anda Salah Memasukkan Username/Password Sebanyak %s Kali"%(batas))
def register():
    print("*"*35)
    print("\tForm Register User")
    print("*"*35)
    nama = input("Masukkan Nama Anda : ")
    username = input("Masukkan Username Anda : ")
    password = getpass.getpass()
    simpan(nama,username,password)
    proses_register()
    print("Data Berhasil Disimpan")
    opsi = input("Apakah Anda Ingin Kembali Ke Menu Utama ? (Y/N) ")
    if opsi.lower() == 'y' :
        print("\nAnda Akan Dialihkan Ke Menu Utama Mohon Tunggu Sebentar")
        time.sleep(2)
        os.system("cls")
        pilih()
    elif opsi.lower() == 'n' :
        time.sleep(2)
        print("\nProgram Akan Kami Hentikan, Terima Kasih Telah Melakukan Registrasi Pada Sistem Ini")
    else :
        print("\nMohon Maaf Pilihan Tidak Tersedia, Anda Akan Kami Alihkan Ke Menu Utama")
        time.sleep(2)
        os.system("cls")
        mulai()
def simpan (nama,username,password) :
    file = open('D:\Project\login_terminal\database.txt','a')
    file.write("\n"+nama+","+username+","+password)
def mulai () :
    print("\nSelamat Datang Di Sistem\nSilahkan Masukkan Kata (Reg) Untuk Register User Baru | (Login) Untuk Login User ke Sistem |(Exit) Untuk Keluar Dari Program")
    pilih()
def pilih():
    opsi = input("Masukkan Kata (Reg) atau (Login) atau (Exit) : ")
    if opsi.lower() == "reg" :
        print("Anda Memimilih Form Registrasi User \nSilahkan Tunggu Sebentar Anda Akan Di Alihkan Ke Form Register")
        time.sleep(2)
        os.system("cls")
        register()
    elif opsi.lower() == "login" :
        print("Anda Memimilih Form Registrasi User \nSilahkan Tunggu Sebentar Anda Akan Di Alihkan Ke Form Login")
        time.sleep(2)
        os.system("cls")
        login()
    elif opsi.lower() == "exit" :
        print("Anda Telah Memilih Exit Program")
        time.sleep(2)
        os.system("cls")
        print("Terima KAsih Telah Menggunakan Program Ini Sampai Jumpa")
        time.sleep(2)
        exit()
    else:
        print("Mohon Maaf Pilihan Tidak Tersedia")
        time.sleep(2)
        os.system("cls")
        mulai()
def proses_login():
    try:
        L="/-\\|"
        for q in range(20):
            time.sleep(0.1)
            sys.stdout.write("\rMemeriksa Data User" +L[q % len(L)]+"")
            sys.stdout.flush()

    except :
        os.system("cls")
        exit()
def proses_register():
    try:
        L="/-\\|"
        for q in range(20):
            time.sleep(0.1)
            sys.stdout.write("\rMenambahkan Data User" +L[q % len(L)]+"")
            sys.stdout.flush()

    except :
        os.system("cls")
        exit()
mulai()
