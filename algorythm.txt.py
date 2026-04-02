1. Start

2. Import required libraries
   - Streamlit
   - Pandas
   - Scikit-learn (TF-IDF, Naive Bayes)

3. Load or create dataset containing messages and labels
   - Label = 1 (Spam/Scam)
   - Label = 0 (Safe/Ham)

4. Preprocess the text data
   - Convert text to lowercase
   - Remove special characters (optional)
   - Tokenize text (optional)

5. Convert text into numerical form
   - Use TF-IDF Vectorizer

6. Train Machine Learning model
   - Use Multinomial Naive Bayes algorithm

7. Save trained model and vectorizer (optional for separate backend)

8. Build Streamlit User Interface
   - Display title and description
   - Create input text area
   - Add "Analyze Message" button

9. Accept user input message

10. Transform input using trained TF-IDF vectorizer

11. Predict output using trained model

12. Display result:
    - If prediction = 1 → Show "Spam/Scam"
    - If prediction = 0 → Show "Safe Message"

13. (Optional Enhancements)
    - Show confidence score
    - Detect suspicious keywords

14. End