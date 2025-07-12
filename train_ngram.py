import pickle
from collections import defaultdict, Counter

with open("data.txt", "r", encoding="utf8") as f:
    text = f.read().lower().replace('\n', ' ').split()

trigrams = defaultdict(Counter)
for i in range(len(text) - 3):
    key = tuple(text[i:i+3])
    next_word = text[i+3]
    trigrams[key][next_word] += 1

with open("trigram_model.pkl", "wb") as f:
    pickle.dump(trigrams, f)

print("Trigram model trained and saved as trigram_model.pkl")