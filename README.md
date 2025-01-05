# **PROJECT UAS**
|                |                    |
| -------------- | ------------------ |
|      _Nama_    | Dwi Okta Ramadhani |
|      _NIM_     |      312410056     |
|     _Kelas_    |      TI.24.A1      |
|  _Mata Kuliah_ | Bahasa Pemrograman |
| _Link Youtube_ |https://youtu.be/ZNCvNh08MnY |

## *Buatlah program sederhana dengan ketentuan program harus dibuat dengan konsep Modular dan OPP (pisahkan CLASS data,CLASS view,CLASS process)*
  1. Program harus meminta input dari pengguna 
  2. Tambahkan validasi input dapat menggunakan konsep eksepsi
  3. Program menampilkan hasil (dapat berupa table view)

# **Eatplaylove Café Cashier System**
![](https://github.com/Dwiokta10/UAS-Bahasa-Pemrograman-Semester-1/blob/main/Kasir-Project%20OPP-Modular/eatplaylovecave.png)
##  **Deskripsi Proyek**
Aplikasi ini adalah sistem kasir berbasis Python menggunakan paradigma **Object-Oriented Programming (OOP)**. Aplikasi ini dirancang untuk mengelola transaksi toko/restoran dengan antarmuka berbasis **Tkinter**. Proyek ini diatur secara modular untuk memastikan pengembangan, debugging, dan pemeliharaan yang efisien.
---

## **Fitur Utama:**
  1. Manajemen Menu
   * Tambahkan nama menu, harga, dan jumlah.
   * Tampilkan data menu dalam tabel.
  2. Penghitungan Otomatis
   * Menghitung subtotal, pajak (10%), biaya layanan (5%), total tagihan, dan kembalian.
  3. Validasi Input
   * Validasi input harga, jumlah, dan transfer.
  4. Hapus Item Menu
   * Kemudahan menghapus item yang tidak diinginkan dari daftar menu.
  5. Ringkasan Transaksi
   * Memberikan detail transaksi dalam format rapi dan siap dicetak.

## Struktur Folder
```plaintext
├── data/
│   ├── __init__.py
│   ├── data.py
├── process/
│   ├── __init__.py
│   ├── process.py
├── view/
│   ├── __init__.py
│   ├── viewGui.py
├── main.py
├── README.md
```
--- 

## **Struktur Kode**
* Aplikasi terdiri dari 3 modul utama:
  1. *Modul data.py:* Mengelola data menu dan transaksi.
  2. *Modul process.py:* Berisi fungsi-fungsi untuk memproses data seperti validasi, perhitungan, dan format harga.
  3. *Modul viewGui.py:* Menyediakan antarmuka pengguna berbasis Tkinter.
---

## **Modul data.py**
* Berfungsi untuk menyimpan dan mengatur data transaksi.
  * Fungsi Utama Data ini Nantinya Guna:
    1. *add_menu_item:* Menambahkan item ke dalam daftar menu.
    2. *remove_menu_item:* Menghapus item dari daftar.
    3. *calculate_total:* Menghitung total harga dari semua item.
```python
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from data.process import Process
```

## Class Untuk Menyimpan Data Transaksi
   * Kelas ini bertanggung jawab menyimpan data item menu, harga, jumlah, dan total harga untuk setiap transaksi. Data disimpan dalam tabel dinamis untuk kemudahan pengelolaan.
```python
class Data:
    def __init__(self):
        self.items = []  # Menyimpan item berupa dict {'name': str, 'price': float, 'quantity': int}

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def get_all_items(self):
        return self.items
```
---

## **Modul process.py**
* Modul ini berisi fungsi pendukung untuk validasi dan format data.
  ~ *Validasi Input:* Memastikan harga hanya berupa angka dan jumlah adalah bilangan bulat.
  ~ *Format Mata Uang:* Mengubah angka menjadi format Rupiah.

## Class Untuk Memproses Data Transaksi
   * Mengelola perhitungan subtotal, pajak, biaya layanan, total tagihan, dan kembalian. Selain itu, mencakup validasi input agar sesuai dengan logika bisnis aplikasi.
```python
class Process:
    TAX_RATE = 0.1  # Pajak 10%
    SERVICE_CHARGE = 0.05  # Biaya layanan 5%

    def __init__(self, data):
        self.data = data

    def calculate_subtotal(self):
        return sum(item["price"] * item["quantity"] for item in self.data.get_all_items())

    def calculate_tax(self, subtotal):
        return subtotal * self.TAX_RATE

    def calculate_service_charge(self, subtotal):
        return subtotal * self.SERVICE_CHARGE

    def calculate_total(self, subtotal, tax, service_charge):
        return subtotal + tax + service_charge
```
--- 

## **Modul viewGui.py**
* Modul ini bertanggung jawab atas antarmuka pengguna dengan fiturnya yang terdiri atas *komponen*, *logika dan validasi*.
```python
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from data.process import Process
```

## Class untuk GUI dan Interaksi Pengguna
   * Mengatur antarmuka pengguna menggunakan **Tkinter**, termasuk tata letak frame, tombol, tabel, dan elemen interaktif lainnya.
```python
class ViewGUI:
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.root.title("☕Eatplaylove Café☕ - Sistem Kasir ")
        self.root.geometry("800x600")
        self.root.configure(bg='#f8f4e3')

        self.create_widgets()

    def create_widgets(self):
```
---
## *Komponen Untuk GUI:*

### Nama Toko dengan Font Renitah
   * Nama **"Eatplaylove Café"** ditampilkan di bagian atas aplikasi menggunakan font khusus untuk memperkuat branding.
```python
        frame_title = tk.Frame(self.root, pady=10, bg='#f3e5d8')
        frame_title.pack(fill=tk.X)
        self.shop_name = tk.Label(frame_title, text="Eatplaylove Café ☕", font=('Renitah', 24, 'bold'), bg='#f3e5d8', fg='#e9967a')
        self.shop_name.pack()
```

### Frame untuk Input Menu
   * Frame ini memungkinkan pengguna memasukkan nama menu, harga, dan jumlah item melalui input teks. Terdapat tombol "Tambah Menu" untuk menambahkan item ke daftar transaksi dan menyimpan data input ke tabel.
```python
        frame_input = tk.Frame(self.root, padx=10, pady=10, bg='#f3e5d8')
        frame_input.pack(fill=tk.X)

        tk.Label(frame_input, text="Nama Menu: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=0, column=0, sticky=tk.W)
        self.entry_name = tk.Entry(frame_input, font=('Lucida Calligraphy', 12))
        self.entry_name.grid(row=0, column=1)

        tk.Label(frame_input, text="Harga: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=1, column=0, sticky=tk.W)
        self.entry_price = tk.Entry(frame_input, font=('Lucida Calligraphy', 12))
        self.entry_price.grid(row=1, column=1)

        tk.Label(frame_input, text="Jumlah: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=2, column=0, sticky=tk.W)
        self.entry_quantity = tk.Entry(frame_input, font=('Lucida Calligraphy', 12))
        self.entry_quantity.grid(row=2, column=1)

        self.add_button = tk.Button(frame_input, text="☕ Tambah Menu", command=self.add_item, bg='#d4a373', fg='white', font=('Lucida Calligraphy', 12, 'bold'))
        self.add_button.grid(row=3, column=1, pady=5, sticky=tk.W)
```

### Tombol Hapus Menu
   * Memungkinkan pengguna memilih item menu dalam tabel dan menghapusnya dengan mudah.
```python
        self.delete_button = tk.Button(frame_input, text="❌ Hapus Menu", command=self.delete_item, bg='#ff6347', fg='white', font=('Lucida Calligraphy', 12, 'bold'))
        self.delete_button.grid(row=4, column=1, pady=5, sticky=tk.W)
```

### Frame untuk Tabel Data
   * Menampilkan data menu yang telah dimasukkan dalam format tabel, lengkap dengan kolom untuk nama menu, harga, jumlah, dan total harga.
```python
       frame_table = tk.Frame(self.root, padx=10, pady=10, bg='#f8f4e3')
        frame_table.pack(fill=tk.BOTH, expand=True)

        self.table = ttk.Treeview(frame_table, columns=("Jumlah", "Nama", "Harga Satuan", "Harga Total"), show="headings")
        self.table.heading("Jumlah", text="Jumlah Menu")
        self.table.heading("Nama", text="Nama Menu")
        self.table.heading("Harga Satuan", text="Harga Satuan")
        self.table.heading("Harga Total", text="Harga Total")
        self.table.pack(fill=tk.BOTH, expand=True)
```
### Frame untuk Ringkasan
   * Menampilkan detail subtotal, pajak, biaya layanan, total tagihan, transfer, dan kembalian dalam format yang rapi.
```python
        frame_summary = tk.Frame(self.root, padx=10, pady=10, bg='#f3e5d8')
        frame_summary.pack(fill=tk.X)

        tk.Label(frame_summary, text="Total Harga Semua Menu: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=0, column=0, sticky=tk.W)
        self.total_price_label = tk.Label(frame_summary, text="Rp 0,00", font=('Lucida Calligraphy', 12, 'bold'), bg='#f3e5d8')
        self.total_price_label.grid(row=0, column=1, sticky=tk.W)

        tk.Label(frame_summary, text="Total Transfer: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=1, column=0, sticky=tk.W)
        self.entry_transfer = tk.Entry(frame_summary, font=('Lucida Calligraphy', 12))
        self.entry_transfer.grid(row=1, column=1)

        self.summary_button = tk.Button(frame_summary, text="💵 Hitung Total", command=self.calculate_summary, bg='#6a994e', fg='white', font=('Lucida Calligraphy', 12, 'bold'))
        self.summary_button.grid(row=2, column=1, pady=5, sticky=tk.W)

    def add_item(self):
        try:
            name = self.entry_name.get()
            if not name.strip():
                raise ValueError("Nama menu tidak boleh kosong.")
```
---

## *Logika dan Validasi Utama:*

### Mengambil Harga dan Menghapus Karakter Selain Angka dan Titik
   * Harga yang dimasukkan pengguna diolah agar hanya menyertakan angka dan karakter desimal untuk memastikan validitas input.
```python
 price = self.entry_price.get().replace(",", "").replace("Rp", "").strip()  # Menghapus koma dan simbol Rp
            if not price.replace(".", "").isdigit():  # Pastikan harga adalah angka yang valid
                raise ValueError("Harga harus berupa angka yang valid.")
            price = float(price)  # Mengubah harga menjadi float setelah valid
```

### Mengecek dan Memastikan Input Jumlah Adalah Angka
   * Validasi memastikan jumlah menu yang dimasukkan pengguna berupa angka valid.
```python
            quantity = self.entry_quantity.get().strip()
            if not quantity.isdigit():
                raise ValueError("Jumlah harus berupa angka yang valid.")
            quantity = int(quantity)

            self.data.add_item(name, price, quantity)
```

### Menghitung Total Harga per Item
   * Mengalikan harga satuan dengan jumlah item untuk mendapatkan total harga per menu.
```python
 total_price = price * quantity
            formatted_price = self.format_currency(price)  # Format harga satuan
            formatted_total = self.format_currency(total_price)  # Format harga total
            self.table.insert("", "end", values=(quantity, name, formatted_price, formatted_total))

            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
```

### Update Total Harga
   * Menambahkan total harga per item ke subtotal keseluruhan.
```python
            self.update_total_price()

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def format_currency(self, amount):
        """ Fungsi untuk memformat angka menjadi format mata uang Indonesia """
        return f"Rp {amount:,.0f}"

    def update_total_price(self):
        total_price = 0
        for item in self.table.get_children():
            total_price += float(self.table.item(item)["values"][3].replace("Rp", "").replace(",", "").strip())
```

### Tampilkan Total Harga Dalam Bagian Ringkasan
   * Menampilkan subtotal, pajak, biaya layanan, dan total tagihan di frame ringkasan.
```python
       self.total_price_label.config(text=self.format_currency(total_price))

    def delete_item(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Silakan pilih menu yang ingin dihapus.")
            return
```

### Ambil Data Harga Total dari Menu yang Dipilih
   * Memungkinkan pengguna memilih item menu dan mengambil total harga untuk penghapusan atau edit data.
```python
        item_values = self.table.item(selected_item)["values"]
        total_price = float(item_values[3].replace("Rp", "").replace(",", "").strip())
```

### Menghapus Item Dari Tabel
   * Menghapus item yang dipilih pengguna dari tabel menu.
```python
        self.table.delete(selected_item)
```

###  Mengupdate Total Harga Setelah Penghapusan
   * Mengurangi subtotal berdasarkan total harga item yang dihapus.
```python
        self.update_total_price()

        messagebox.showinfo("Sukses", f"Menu {item_values[1]} telah dihapus. Harga yang dihapus: {self.format_currency(total_price)}")

    def calculate_summary(self):
        try:
            process = Process(self.data)
            subtotal = process.calculate_subtotal()
            tax = process.calculate_tax(subtotal)
            service_charge = process.calculate_service_charge(subtotal)
            total = process.calculate_total(subtotal, tax, service_charge)

            transfer = float(self.entry_transfer.get())
            if transfer < total:
                raise ValueError("Jumlah transfer tidak mencukupi.")

            change = transfer - total
```

### Tampilkan Hasil Dalam Kotak Pesan
   * Ringkasan transaksi ditampilkan dalam kotak pesan menggunakan messagebox. Informasi meliputi subtotal, pajak, biaya layanan, total pembayaran, kembalian, tanggal, dan waktu transaksi.
```python
            date = datetime.now().strftime("%d/%m/%Y")
            time = datetime.now().strftime("%H:%M:%S")
            cashier = "Kasir 1"
            summary_message = (
                f"☕ Sub Total: {self.format_currency(subtotal)}\n"
                f"🛡 Pajak (10%): {self.format_currency(tax)}\n"
                f"🍴 Service (5%): {self.format_currency(service_charge)}\n"
                f"💵 Total Tagihan: {self.format_currency(total)}\n"
                f"💳 Transfer: {self.format_currency(transfer)}\n"
                f"🔄 Kembalian: {self.format_currency(change)}\n"
                f"🕒 Waktu Pembayaran: {time}\n"
                f"📅 Tanggal: {date}\n"
                "----------------------------------\n"
                "Harga sudah termasuk tax dan service\n"
                "Terimakasih sudah berkunjung di Eatplaylove Café\n"
                "Instagram: @eatplaylove_café\n"
                f"Terbayar: {date}\n"
                f"🧾 Dicetak oleh: {cashier}"
            )
            messagebox.showinfo("Ringkasan Transaksi", summary_message)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
```
---

## **Main Program**
   * File main.py menghubungkan semua modul, termasuk menginisialisasi GUI dan menjalankan aplikasi menggunakan tkinter.
```python
from tkinter import Tk
from data.data import Data
from view.viewGui import ViewGUI

if __name__ == "__main__":
    root = Tk()
    data = Data()
    app = ViewGUI(root, data)
    root.mainloop()
```
## **Cara Kerja Utama Aplikasi:**
   1. Input menu dilakukan melalui frame input.
   2. Data yang dimasukkan ditampilkan dalam tabel menu.
   3. Total harga, pajak, dan biaya layanan dihitung secara otomatis.
   4. Hasil transaksi dirangkum dalam frame ringkasan dan kotak pesan.

## **Cara Penggunaan:**
   1. Jalankan aplikasi menggunakan perintah python main.py.
   2. Isi nama menu, harga, dan jumlah di frame input.
   3. Klik Tambah untuk menambahkan item ke tabel.
   4. Total harga akan diperbarui secara otomatis.
   5. Klik item di tabel dan pilih "Hapus Menu" jika ingin menghapus item tertentu.
   6. Masukkan jumlah transfer dan klik "Hitung Total" untuk melihat total pembayaran dan kembalian, serta menampilkan ringkasan di kotak pesan.

## **Contoh Penggunaan:**

### Input Data:
|                 Nama Menu         | Harga | Jumlah |
| --------------------------------  | ----- | ------ |
| Nasi Bakar Sambal Padang          | 37,000|   2    |
| Sate Ayam                         | 52,000|   2    |
| Avocado Latte Ice                 | 33,000|   2    |
| Dimsum Salmon                     | 25,000|   2    |
| Soft Banana Choco Pudding         | 23,000|   2    |
|  Transfer                         | 400,000        |


 ### Hasil Tabel Output:
|Jumlah Menu|                 Nama Menu         |    Harga    |
|-----------| --------------------------------  | ------------|
|     2     | Nasi Bakar Sambal Padang          |Rp 74,000    |
|     2     | Sate Ayam                         |Rp 104,000   |
|     2     | Avocado Latte Ice                 |Rp 66,000    |
|     2     | Dimsum Salmon                     |Rp 50,000    |
|     2     | Soft Banana Choco Pudding         |Rp 46,000    | 


 ### Output Ringkasan:
* ☕ Sub Total: Rp 340,000
* 🛡 Pajak (10%): Rp 34,000
* 🍴 Service (5%): Rp 17,000
* 💵 Total Tagihan: Rp 391,000
* 💳 Transfer: Rp 400,000
* 🔄 Kembalian: Rp 9,000
* 🕒 Waktu Pembayaran: 07:48:43
* 📅 Tanggal: 04/01/2025
----------------------------------
* Harga sudah termasuk tax dan service
* Terimakasih sudah berkunjung di Eatplaylove Café
* Instagram: @eatplaylove_café
* Terbayar: 01/01/2025
* 📂 Dicetak oleh: Kasir 1

## **Terimakasih**
