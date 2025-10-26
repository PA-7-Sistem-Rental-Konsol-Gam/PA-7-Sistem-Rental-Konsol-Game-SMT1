# PROJECT AKHIR KELOMPOK 7 DDP

<b> Sistem Rental Konsol Game</b>

# Anggota Kelompok

 1. Riaz Ramadan Al Fattah (2509116106)
 2. Arizky Saputra (2509116088)
 3. Otniel Putra Wardana (2509116081)

# Flowchart Program
<h2>A. Flowchart Menu Utama</h2>
<img width="1191" height="891" alt="Flowchart Menu Utama drawio" src="https://github.com/user-attachments/assets/de9df609-3338-4c64-8396-11f303ef28ae" />
<p style="text-align: center;"></p>

<br>
Bagian Flowchart ini menjelaskan bagaimana alur program akan berjalan saat program mulai dijalankan.
Bagian-bagian program dijelaskan dalam beberapa poin sebagai berikut:

<br><b>1. START</b>
    <p>Sistem mulai menjalankan isi dari program</p>

<br><b>2. Input - Memasukkan Pilihan dari Menu Utama</b>

   <p> Setelah program mulai dijalankan, program akan menampilkan pilihan menu yang terdapat dalam program, diantaranya adalah : <br>
    1. Log in <br>
    2. Registrasi <br>
    3. Keluar
    </p>

<p> Pengguna kemudian dapat memasukkan salah satu dari pilihan menu yang tersedia dengan menginput "1" untuk Log in atau masuk ke akun pengguna yang sebelumnya telah terdaftar pada sistem. </p>

<p> Pengguna juga dapat menginput pilihan "2" untuk melakukan Registrasi akun baru. </p>

<p> Jika pengguna selesai menggunakan aplikasi, pengguna dapat menginput pilihan "3" untuk keluar dan mengakhiri program. </p>


<br><b>3. Input Decision - Conditial Statement berdasarkan pilihan User</b>
<br>
<p>Setelah pengguna memasukkan pilihan menu yang diinginkan, selanjutnya sistem akan menentukan alur program selanjutnya yang diperlukan sesuai kebutuhan pengguna</p>

<br>
    <p><b>- Pilihan 1 : Log in<br><br></b>
    <img width="1233" height="183" alt="Screenshot 2025-10-26 170002" src="https://github.com/user-attachments/assets/f3bd0ee0-655c-4beb-95e4-1e4ee7a82482" /> <br>
<p>Bagian ini menjelaskan jika pengguna memilih menu Log in. Sistem akan meminta pengguna untuk memasukkan Username dan Password dari akun yang telah terdaftar.<br>
Setelah itu sistem akan melakukan verifikasi akun dengan database berdasarkan Username dan Password yang dimasukkan pengguna.</p>

<p>

 - Jika proses verifikasi Username dan Password pengguna telah terdaftar, maka program akan menampilkan Username dan Role atau Hak akses pengguna, dan kemudian akan menampilkan pilihan menu berdasarkan Role akun pengguna.

 - Sebaliknya jika proses verifikasi Username dan Password pengguna belum terdaftar, maka program akan menampilkan pesan "Akun tidak terdaftar", dan program akan mengembalikan pengguna ke menu utama 
 
 </p>

<br>
    <p><b>- Pilihan 2 : Registrasi<br><br></b>
    <img width="1754" height="251" alt="Screenshot 2025-10-26 172641" src="https://github.com/user-attachments/assets/8ad07504-5fdc-4c62-b430-035e403fdb99" /> <br>

<p>Bagian ini menjelaskan jika pengguna memilih menu Registrasi akun baru.<br>Pengguna akan diminta untuk memasukkan Username dan Password untuk membuat akun baru. <br>
Setelah itu program akan menyimpan data Username dan Password tersebut ke database dan kemudian menampilkan Username, ID user, dan Role dari akun yang telah dibuat oleh pengguna.
</p>
<br>
    <p><b>- Pilihan 3 : Keluar <br><br></b>
    <img width="544" height="131" alt="Screenshot 2025-10-26 173118" src="https://github.com/user-attachments/assets/f6cca0d0-8f46-4a55-9c1a-0142589058dd" /> <br>

<p>Bagian ini menjelaskan jika pengguna memilih menu Keluar. <br>
Sistem akan menampilkan pesan "Selamat tinggal" dan kemudian akan mengakhiri semua program yang berjalan.
<br>

 <p><b>- Pilihan Tidak Valid <br><br></b>
<img width="653" height="203" alt="Screenshot 2025-10-26 173350" src="https://github.com/user-attachments/assets/04b9e7f9-f7fa-460b-9c8a-34f1a6b37da9" />

<p> Bagian ini menjelaskan jika pengguna memasukkan pilihan selain dari pilihan 1, 2, atau 3. Maka sistem akan menampilkan pesan "Menu tidak valid" dan akan mengembalikan pengguna ke tampilan Menu Utama.

