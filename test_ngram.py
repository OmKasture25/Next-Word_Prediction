import pickle

with open("trigram_model.pkl", "rb") as f:
    trigrams = pickle.load(f)

def predict_next(word1, word2, word3):
    key = (word1.lower(), word2.lower(), word3.lower())
    if key in trigrams:
        prediction = trigrams[key].most_common(1)[0][0]
        return prediction
    else:
        return "Pattern not found."

print(" Trigram Next Word Predictor")
print("Enter a 3-word phrase from training data. Type '1' to exit.\n")

while True:
    text = input("Enter 3 words: ").strip()
    if text == "1":
        print(" Exiting.")
        break

    words = text.split()
    if len(words) != 3:
        print(" Please enter exactly 3 words.")
        continue

    print("→ Predicted next word:", predict_next(*words))