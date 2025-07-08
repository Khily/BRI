# File: ui/admin_dashboard_frame.py
# Berisi UI untuk halaman dashboard yang dilihat oleh User Admin,
# dengan layout yang mirip Dashboard Guest.

import customtkinter
from PIL import Image
import os
import database as db
import logging

class AdminDashboardFrame(customtkinter.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)
        
        self.app = app  # Simpan referensi ke instance App utama
        self.configure(fg_color="#F8F9FA")

        # Konfigurasi grid agar konten bisa di-scroll
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Buat frame utama yang bisa di-scroll
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, fg_color="transparent", border_width=0)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Panggil semua fungsi untuk membuat setiap bagian secara berurutan
        self.create_summary_section()      # Akan ditempatkan di row=0
        self.create_actions_section()      # Akan ditempatkan di row=1
        self.create_hero_banner()          # Akan ditempatkan di row=2
        self.create_how_it_works_section() # Akan ditempatkan di row=3

    def get_asset_path(self, *paths):
        """Fungsi bantuan untuk mendapatkan path absolut ke folder assets."""
        return os.path.join(db.get_base_path(), "assets", *paths)
        
    def create_summary_section(self):
        """Membuat bagian ringkasan statistik di bagian atas."""
        summary_container = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        # Menempati baris pertama
        summary_container.grid(row=0, column=0, sticky="ew", padx=30, pady=20)
        summary_container.grid_columnconfigure(0, weight=1)

        summary_frame = customtkinter.CTkFrame(summary_container, fg_color="#FFFFFF", corner_radius=20, border_width=1, border_color="#E5E7EB")
        summary_frame.pack(fill="both", expand=True, ipady=20)
        
        welcome_label = customtkinter.CTkLabel(summary_frame, text="Ringkasan Inventaris", font=customtkinter.CTkFont(family="Inter", size=24, weight="bold"))
        welcome_label.pack(pady=(15, 20))

        stats_frame = customtkinter.CTkFrame(summary_frame, fg_color="transparent")
        stats_frame.pack(fill="x", expand=True, padx=30)
        stats_frame.grid_columnconfigure((0, 1, 2), weight=1)

        frame_1 = customtkinter.CTkFrame(stats_frame, fg_color="transparent")
        frame_1.grid(row=0, column=0)
        customtkinter.CTkLabel(frame_1, text="Total Barang", font=("Inter", 16)).pack()
        self.total_items_label = customtkinter.CTkLabel(frame_1, text="0", font=("Inter", 48, "bold"), text_color="#3B82F6")
        self.total_items_label.pack()
        
        frame_2 = customtkinter.CTkFrame(stats_frame, fg_color="transparent")
        frame_2.grid(row=0, column=1)
        customtkinter.CTkLabel(frame_2, text="Total Kategori", font=("Inter", 16)).pack()
        self.total_categories_label = customtkinter.CTkLabel(frame_2, text="0", font=("Inter", 48, "bold"), text_color="#10B981")
        self.total_categories_label.pack()

        frame_3 = customtkinter.CTkFrame(stats_frame, fg_color="transparent")
        frame_3.grid(row=0, column=2)
        customtkinter.CTkLabel(frame_3, text="Stok Hampir Habis", font=("Inter", 16)).pack()
        self.low_stock_label = customtkinter.CTkLabel(frame_3, text="0", font=("Inter", 48, "bold"), text_color="#EF4444")
        self.low_stock_label.pack()
        
        # Panggil refresh data setelah label dibuat
        self.refresh_data()

    def create_actions_section(self):
        """Membuat bagian untuk tombol aksi cepat."""
        actions_container = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        # Menempati baris kedua
        actions_container.grid(row=1, column=0, sticky="ew", padx=30, pady=(20, 40))
        actions_container.grid_columnconfigure(0, weight=1)

        actions_frame = customtkinter.CTkFrame(actions_container, fg_color="#FFFFFF", corner_radius=20, border_width=1, border_color="#E5E7EB")
        actions_frame.pack(fill="both", expand=True, ipady=20)
        
        actions_header = customtkinter.CTkLabel(actions_frame, text="Akses Cepat", font=customtkinter.CTkFont(family="Inter", size=24, weight="bold"))
        actions_header.pack(pady=(15, 20))

        buttons_frame = customtkinter.CTkFrame(actions_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", expand=True, padx=30, pady=20)
        buttons_frame.grid_columnconfigure((0, 1), weight=1)

        manage_button = customtkinter.CTkButton(buttons_frame, text="📊 Kelola Barang", height=60, font=customtkinter.CTkFont(size=18, weight="bold"), command=lambda: self.app.select_frame_by_name("management"))
        manage_button.grid(row=0, column=0, padx=15, sticky="ew")

        history_button = customtkinter.CTkButton(buttons_frame, text="📜 Lihat Riwayat", height=60, font=customtkinter.CTkFont(size=18, weight="bold"), command=lambda: self.app.select_frame_by_name("history"))
        history_button.grid(row=0, column=1, padx=15, sticky="ew")
        
    def create_hero_banner(self):
        """Membuat bagian banner di bawah 'Akses Cepat'."""
        banner_container = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        # --- PERUBAHAN DI SINI: Menjadi baris ketiga ---
        banner_container.grid(row=2, column=0, sticky="ew", padx=30, pady=20)
        banner_container.grid_columnconfigure(0, weight=1)

        banner_frame = customtkinter.CTkFrame(banner_container, fg_color="#F8F9FA", corner_radius=20, border_width=1, border_color="#F8F9FA")
        banner_frame.pack(fill="both", expand=True)
        
        try:
            banner_image = customtkinter.CTkImage(light_image=Image.open(self.get_asset_path("banner.png")), dark_image=Image.open(self.get_asset_path("banner.png")), size=(1000, 350))
            image_label = customtkinter.CTkLabel(banner_frame, image=banner_image, text="")
            image_label.pack(fill="both", expand=True)
        except Exception as e:
            logging.error(f"Gagal memuat gambar banner: {e}")
            banner_frame.configure(fg_color="#297AB9")
            fallback_label = customtkinter.CTkLabel(banner_frame, text="Gambar banner tidak ditemukan", text_color="white")
            fallback_label.pack(expand=True)

    def create_how_it_works_section(self):
        """Membuat bagian 'Bagaimana BRI INV Bekerja?' di bagian paling bawah."""
        works_container = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        # --- PERUBAHAN DI SINI: Menjadi baris keempat ---
        works_container.grid(row=3, column=0, sticky="ew", padx=30, pady=(40, 60))
        works_container.grid_columnconfigure(0, weight=1)

        image_frame = customtkinter.CTkFrame(works_container, fg_color="transparent", corner_radius=20)
        image_frame.pack(fill="both", expand=True)
        
        try:
            banner_image = customtkinter.CTkImage(light_image=Image.open(self.get_asset_path("cara.png")), dark_image=Image.open(self.get_asset_path("cara.png")), size=(900, 350))
            image_label = customtkinter.CTkLabel(image_frame, image=banner_image, text="")
            image_label.pack(fill="both", expand=True)
        except Exception as e:
            logging.error(f"Gagal memuat gambar 'cara.png': {e}")
            image_frame.configure(fg_color="#F3F4F6", border_width=1, border_color="#E5E7EB")
            fallback_label = customtkinter.CTkLabel(image_frame, text="Gambar 'Bagaimana BRI INV Bekerja?' tidak ditemukan", text_color="#4B5563")
            fallback_label.pack(expand=True)

    def refresh_data(self):
        """Mengambil data terbaru dan memperbarui UI."""
        try:
            total_items = db.get_total_items_count()
            total_categories = db.get_total_categories_count()
            low_stock_count = db.get_low_stock_items_count(threshold=5)

            self.total_items_label.configure(text=str(total_items))
            self.total_categories_label.configure(text=str(total_categories))
            self.low_stock_label.configure(text=str(low_stock_count))
        except Exception as e:
            logging.error(f"Gagal merefresh data di AdminDashboard: {e}")