<br>
<h2>B. Flowchart Menu User as Admin</h2>
<img width="1022" height="2266" alt="Flowchart Menu Admin drawio" src="https://github.com/user-attachments/assets/30060264-294a-4fd0-8542-ec70165f0c8f" /> <br><br>

<p>Bagian ini menjelaskan bagaimana alur program setelah pengguna melakukan Log in dan terverifikasi sebagai Admin. Sistem akan menampilkan pilihan menu dan hak akses yang dimiliki oleh Admin.<br>
Beberapa pilihan menu yang dimiliki oleh akun Admin yaitu : <br>

<b>1. Lihat semua produk.</b> <br>
<p>Pilihan ini akan mengarahkan sistem untuk mengambil data produk yang tersimpan pada database, yang kemudian akan ditampilkan dalam bentul Tabel kepada pengguna.</p>
<img width="885" height="123" alt="Screenshot 2025-10-26 175359" src="https://github.com/user-attachments/assets/074e4144-0996-486d-9254-e7603918c695" /> <br><br>

<b>2. Tambah Produk</b> <br> <br>
<img width="875" height="104" alt="Screenshot 2025-10-26 175814" src="https://github.com/user-attachments/assets/7ac7aaea-655b-4617-9775-59dcef0bc752" /> <br>

<p>Bagian ini digunakan untuk menambah produk baru kedalam database. Pengguna akan diminta memasukkan Nama Produk, Nama Brand, Tarif Rental(dalam satuan jam), dan Jumlah Stok yang ada. <br>
Setelah itu sistem akan menyimpan data tersebut ke database, setelah berhasil maka program akan memberikan pesan "Produk berhasil ditambahkan", Lalu pengguna akan diarahkan kembali ke Menu Admin.

 <b>3. Ubah Produk</b> <br> <br>
<img width="875" height="92" alt="Screenshot 2025-10-26 214908" src="https://github.com/user-attachments/assets/a2785361-3cde-4ab7-87fb-f0f8d3225e7a" /> <br>

<p>Pilihan Ubah Produk dapat digunakan untuk mengedit detail dari suatu produk rental yang tersedia. <br>
Untuk mengubah suatu produk, pengguna akan terlebih dahulu diminta untuk memasukkan "ID Produk" yang terdapat dalam database. Jika ID Produk yang diinput tersebut sesuai dengan ID Produk yang ada dalam database, Selanjutnya pengguna dapat mengubah detail dari produk dengan memasukkan "Nama Produk, Nama Brand, Tarif rental, dan Stok produk" baru. <br>
Setelah menginput data produk, selanjutnya program akan menyimpan perubahan data tersebut ke database dan akan menampilkan pesan "Perubahan berhasil disimpan" lalu kemudian akan mengarahkan tampilan pengguna ke menu utama User Admin 

<b>4. Hapus Produk</b> <br> <br>
<img width="945" height="268" alt="Screenshot 2025-10-26 223126" src="https://github.com/user-attachments/assets/8c3e3c4b-c47f-4242-8449-832a3a62a499" />
<p>Pilihan ke-4 ini menjelaskan alur program ketika pengguna ingin menghapus sebuah produk yang terdaftar dalam database</p> <br>

<b>5. Lihat Semua Pengguna</b> <br> <br>
<img width="848" height="144" alt="Screenshot 2025-10-26 223742" src="https://github.com/user-attachments/assets/09ce46bb-48e4-443e-9537-96f501b4eb2d" /> <br>

<p>Pilihan ini akan mengarahkan program untuk menampilkan daftar pengguna dalam bentuk tabel yang terdaftar dalam Database.</p> <br>

<b>6. Ubah Pengguna</b> <br> <br>
<img width="925" height="225" alt="Screenshot 2025-10-26 224849" src="https://github.com/user-attachments/assets/1ea5aaa6-9cdf-4284-b4d3-73c097d8583e" /> <br>

<p>Pilihan ini digunakan untuk mengubah data dari akun user yang terdaftar di dalam database. Data yang dapat diubah adalah Username, Role akun(Admin/Customer User), dan Saldo Pengguna.</p> <br>

<b>7. Hapus Pengguna</b> <br> <br>
<img width="915" height="318" alt="Screenshot 2025-10-26 225818" src="https://github.com/user-attachments/assets/1579e739-8bed-48b7-9806-52a38cec87a1" />

<p>Pilihan ini berfungsi untuk menghapus akun pengguna yang sebelumnya telah terdaftar di Database. Pengguna(Admin) menginputkan IDD User yang ingin dihapus, dan kemudian sistem akan menghapus data user tersebut dari database</p> <br>

<b>8. Lihat Semua Transaksi</b> <br> <br>
<img width="870" height="147" alt="Screenshot 2025-10-26 230448" src="https://github.com/user-attachments/assets/e5f4823d-7103-4c25-91c5-5b721a8218f0" />

