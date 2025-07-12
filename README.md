![Banner](assets/banner.png)

# 🧠 Trigram-Based Next Word Prediction

This project builds a simple **next-word prediction system** using **trigrams**, a type of n-gram where predictions are made based on the **previous three words**. The model uses only **Python standard libraries**, making it lightweight, fast, and easy to run.

---

## 📘 What is an N-Gram?

An **n-gram** is a sequence of `n` consecutive words in a text. For example:

- **Unigram (1-gram)** → `["the", "cat", "sat"]`
- **Bigram (2-gram)** → `[("the", "cat"), ("cat", "sat")]`
- **Trigram (3-gram)** → `[("the", "cat", "sat")]`

In this project, we use **trigrams** to predict the next word based on a 3-word input.

---

## 📁 Project Structure

| File                | Description                                     |
|---------------------|-------------------------------------------------|
| `data.txt`          | Input text data used to train the model         |
| `train_ngram.py`    | Script that builds and saves the trigram model  |
| `trigram_model.pkl` | Auto-generated model file after training        |
| `test_ngram.py`     | Loads the model and predicts the next word      |
| `README.md`         | Project documentation                           |

---

## ⚙️ How the Model Works

### 1. `train_ngram.py` – Training Phase

- Loads and reads text from `data.txt`
- Cleans and tokenizes the text into words
- Builds a trigram dictionary mapping each 3-word sequence to its most likely next word
- Saves the trained model as `trigram_model.pkl`

### 2. `test_ngram.py` – Prediction Phase

- Loads the saved model from `trigram_model.pkl`
- Prompts the user to enter a 3-word phrase
- If the phrase exists in training data, it predicts the most frequent next word

---

## 🚀 How to Run the Project

### ✅ Step 1: Prepare Training Data

Edit the `data.txt` file with training text, e.g.:
the sun is shining and the sky is blue
she wore her favorite dress to the party
we are going to the market today


---

### ✅ Step 2: Train the Model

```bash
python train_ngram.py
```
### ✅ Step 3: Predict the Next Word
```bash
python test_ngram.py
```
### Output
```bash
Enter 3 words: she wore her
Predicted next word: favorite
```
### 📦 Dependencies
Python 3.12.x
No external libraries (only built-in modules: pickle, re, collections)

### 🛠️ Future Improvements
Add smoothing techniques to handle unseen trigrams

Fallback to bigram/unigram if trigram not found

Create a web interface using Flask or Streamlit

Add functionality for uploading training text dynamically

### 🙋‍♂️ Author
Om Kasture
Intern at EmpowerYou Technologies
GitHub • LinkedIn

