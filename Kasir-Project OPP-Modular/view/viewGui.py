import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from data.process import Process


class ViewGUI:
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.root.title("☕Eatplaylove Café☕ - Sistem Kasir ")
        self.root.geometry("800x600")
        self.root.configure(bg='#f8f4e3')

        self.total_price = 0  # Variable to keep track of the total price
        self.create_widgets()

    def create_widgets(self):
        # Nama Toko dengan font Renitah
        frame_title = tk.Frame(self.root, pady=10, bg='#f3e5d8')
        frame_title.pack(fill=tk.X)
        self.shop_name = tk.Label(frame_title, text="Eatplaylove Café ☕", font=('Renitah', 24, 'bold'), bg='#f3e5d8', fg='#e9967a')
        self.shop_name.pack()

        # Frame untuk Input Menu
        frame_input = tk.Frame(self.root, padx=10, pady=10, bg='#f3e5d8')
        frame_input.pack(fill=tk.X)

        tk.Label(frame_input, text="Nama Menu: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=0, column=0, sticky=tk.W)
        self.entry_name = tk.Entry(frame_input, font=('Lucida Calligraphy', 12))
        self.entry_name.grid(row=0, column=1)

        tk.Label(frame_input, text="Harga Satuan: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=1, column=0, sticky=tk.W)
        self.entry_price = tk.Entry(frame_input, font=('Lucida Calligraphy', 12))
        self.entry_price.grid(row=1, column=1)

        tk.Label(frame_input, text="Jumlah: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=2, column=0, sticky=tk.W)
        self.entry_quantity = tk.Entry(frame_input, font=('Lucida Calligraphy', 12))
        self.entry_quantity.grid(row=2, column=1)

        self.add_button = tk.Button(frame_input, text="☕ Tambah Menu", command=self.add_item, bg='#d4a373', fg='white', font=('Lucida Calligraphy', 12, 'bold'))
        self.add_button.grid(row=3, column=1, pady=5, sticky=tk.W)

        # Frame untuk Tabel Data
        frame_table = tk.Frame(self.root, padx=10, pady=10, bg='#f8f4e3')
        frame_table.pack(fill=tk.BOTH, expand=True)

        self.table = ttk.Treeview(frame_table, columns=("Jumlah", "Nama", "Harga", "Harga Satuan"), show="headings")
        self.table.heading("Jumlah", text="Jumlah Menu")
        self.table.heading("Nama", text="Nama Menu")
        self.table.heading("Harga", text="Harga Total")
        self.table.heading("Harga Satuan", text="Harga Satuan")
        self.table.pack(fill=tk.BOTH, expand=True)

        # Frame untuk Ringkasan
        frame_summary = tk.Frame(self.root, padx=10, pady=10, bg='#f3e5d8')
        frame_summary.pack(fill=tk.X)

        tk.Label(frame_summary, text="Total Transfer: ", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold')).grid(row=0, column=0, sticky=tk.W)
        self.entry_transfer = tk.Entry(frame_summary, font=('Lucida Calligraphy', 12))
        self.entry_transfer.grid(row=0, column=1)

        self.summary_button = tk.Button(frame_summary, text="💵 Hitung Total", command=self.calculate_summary, bg='#6a994e', fg='white', font=('Lucida Calligraphy', 12, 'bold'))
        self.summary_button.grid(row=1, column=1, pady=5, sticky=tk.W)

        # Label to show total price
        self.total_label = tk.Label(frame_summary, text="Total Harga: Rp 0,00", bg='#f3e5d8', font=('Lucida Calligraphy', 12, 'bold'))
        self.total_label.grid(row=2, column=1, sticky=tk.W, pady=5)

    def add_item(self):
        try:
            name = self.entry_name.get()
            if not name.strip():
                raise ValueError("Nama menu tidak boleh kosong.")

            price = float(self.entry_price.get())  # Harga satuan
            quantity = int(self.entry_quantity.get())

            # Calculate the total price for the current item (unit price * quantity)
            total_item_price = price * quantity
            self.total_price += total_item_price

            # Insert item into the table
            self.table.insert("", "end", values=(quantity, name, f"Rp {total_item_price:,.2f}", f"Rp {price:,.2f}"))

            # Update the total price label
            self.total_label.config(text=f"Total Harga: Rp {self.total_price:,.2f}")

            # Clear the input fields
            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def calculate_summary(self):
        try:
            process = Process(self.data)
            subtotal = self.total_price  # Use the total price directly
            tax = process.calculate_tax(subtotal)
            service_charge = process.calculate_service_charge(subtotal)
            total = process.calculate_total(subtotal, tax, service_charge)

            transfer = float(self.entry_transfer.get())
            if transfer < total:
                raise ValueError("Jumlah transfer tidak mencukupi.")

            change = transfer - total

            # Tampilkan hasil dalam kotak pesan
            date = datetime.now().strftime("%d/%m/%Y")
            time = datetime.now().strftime("%H:%M:%S")
            cashier = "Kasir 1"
            summary_message = (
                f"☕ Sub Total: Rp {subtotal:,.2f}\n"
                f"🛡 Pajak (10%): Rp {tax:,.2f}\n"
                f"🍴 Service (5%): Rp {service_charge:,.2f}\n"
                f"💵 Total Tagihan: Rp {total:,.2f}\n"
                f"💳 Transfer: Rp {transfer:,.2f}\n"
                f"🔄 Kembalian: Rp {change:,.2f}\n"
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
