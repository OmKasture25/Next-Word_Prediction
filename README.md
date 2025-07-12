![Banner](assets/banner.png)

# 🧠 Trigram-Based Next Word Prediction

This project builds a simple **next-word prediction system** using **trigrams**, a type of n-gram where predictions are made based on the **previous three words**. The model uses only **Python standard libraries**, making it lightweight and easy to run.

---

## 📘 What is an N-Gram?

An **n-gram** is a sequence of `n` consecutive words in a text.

- **Unigram (1-gram)** → `["the", "cat", "sat"]`
- **Bigram (2-gram)** → `[("the", "cat"), ("cat", "sat")]`
- **Trigram (3-gram)** → `[("the", "cat", "sat")]`

In this project, we use **trigrams** to predict the next word after a 3-word input.

---

## 📁 Project Structure

| File                | Description                                     |
|---------------------|-------------------------------------------------|
| `data.txt`          | Input text data used to train the model         |
| `train_ngram.py`          | Script that builds and saves the trigram model  |
| `trigram_model.pkl` | Auto-generated model file after training        |
| `test_ngram.py`           | Loads the model and predicts the next word      |
| `README.md`         | Project documentation                           |

---

## ⚙️ How the Model Works

### 1. `train.py` – Training Phase

- Loads and reads text from `data.txt`
- Cleans and tokenizes the text into words
- Builds a trigram dictionary mapping to the next word
- Saves the trained model as `trigram_model.pkl`

### 2. `test.py` – Prediction Phase

- Loads the model from `trigram_model.pkl`
- Prompts user for a 3-word phrase
- If the phrase exists in training data, predicts the next word

---

## 🚀 Steps to Run the Project

### Step 1: Prepare Training Data

Edit `data.txt` with your training phrases, like:

the sun is shining and the sky is blue
she wore her favorite dress to the party
we are going to the market today

---

### Step 2: Train the Model

```bash
Step 3: Predict Next Word

python test.py
Then enter 3 words:

Enter 3 words: she wore her
Predicted next word: favorite
📦 Dependencies
Python 3.x

No external libraries required

🛠️ Future Improvements
Add smoothing for unseen phrases

Fallback to bigram or unigram if no trigram match found

Add a web interface (Flask or Streamlit)

🙋‍♂️ Author
Om Kasture
Intern at EmpowerYou Technologies
GitHub • LinkedIn