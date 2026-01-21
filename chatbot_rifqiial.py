import os
from groq import Groq

# kode api key 
KODE_API_BARU = "Masukan api key"

try:
    client = Groq(api_key=KODE_API_BARU)

    laptop_data = """
KATEGORI OFFICE & KULIAH:
1. ASUS Vivobook 14 (Rp 6.500.000): Layar OLED, ringan, cocok untuk mahasiswa/admin.
2. Acer Aspire 5 (Rp 7.200.000): RAM mudah di-upgrade, cocok untuk multitasking ringan.
3. HP Laptop 14s (Rp 5.800.000): Harga terjangkau, desain tipis, cocok untuk ngetik tugas.

KATEGORI GAMING & CODING:
4. Lenovo Ideapad Gaming 3 (Rp 11.200.000): GPU RTX 3050, cocok untuk game menengah & coding.
5. ASUS TUF Gaming F15 (Rp 13.500.000): Awet/Military Grade, cocok untuk pemakaian berat.
6. Acer Predator Helios (Rp 21.000.000): Spek rata kanan, cocok untuk render 3D & video berat.

KATEGORI PROFESIONAL & DESAIN:
7. MacBook Air M2 (Rp 15.800.000): Baterai awet 18 jam, sangat tipis, cocok untuk desainer.
8. MacBook Pro M3 (Rp 25.000.000): Layar Liquid Retina, performa sangat cepat untuk editing video 4K.
9. ASUS Zenbook 14 (Rp 17.000.000): Premium, layar sentuh, cocok untuk eksekutif/profesional.
"""

    instruction = f"Anda adalah Laptop Expert. Gunakan data ini: {laptop_data}"

    print("\n=== BOT REKOMENDASI LAPTOP AKTIF ===")
    print("(Ketik 'keluar' untuk berhenti)\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['keluar', 'exit']:
            break

        # Bot Engine
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_input}
            ],
            model="llama-3.3-70b-versatile", # Model terbaru dan aktif
        )
        
        print(f"\nBot: {completion.choices[0].message.content}\n")

except Exception as e:
    print(f"\nTerjadi kesalahan sistem: {e}")