<p>Pilihan ini berfungsi untuk menampilkan semua riwayat transaksi yang terjadi dan disimpan di dalam database.</p>

<b>9. Log Out</b> <br> <br>
<img width="751" height="117" alt="Screenshot 2025-10-26 230757" src="https://github.com/user-attachments/assets/438d5e9c-fa62-4f92-b494-869d32894b84" />

<p>Pilihan ini digunakan jika user ingin keluar dari akun saat ini. Sistem akan mengeluarkan pengguna dari akun saat ini dan akan mengarahkan pengguna kembali ke Menu Utama </p> <br>

<p>
- Jika Pengguna memasukkan input selain dari pilihan yang tersedia (1 - 9), maka sistem hanya akan menampilkan pesan "Pilihan tidak valid" dan mengembalikan pengguna ke tampilam menu awal.


<h2>C. Flowchart Menu Customer</h2>
<img width="1786" height="1286" alt="Flowchart Menu User Customers drawio" src="https://github.com/user-attachments/assets/62c6026b-fc20-4b27-9a42-574aedd0247d" />
<br><br>

<p>Bagian ini menjelaskan bagaimana alur program setelah pengguna melakukan Log in dan terverifikasi sebagai User Customer. Sistem akan menampilkan pilihan menu dan hak akses yang dimiliki oleh Customers.</p>

Beberaoa pilihan menu yang dimiliki oleh akun Customer yaitu : <br>

<b>1. Lihat Produk </b>
<img width="821" height="136" alt="Screenshot 2025-10-27 013205" src="https://github.com/user-attachments/assets/8702f808-b88e-4e14-a945-d4e8b2e1d6ec" />

<p>Pilihan ini berfungsi untuk menampilkan list data produk yang tersedia dalam sistem Rental Konsol Game</p>


<b>2. Top Up Saldo</b>
<img width="1272" height="188" alt="Screenshot 2025-10-27 013548" src="https://github.com/user-attachments/assets/7002fb4d-e477-47d4-ba05-abb8a20c90f1" />

<p>Pilihan ini dapat digunakan user untuk melakukan pengisian saldo E-Money yang dapat digunakan untuk melakukan penyewaan produk Konsol Game. </p>


<b>3. Sewa Produk</b>
<img width="1618" height="235" alt="Screenshot 2025-10-27 013938" src="https://github.com/user-attachments/assets/dfb6233a-db82-445c-b6a9-7741aba76665" />

<p>Pilihan ini digunakan untuk melakukan transaksi atau penyewaan konsol game. Pengguna akan diminta untuk memasukkan ID produk dan durasi rental dari produk yang ingin disewa, lalu selanjutnya akan masuk ke proses pembayaran biaya sewa konsol game nya.</p>


<b>4. Lihat Riwayat Transaksi</b>
<img width="762" height="129" alt="Screenshot 2025-10-27 014502" src="https://github.com/user-attachments/assets/6ec4446e-e2cc-4d3b-a549-4317a1d7bfc3" />

<p>Pilihan ini akan menampilkan kepada pengguna tentang riwayat transaksi yang pernah dilakukan dalam akun pengguna tersebut.</p>


<b>5. Log Out</b><br>
<img width="355" height="251" alt="Screenshot 2025-10-27 014733" src="https://github.com/user-attachments/assets/dafcafb5-9c28-4d4d-bb0b-e83b39250e8f" />

<p>Pilihan ini digunakan jika pengguna ingin keluar dari akun saat ini, kemudian program akan mengarahkan pengguna kembali ke menu utama. <br>

- Jika pengguna memasukkan input menu selain dari menu yang tersedia (1 - 5), maka sistem hanya akan menampilkan pesan "Pilihan menu tidak valid", dan kemudian akan mengembalikan pengguna ke tampilan menu Customer</p><br>

# Panduan Penggunaan Program
<h2>A. Menu Utama</h2><br>
<img width="329" height="122" alt="Screenshot 2025-10-27 020037" src="https://github.com/user-attachments/assets/3f0266b3-8b26-4433-a94c-e90ee3d709fd" />

<p>Pada tampilan menu utama setelah program dijalankan, sistem akan menampilkan 3 pilihan menu yang dapat digunakan oleh pengguna. Masing-masing menu memiliki kegunaannya masing-masing yaitu :</p><br>

<b><p>1. Log in</p></b>
<br>
<img width="339" height="129" alt="Screenshot 2025-10-27 020649" src="https://github.com/user-attachments/assets/4c31fa10-1575-4b5f-92d5-777c2594d7f1" /> <br>

<p>Pilihan menu ini digunakan untuk masuk ke akun pengguna yang sebelumnya telah terdaftar dalam database. Jenis akun pengguna terbagi menjadi 2 role, yaitu akun Admin dan akun Customer, yang masing-masing memiliki hak akses nya masing-masing dalam program</p>












