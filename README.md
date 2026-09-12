# minpro1_sarah024

Nama: Sarah Afifah Ramadhani

Kelas: A

NIM: 2609116024(Genap)

# PENJELASAN MENGENAI PROGRAM

  Program sederhana yang saya buat digunakan untuk mengelola data karya lukisan dari pelukis terkenal. User dapat mendata nama dari lukisan, nama pelukis dan tahun lukisan tersebut debut. Konsepnya terdiri dari 'Create' untuk menambahkan data baru, 'Read' untuk menampilkan data yang sudah ada pada list yang sudah diisi oleh user, 'Update' untuk mengubah data pada list dan 'Delete' untuk menghapus data yang ada pada list. Berikut adalah flowchart untuk program yang saya buat. 

  <img width="1561" height="1762" alt="sararaaaa drawio" src="https://github.com/user-attachments/assets/3f01737f-e5e1-49da-a59a-170cba9cad4c" />


# INPUT dan OUTPUT
1. 
<img width="575" height="301" alt="Screenshot 2026-09-12 143934" src="https://github.com/user-attachments/assets/410784ee-0548-4ac3-8b97-e2fe7c6a4f0f" />


 While true(perulangan) disini agar program terus berproses dan selalu kembali ke menu utama setiap user melakukan suatu aksi(melihat atau menambah data)

<img width="424" height="179" alt="Screenshot 2026-09-12 152748" src="https://github.com/user-attachments/assets/4a5210e7-a3ab-4edf-b6da-85a49f6317e2" />

Gambar diatas adalah Output dari input gambar 1

2. 
<img width="590" height="433" alt="Screenshot 2026-09-12 144034" src="https://github.com/user-attachments/assets/91d7a4c3-26b9-410c-92f2-ef05978ec64f" />

ini adalah input dan output ubtuk fitur "view art", program memeriksa list artwork terlebih dahulu. Jika len() lebih dari nol, program akan menggunakan perulangan for lalu menampilkan isi dari list dari indeks awal sampai terakhir.

3. 
<img width="530" height="341" alt="Screenshot 2026-09-12 134120" src="https://github.com/user-attachments/assets/caeef3f1-35de-4dfb-af56-58357aee6856" />

ini adalah input dan output untuk fitur "add art", fitur ini bertugas untuk menambah data baru dengan meminta user untuk input judul, seniman dan tahun yang akan disimpan dalam kurung siku dan menggunakan fungsi .append untuk membuat list baru.

4. 
<img width="645" height="287" alt="Screenshot 2026-09-12 155237" src="https://github.com/user-attachments/assets/19e09a63-d4c1-4439-8c4c-4b104233482b" />

ini adalah input dari fitur "change art", fitur ini digunakan untuk memperbarui data dengan cara menimpa data awal dengan data baru yang diperbarui oleh user.

<img width="335" height="377" alt="Screenshot 2026-09-12 155404" src="https://github.com/user-attachments/assets/7b7ebbca-4b8f-4410-b073-679c2d03441b" />

ini adalah output dari gambar 4. terlihat point ke 3 yang berubah dari karya seni dari Frida Kahlo menjadi karya seni dari Berthe Morisot.

5. 
<img width="574" height="436" alt="Screenshot 2026-09-12 161445" src="https://github.com/user-attachments/assets/53d0a0ec-2640-4e16-8016-e8c68c201ccc" />

ini adalah input dan output dari fitur "delete art", fitur ini digunakan untuk menghapus data karya seni dengan menggunakan fungsi artwork.pop.

6. 
<img width="362" height="431" alt="Screenshot 2026-09-12 161508" src="https://github.com/user-attachments/assets/5124529f-f90f-47fe-8d1a-dd9444147acf" />

ini adalah input dan output dari fitur "exit", fitur ini akan menghentikan (While True) atau perulangan dengan fungsi 'break'. Jika user menginput nomor selain yang ada di menu maka program akan memberikan output "system error".
