def escape(room, y, x):
    # Cek batas
    if y < 0 or y >= len(room) or x < 0 or x >= len(room[0]):
        return False
    # Harus jalan (1)
    if room[y][x] != 1:
        return False
    # Jika mencapai baris 0 -> sukses
    if y == 0:
        room[y][x] = 2
        return True
    # Tandai jejak
    room[y][x] = 2
    # Lima arah: kiri, diag kiri-atas, diag kiri-bawah, atas, bawah
    moves = [
        (y-1, x),     # atas
        (y+1, x-1),   # diag kiri-bawah
        (y,   x-1),   # kiri
        (y-1, x-1),   # diag kiri-atas
        (y+1, x),     # bawah
    ]
    for ny, nx in moves:
        if escape(room, ny, nx):
            return True
    return False

# --- PROGRAM UTAMA ---
room = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
]

# Start dari pojok kanan bawah (Baris 3, Kolom 3)
start_y = 3
start_x = 3

print("START")
for r in room:
    print(r)

escape(room, start_y, start_x)

print("ESCAPE MAP")
for r in room:
    print(r)