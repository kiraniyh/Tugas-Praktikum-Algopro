# Modul display.py

def print_result(principal, rate, years, ci, si):
    print(f"\n==== Hasil Perhitungan Tabungan ====")
    print(f"Saldo Awal            : ¥{principal:,.0f}")
    print(f"Bunga Tahunan         : {rate * 100}%")
    print(f"Lama Menabung         : {years} tahun")
    print(f"Nilai Akhir (Majemuk) : ¥{ci:,.2f}")
    print(f"Nilai Akhir (Sederhana): ¥{si:,.2f}")