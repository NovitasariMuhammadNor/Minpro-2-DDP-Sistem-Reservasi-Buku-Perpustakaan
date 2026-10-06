# Minpro-2-DDP-Sistem-Reservasi-Buku-Perpustakaan

*Nama : Novitasari Muhammad Nor*    
*Nim : 082*

# Penjelasan koding dan flowchart Sistem Reservasi Buku Perpustakaan    


# flowchart
<img width="578" height="443" alt="image" src="https://github.com/user-attachments/assets/0aa52baf-344e-4e1d-a1b5-53b9c7a6078f" />          

Program dimulai dengan menyiapkan dictionary akun dan reservasi, lalu membersihkan layar. Pengguna memasukkan username dan password, dan jika tidak cocok, input diulang sampai benar. Setelah login berhasil, role pengguna disimpan dan program berjeda 1 detik sebelum menampilkan menu utama.

Pada menu utama, pengguna memilih menu 1 sampai 5. Menu 1 meminta judul, nama pemesan, dan tanggal; jika semuanya valid, data disimpan ke dictionary dengan ID baru, jika tidak, muncul pesan error. Menu 2 menampilkan semua reservasi beserta ID-nya.

Menu 3 (ubah status) dan menu 4 (hapus) memeriksa role terlebih dahulu. Jika bukan admin, muncul pesan akses ditolak. Jika admin, pengguna memasukkan ID (dan status baru untuk menu 3); jika ID dan status valid, data diubah atau dihapus dari dictionary, jika tidak, muncul pesan error.

Menu 5 mengakhiri program, sedangkan pilihan lain menampilkan pesan tidak valid. Setelah setiap proses selesai, program kembali ke menu utama.      

# Koding

    
<img width="194" height="32" alt="image" src="https://github.com/user-attachments/assets/232bc694-39e7-4c6c-bc17-07e31a44553b" />     
  
1. Program menggunakan 3 library bawaan Python: datetime untuk memvalidasi tanggal, os untuk membersihkan layar terminal, dan time untuk memberi jeda setelah login.


<img width="246" height="109" alt="image" src="https://github.com/user-attachments/assets/08ce7c1c-3fc0-4836-a40e-3f115007574b" />    

2. Dictionary akun menyimpan data login, dengan username sebagai key dan password serta role (admin atau user) sebagai isinya. Dictionary ini dipakai untuk mencocokkan login dan menentukan hak akses pengguna.

<img width="315" height="121" alt="image" src="https://github.com/user-attachments/assets/472b5673-27eb-43c5-b173-5753ee560cea" />    
    
3. def login() meminta pengguna memasukkan username dan password, lalu mencocokkannya dengan dictionary akun. Jika cocok, program menampilkan pesan berhasil beserta role pengguna, dan role tersebut dikembalikan untuk menentukan hak akses. Jika tidak cocok, program menampilkan pesan gagal dan mengembalikan False, sehingga login diulang.

<img width="446" height="60" alt="image" src="https://github.com/user-attachments/assets/ed278be6-517c-471e-b2b1-ffaaba15416f" />      

4. Dictionary reservasi menyimpan data reservasi buku. Key-nya adalah ID reservasi (1, 2, 3, ...), dan isinya berupa dictionary lain yang memuat judul, nama pemesan, tanggal, dan status. Data diakses lewat ID, bukan index, sehingga ID tidak bergeser ketika ada data yang dihapus.

<img width="221" height="56" alt="image" src="https://github.com/user-attachments/assets/479e3396-ba04-4cd2-a0fc-8b1234c06fba" />      

5. bersihkan_layar() membersihkan tampilan terminal. Fungsi ini memeriksa sistem operasi dengan os.name: jika Windows ("nt"), program menjalankan perintah cls, sedangkan pada sistem lain (Mac/Linux) menjalankan clear. Fungsi ini dipanggil sekali saat program dimulai, sebelum login.


<img width="261" height="69" alt="image" src="https://github.com/user-attachments/assets/f8e87c2b-4804-4177-8b94-d266a9e04f1e" />    

6. buat_id_baru() membuat ID untuk reservasi baru. Program mengecek semua ID di dictionary reservasi dengan perulangan for, mencari yang paling besar, lalu mengembalikan nilainya ditambah 1. Jika dictionary kosong, ID pertama yang dihasilkan adalah 1.


