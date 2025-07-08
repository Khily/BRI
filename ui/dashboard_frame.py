# File: ui/dashboard_frame.py
# Berisi UI untuk halaman utama/dashboard yang dilihat oleh User Guest. (Versi Desain Final)

import customtkinter
from PIL import Image
import os
import database as db # Diperlukan untuk get_base_path
import logging

class DashboardFrame(customtkinter.CTkFrame):
    def __init__(self, master, explore_callback, **kwargs):
        super().__init__(master, **kwargs)
        
        self.explore_callback = explore_callback # Fungsi untuk pindah ke halaman item
        self.configure(fg_color="#F8F9FA") # Warna latar yang lebih lembut dan modern

        # Konfigurasi grid agar konten bisa di-scroll
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Buat frame utama yang bisa di-scroll
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, fg_color="transparent", border_width=0)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # --- 1. Hero Banner ---
        self.create_hero_banner()

        # --- 2. Penjelasan Cara Kerja ---
        self.create_how_it_works_section()

    def get_asset_path(self, *paths):
        """Helper untuk mendapatkan path absolut ke folder assets."""
        return os.path.join(db.get_base_path(), "assets", *paths)

    def create_hero_banner(self):
        """Membuat bagian banner promosi di bagian atas dengan desain baru."""
        banner_container = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        banner_container.grid(row=0, column=0, sticky="ew", padx=30, pady=20)
        banner_container.grid_columnconfigure(0, weight=1)

        banner_frame = customtkinter.CTkFrame(banner_container, fg_color="#F8F9FA", corner_radius=20, border_width=1, border_color="#F8F9FA")
        banner_frame.pack(fill="both", expand=True)
        
        banner_frame.grid_rowconfigure(0, weight=1)
        banner_frame.grid_columnconfigure(0, weight=1)
        
        try:
            # --- LANGKAH 1: Muat gambar Anda ---
            # Pastikan file 'banner.png' ada di path yang benar.
            # Ganti ukuran (width, height) sesuai dengan kebutuhan banner Anda.
            banner_image = customtkinter.CTkImage(
                light_image=Image.open(self.get_asset_path("banner.png")),
                dark_image=Image.open(self.get_asset_path("banner.png")),
                size=(1000, 350)  # <-- SESUAIKAN UKURAN INI
            )

            # --- LANGKAH 2: Buat Label untuk menampilkan gambar ---
            # Label ditempatkan di dalam 'banner_frame'.
            image_label = customtkinter.CTkLabel(banner_frame, image=banner_image, text="")
            
            # --- LANGKAH 3: Tempatkan label agar mengisi seluruh frame ---
            # .pack() akan membuat label mengisi seluruh ruang di dalam banner_frame.
            image_label.pack(fill="both", expand=True)

        except Exception as e:
            logging.error(f"Gagal memuat gambar banner: {e}")
            # Fallback jika gambar tidak ditemukan, tampilkan frame biru saja
            banner_frame.configure(fg_color="#297AB9")
            fallback_label = customtkinter.CTkLabel(banner_frame, text="Gambar banner tidak ditemukan", text_color="white")
            fallback_label.pack(expand=True)


    def create_how_it_works_section(self):
        """Membuat bagian 'Bagaimana BRI INV Bekerja?' dengan desain baru."""
        works_container = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        works_container.grid(row=1, column=0, sticky="ew", padx=30, pady=(40, 60))
        works_container.grid_columnconfigure(0, weight=1)

        # Canvas untuk menampung gambar garis dan kartu langkah
        image_frame = customtkinter.CTkFrame(works_container, fg_color="transparent", corner_radius=20)
        image_frame.pack(fill="both", expand=True)
        
        # Gambar garis sebagai latar belakang
        try:
            # --- LANGKAH 1: Muat gambar 'banner2.png' ---
            # Ganti ukuran (width, height) agar sesuai dengan desain Anda.
            banner_image = customtkinter.CTkImage(
                light_image=Image.open(self.get_asset_path("banner2.png")),
                dark_image=Image.open(self.get_asset_path("banner2.png")),
                size=(900, 350)  # <-- SESUAIKAN UKURAN INI JIKA PERLU
            )

            # --- LANGKAH 2: Tampilkan gambar dalam sebuah Label ---
            # Label ditempatkan di dalam 'image_frame' agar bentuknya mengikuti.
            image_label = customtkinter.CTkLabel(image_frame, image=banner_image, text="")
            
            # --- LANGKAH 3: Pastikan gambar mengisi seluruh area frame ---
            image_label.pack(fill="both", expand=True)

        except Exception as e:
            logging.error(f"Gagal memuat gambar 'banner2.png': {e}")
            # Fallback jika gambar tidak ditemukan, tampilkan frame abu-abu.
            image_frame.configure(fg_color="#F3F4F6", border_width=1, border_color="#E5E7EB")
            fallback_label = customtkinter.CTkLabel(
                image_frame, 
                text="Gambar 'Bagaimana BRI INV Bekerja?' tidak ditemukan", 
                text_color="#4B5563"
            )
            fallback_label.pack(expand=True)

    def create_step_card(self, parent, column, icon_name, title, description, color, is_highlighted):
        """Membuat satu kartu untuk langkah-langkah cara kerja dengan desain baru."""
        
        card_fg = "#FFFFFF" if is_highlighted else "transparent"
        card_border_width = 1 if is_highlighted else 0
        
        card_container = customtkinter.CTkFrame(parent, fg_color='transparent')
        card_container.grid(row=0, column=column, sticky='s' if is_highlighted else 'n', padx=10, pady=(20 if is_highlighted else 60))

        card = customtkinter.CTkFrame(card_container, fg_color=card_fg, corner_radius=15, border_width=card_border_width, border_color="#E5E7EB")
        card.pack()
        
        icon_frame = customtkinter.CTkFrame(card, fg_color=color, corner_radius=30, width=64, height=64)
        icon_frame.pack(padx=20, pady=(20, 15))
        icon_frame.grid_propagate(False)
        icon_frame.grid_columnconfigure(0, weight=1)
        icon_frame.grid_rowconfigure(0, weight=1)

        try:
            icon_img = customtkinter.CTkImage(Image.open(self.get_asset_path("icons", icon_name)), size=(32, 32))
            customtkinter.CTkLabel(icon_frame, image=icon_img, text="").grid(row=0, column=0)
        except Exception as e:
            logging.warning(f"Ikon langkah '{icon_name}' tidak ditemukan: {e}")
            customtkinter.CTkLabel(icon_frame, text="?", font=("Inter", 24)).grid(row=0, column=0)
        
        text_frame = customtkinter.CTkFrame(card, fg_color="transparent")
        text_frame.pack(padx=20, pady=(0, 20), fill="x")

        customtkinter.CTkLabel(text_frame, text=title, font=customtkinter.CTkFont(family="Inter", size=18, weight="bold"), text_color="#111827").pack(pady=(0, 8))
        customtkinter.CTkLabel(text_frame, text=description, wraplength=220, justify="center", text_color="#6B5D5D", font=("Inter", 14)).pack()
