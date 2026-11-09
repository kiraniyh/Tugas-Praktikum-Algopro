# Modul interest.py

def compound_interest(principal, rate, years):
    # Rumus: A = P * (1 + r)^t
    amount = principal * ((1 + rate) ** years)
    return amount

def simple_interest(principal, rate, years):
    # Rumus: Bunga Sederhana (Total Nilai Akhir) = P + (P * r * t) atau P * (1 + r * t)
    # Sesuaikan dengan rumus umum praktikum alpro:
    amount = principal + (principal * rate * years)
    return amount