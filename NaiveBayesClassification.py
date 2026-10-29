import numpy as np
reviews = [
    "kamar sangat bersih dan bagus",             # Positif
    "pelayanan lambat dan mengecewakan",          # Negatif
    "lokasi strategis tapi harga terlalu mahal",  # Netral
    "semuanya sempurna, hotel terbaik",           # Positif
    "agak kotor, staff ramah",                    # Netral (campuran)
    "sarapan enak, sangat puas",                  # Positif
    "air panas tidak berfungsi",                  # Negatif
    "biasa saja, tidak ada yang spesial",        # Netral
    "staff cepat tanggap dan profesional",        # Positif
    "wifi lemot sekali, kamar sempit",            # Negatif
    "view bagus, tapi kasur kurang nyaman",       # Netral
    "sangat direkomendasikan",                    # Positif
    "malam berisik, tidak bisa tidur",            # Negatif
    "cukup baik dengan harga segitu",             # Netral
    "terima kasih atas keramahan anda"            # Positif
]
labels = np.array([
    1, 0, 2, 1, 2,
    1, 0, 2, 1, 0,
    2, 1, 0, 2, 1
])


def preprocess_text(text):
    return text.lower().split()
vocabulary = set()
for review in reviews:
    words = preprocess_text(review)
    vocabulary.update(words)

vocab_list = list(vocabulary)
vocab_size = len(vocab_list)
num_reviews = len(reviews)
num_classes = 3 # 0 (Negatif), 1 (Positif), 2 (Netral)

print(f"Total kata unik (Vocabulary Size): {vocab_size}")
prior_prob = np.zeros(num_classes)

for c in range(num_classes):
    # Hitung jumlah ulasan untuk setiap kelas dan bagi dengan total ulasan
    count_c = np.sum(labels == c)
    prior_prob[c] = count_c / num_reviews

print(f"\nPrior Probability (P(C)): {prior_prob}")

word_counts = np.zeros((num_classes, vocab_size))

for i, review in enumerate(reviews):
    class_label = labels[i]
    words = preprocess_text(review)

    #mengambil kata dari kalimat
    for word in words:
        if word in vocab_list:
            word_index = vocab_list.index(word)
            word_counts[class_label, word_index] += 1
likelihood_prob = np.zeros((num_classes, vocab_size))

for c in range(num_classes):
    # Total kata di kelas C
    total_words_in_class = np.sum(word_counts[c, :])

    # Penerapan rumus smoothing
    likelihood_prob[c, :] = (word_counts[c, :] + 1) / (total_words_in_class + vocab_size)

print("\nLikelihood Probability (P(W|C)) berhasil dihitung.")
LABEL_MAP = {
    0: "Negatif",
    1: "Positif",
    2: "Netral"
}

def predict_sentiment(review_text):
    """
    Memprediksi sentimen ulasan baru berdasarkan model Naive Bayes yang dilatih.
    """
    # 1. Preprocessing ulasan baru
    words_in_review = preprocess_text(review_text)

    # Inisialisasi skor log untuk setiap kelas (sentimen)
    # Skor ini adalah P(C) * P(w1|C) * P(w2|C) ... dalam bentuk log untuk setiap kelas
    log_scores = np.zeros(num_classes)

    # Looping untuk setiap kelas (c = 0, 1, 2)
    for c in range(num_classes):
        # Mulai dengan log Prior Probability log(P(C))
        log_score = np.log(prior_prob[c])

        # Iterasi melalui setiap kata dalam ulasan baru
        for word in words_in_review:
            if word in vocab_list:
                # Jika kata ada di vocabulary
                word_index = vocab_list.index(word)
                # Ambil Likelihood P(W|C) dan tambahkan log-nya ke skor
                log_score += np.log(likelihood_prob[c, word_index])
            else:
                # Jika kata TIDAK ada di vocabulary (kata baru),
                # kita harus menggunakan Laplace Smoothing juga.
                # P(w|C) untuk kata baru adalah (0 + 1) / (Total Kata di C + Vocab Size)
                # Kita harus menghitung ulang denominator dari P(W|C)
                total_words_in_class = np.sum(word_counts[c, :]) #berapa kali kata muncul di kelas c
                prob_new_word = 1 / (total_words_in_class + vocab_size)
                log_score += np.log(prob_new_word)

        log_scores[c] = log_score

    # Ambil indeks (label 0, 1, atau 2) dengan skor log tertinggi
    predicted_label = np.argmax(log_scores)

    return LABEL_MAP[predicted_label], log_scores

### 4. UJI COBA DAN OUTPUT HASIL ###

# Uji beberapa ulasan baru:
ulasan_1 = "staf sangat ramah dan kamar bersih" # Harusnya Positif
ulasan_2 = "kamar kotor dan lambat sekali"      # Harusnya Negatif
ulasan_3 = "harga oke tapi tidak ada tv"        # Harusnya Netral

hasil_1, skor_1 = predict_sentiment(ulasan_1)
hasil_2, skor_2 = predict_sentiment(ulasan_2)
hasil_3, skor_3 = predict_sentiment(ulasan_3)


print("\n--- HASIL PREDIKSI ---")
print(f"Ulasan 1: '{ulasan_1}'")
print(f"-> Prediksi: {hasil_1}")
# print(f"   Skor Log: {skor_1}") # Opsional untuk debugging

print(f"\nUlasan 2: '{ulasan_2}'")
print(f"-> Prediksi: {hasil_2}")

print(f"\nUlasan 3: '{ulasan_3}'")
print(f"-> Prediksi: {hasil_3}")