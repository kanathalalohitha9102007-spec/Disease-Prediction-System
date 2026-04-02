import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
data = {
    "message": [
        "Win money now!!! Click here",
        "Congratulations you have won lottery",
        "Call me later",
        "Hey how are you",
        "Free entry in contest!!!",
        "Important update from your bank",
        "You have been selected for prize",
        "Let's meet tomorrow"
    ],
    "label": [1, 1, 0, 0, 1, 1, 1, 0]  # 1 = Spam, 0 = Ham
}

df = pd.DataFrame(data)
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")