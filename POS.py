
#   LEVENSHTEIN DISTANCE 
def levenshtein(a, b):
    m, n = len(a), len(b) 
    dp = [[0]*(n+1) for _ in range(m+1)] 

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                cost = 0
            else: 
                cost = 1

            dp[i][j] = min(
                dp[i-1][j] + 1,      # delete
                dp[i][j-1] + 1,      # insert
                dp[i-1][j-1] + cost  # substitute
            )

    return dp[m][n]


def cari_produk(input_user, database_produk, limit=3):
    skor = []
    for nama_produk in database_produk.keys():  
        distance = levenshtein(input_user.lower(), nama_produk.lower())
        # prefix matching case
        if nama_produk.startswith(input_user):
            skor.append((nama_produk, 0)) # kalau 0 artinya kata depannya sama
            continue
        skor.append((nama_produk, distance))
            
    skor.sort(key=lambda x: x[1]) # urutkan berdasarkan distance levenshtein
    return skor[:limit]

#   GREEDY ALGORITHM UNTUK KEMBALIAN

def kembalian_greedy(jumlah, pecahan):
    hasil = {}
    for uang in sorted(pecahan, reverse=True): #descending 
        if jumlah >= uang:
            banyak = jumlah // uang # hitung berapa lembar pecahan uangnya
            hasil[uang] = banyak
            jumlah -= uang * banyak # kurangi total yang sudah diberikan
    return hasil

produk = {
    "Aqua":7800,
    "Coca Cola":12000,
    "Sprite":10000,
    "Fanta": 13000,
    "Yakult": 3600,
    "Gulaku": 14000,
    "Teh Pucuk": 3500,
    "Indomie Goreng": 3700,
    "Beras": 65000,
    "Sari Roti":10000
}
keranjang = []

while True:
    print("=== POINT OF SALE ===\n")
    print("List Produk : ")
    print(f"{'Produk':-<{25}} Harga")



    for key, value in produk.items():
        print(f"{key:.<{25}} {value}")
    # Langkah 1: Kasir mengetik nama produk
    input_user = input("Masukkan nama produk: ")

    # Langkah 2: Dapatkan rekomendasi berdasarkan search
    rekomendasi = cari_produk(input_user, produk)

    print("\nRekomendasi Produk:")
    for idx, (nama, dist) in enumerate(rekomendasi, start=1):
        print(f"{idx}. {nama} (distance: {dist})")

    # Langkah 3: Pilih produk dari hasil rekomendasi
    pilihan = int(input("\nPilih nomor produk: "))
    nama_produk = rekomendasi[pilihan - 1][0]
    harga_produk = produk[nama_produk]

    print(f"\nAnda memilih: {nama_produk}")
    print(f"Harga: Rp{harga_produk}\n")
    keranjang.append(nama_produk)

    print("Keranjang ada sekarang berisi : ")
    total = 0
    for i in keranjang:
        total += produk[i]
        print(f"{i:.<{25}} 1x Rp{produk[i]}")

    print(f"Total Harga : {total}")
    lagi = input("Tambah lagi (Y/N) ? ")
    if lagi.lower() == "n":
        break

# Langkah 4: Input uang pembayaran
bayar = int(input("Uang dibayarkan: Rp"))

if bayar < harga_produk:
    print("Uang tidak cukup!")
else:
    kembali = bayar - harga_produk
    print(f"Total kembalian: Rp{kembali}")

    pecahan = [10000, 5000, 2000, 1000, 500, 200, 100] #uang pecahan yang ada di kasir

    rincian = kembalian_greedy(kembali, pecahan)

    print("\nRincian kembalian:")
    for nominal, jumlah in rincian.items():
        print(f"{jumlah} lembar/keping Rp{nominal}")