<img width="413" height="158" alt="image" src="https://github.com/user-attachments/assets/a8e64920-da99-4fa5-8206-04809e257c94" />

     
7. tambah_reservasi() meminta judul buku, nama pemesan, dan tanggal reservasi. Input divalidasi: judul dan nama tidak boleh kosong, dan tanggal harus berformat tahun-bulan-tanggal (dicek dengan datetime dan try-except). Jika valid, data disimpan ke dictionary reservasi dengan ID baru dari buat_id_baru() dan status "menunggu". Jika tidak valid, program menampilkan pesan error dan kembali ke menu.


<img width="602" height="90" alt="image" src="https://github.com/user-attachments/assets/53f3bb10-75c8-42b3-820c-0505e57a8fdd" />      

8. lihat_reservasi() menampilkan semua data reservasi. Jika dictionary reservasi kosong, program menampilkan pesan bahwa belum ada data. Jika ada, program melakukan perulangan for pada setiap pasangan ID dan datanya, lalu mencetak ID, judul, nama pemesan, tanggal, dan status.


<img width="437" height="216" alt="image" src="https://github.com/user-attachments/assets/327c187b-56fa-48b5-8c03-8640ca1936aa" />        


9. ubah_status() mengubah status sebuah reservasi dan hanya bisa dipakai admin; user mendapat pesan "akses ditolak". Jika data kosong, program menampilkan pesan lalu berhenti. Jika tidak, daftar reservasi ditampilkan dan admin memilih ID reservasi. Setelah itu admin memasukkan status baru (menunggu, selesai, atau dibatalkan), yang divalidasi dengan if. Jika valid, status diperbarui di dictionary reservasi. Jika ID tidak ada atau status tidak valid, program menampilkan pesan error. Jika input ID bukan angka, try-except ValueError menangkapnya sehingga program tidak berhenti.


<img width="394" height="182" alt="image" src="https://github.com/user-attachments/assets/3d386680-3203-47c8-97c0-e03fd9350749" />      


10. hapus_reservasi() menghapus sebuah reservasi dan hanya bisa dipakai admin; user mendapat pesan "akses ditolak". Jika data kosong, program menampilkan pesan lalu berhenti. Jika tidak, daftar reservasi ditampilkan dan admin memilih ID reservasi yang ingin dihapus. Jika ID ada, datanya dihapus dari dictionary reservasi dengan pop(). Jika ID tidak ada, program menampilkan pesan error. Jika input bukan angka, try-except ValueError menangkapnya sehingga program tidak berhenti.


<img width="172" height="59" alt="image" src="https://github.com/user-attachments/assets/78868a48-89d6-4fc0-a6e9-32ea60ba17a2" />      


11. Bagian ini adalah proses awal program sebelum menu muncul. Pertama, bersihkan_layar() membersihkan tampilan terminal. Lalu login() dipanggil dan hasilnya (role pengguna) disimpan di variabel role. Selama login gagal (role == False), login() dipanggil lagi sampai username dan password benar. Setelah berhasil, time.sleep(1) memberi jeda 1 detik sebelum menu utama ditampilkan.


<img width="346" height="236" alt="image" src="https://github.com/user-attachments/assets/d671ff88-e90f-4a54-b6b6-72175b978249" />        


12. Berikut ini adalah menu utama program. Perulangan while True menampilkan menu 1-5 terus-menerus sampai pengguna memilih keluar. Pilihan pengguna disimpan di variabel pilih, lalu dicek dengan if-elif: menu 1 memanggil tambah_reservasi(), menu 2 lihat_reservasi(), menu 3 ubah_status(), dan menu 4 hapus_reservasi(). Menu 5 menampilkan pesan penutup dan menghentikan perulangan dengan break, sehingga program selesai. Jika pilihan selain 1-5, program menampilkan pesan "pilihan tidak valid" lalu menu muncul lagi.



# Output

*1.*

<img width="399" height="151" alt="image" src="https://github.com/user-attachments/assets/72424c64-51cb-4795-8529-8786fa2d90e2" />              


 *2.*       
<img width="374" height="210" alt="image" src="https://github.com/user-attachments/assets/03a2df8c-aee0-4065-92aa-776308351dd2" />           


*3.*

<img width="369" height="341" alt="image" src="https://github.com/user-attachments/assets/84bf94b5-fac7-4392-ac18-e3c64f8945f6" />          

*4.*

<img width="378" height="371" alt="image" src="https://github.com/user-attachments/assets/6eada7c3-1347-4484-8662-937fcc6c259c" />                              

*5.*

<img width="370" height="348" alt="image" src="https://github.com/user-attachments/assets/1cd3c98b-ad34-41b0-9d40-dcd7aea4a0dc" />                              

*6.*

<img width="369" height="374" alt="image" src="https://github.com/user-attachments/assets/dc083e68-05a6-4d36-b8df-ed9f0bd83c5f" />












