# Sistem Reservasi Buku Perpustakaan

import datetime
import os
import time

akun = {
    "vita" : {
        "password" : "vita121",
        "role" : "admin"
    },
    "user" : {
        "password" : "user123",
        "role" : "user"
    }
}

def login(): 
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    if username in akun and password == akun[username]["password"]:
        print("login berhasil!")
        print("role:", akun[username]["role"])
        return akun[username]["role"]
    else:
        print("login gagal! username atau password salah.")
        return False
    

    
reservasi = {
    1: {"judul": "Algoritma Pemrograman", "nama": "vita", "tanggal": "2026-09-11", "status": "Menunggu"},
    2: {"judul": "Basis Data", "nama": "Andi", "tanggal": "2026-09-12", "status": "Selesai"},
    3: {"judul": "Jaringan Komputer", "nama": "jungkook", "tanggal": "2026-09-13", "status": "Menunggu"}
    }

def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def buat_id_baru():
    id_terbesar = 0
    for id_reservasi in reservasi.keys():
        if id_reservasi > id_terbesar:
            id_terbesar = id_reservasi
    return id_terbesar + 1

def tambah_reservasi(): 
    judul = input("masukan judul buku: ")
    nama = input("masukan nama pemesan: ")
    tanggal = input("masukan tanggal reservasi (YYYY-MM-DD): ")
    status = "menunggu"
    if judul == "" or nama == "":
        print("judul dan nama tidak boleh kosong.\n")
        return
    try:
        datetime.datetime.strptime(tanggal, "YYYY-MM-DD")
    except ValueError:
        print("format tanggal salah! contoh: 2026-11-31\n")
        return
    reservasi[buat_id_baru()] = {"judul": judul, "nama": nama, "tanggal": tanggal, "status": status}
    print("reservasi telah berhasil ditambahkan!\n")

def lihat_reservasi():
    if not reservasi:
        print("belum ada data reservasi.\n")
    else :
        print("daftar reservasi: ")
        for id_reservasi, data in reservasi.items():
            print(f"{id_reservasi}. judul: {data['judul']} , nama: {data['nama']} , tanggal: {data['tanggal']} , status: {data['status']}")
            print()

def ubah_status():
    if role != "admin":
        print("akses ditolak! hanya admin yang bisa mengubah status.\n")
        return
    if not reservasi: 
        print("tidak ada data yang mau diubah.\n")
        return
    lihat_reservasi()
    try:
        id_reservasi = int(input("pilih nomor reservasi yang ingin diubah statusnya: "))
        if id_reservasi in reservasi:
            status_baru = input("masukan status baru (menunggu/selesai/dibatalkan): ")
            if status_baru == "menunggu" or status_baru == "selesai" or status_baru == "dibatalkan":
                reservasi[id_reservasi]["status"] = status_baru
                print("status telah berhasil diubah!\n")
            else:
                print("status tidak valid.\n")
        else:
            print("nomor reservasi tidak valid.\n")
    except ValueError:
        print("input harus berupa angka.\n")

def hapus_reservasi():
    if role != "admin":
        print("akses ditolak! hanya admin yang bisa menghapus reservasi.\n")
        return
    if not reservasi:
        print("tidak ada data yang mau dihapus.\n")
        return
    lihat_reservasi()
    try:
        id_reservasi = int(input("pilih nomor reservasi yang ingin dihapus: "))
        if id_reservasi in reservasi:
            reservasi.pop(id_reservasi)
            print("reservasi telah berhasil dihapus!\n")
        else:
            print("nomor reservasi tidak valid.\n")
    except ValueError:
        print("input harus berupa angka.\n")

bersihkan_layar()
role = login()
while role == False:
    role = login()
time.sleep(1)

while True:
    print(">>>> SISTEM RESERVASI BUKU PERPUSTAKAAN <<<< ")
    print("1. tambahkan reservasi")
    print("2. lihat reservasi")
    print("3. ubah status reservasi")
    print("4. hapus reservasi")
    print("5. keluar")

    pilih = input("pilih menu (1-5): ")

    if pilih == "1" :
        tambah_reservasi()
    elif pilih == "2" :
        lihat_reservasi()
    elif pilih == "3" :
        ubah_status()
    elif pilih == "4" :
        hapus_reservasi()
    elif pilih == "5" :
        print("terimakasih! program selesai.")
        break
    else:
        print("pilihan tidak valid, silahkan coba lagi.\n")