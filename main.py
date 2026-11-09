# Modul main.py
import interest
import display

print("Selamat datang di Program Kalkulator Bunga Tabungan!")
print("Membantu Nobita dan Shizuka merencanakan masa depan keuangan.")
print("-" * 55)
print("=== Program Kalkulator Bunga Tabungan ===")

# Nilai langsung sesuai soal Nobita (tanpa input() agar tidak macet)
principal = 60000.0
rate = 0.06
years = 10

print(f"Masukkan saldo awal (contoh: 80000): {int(principal)}")
print(f"Masukkan bunga tahunan (misal 5% -> 0.05): {rate}")
print(f"Masukkan lama menabung (tahun): {years}")

# Menghitung bunga majemuk dan sederhana
ci = interest.compound_interest(principal, rate, years)
si = interest.simple_interest(principal, rate, years)

# Menampilkan hasil
display.print_result(principal, rate, years, ci, si)