import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
import streamlit as st
import numpy as np

# App title
st.title("🎥 Movie Review Sentiment Analysis App")

# Load the trained Random Forest model and vectorizer
try:
    rf_model = pk.load(open('rf_model.pkl', 'rb'))
    vectorizer = pk.load(open('vectorizer.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Model or vectorizer files not found. Ensure 'rf_model.pkl' and 'vectorizer.pkl' are in the same directory.")

# Input section for movie review
review = st.text_area("Enter your movie review below:")

if st.button("Analyze"):
    if review.strip():
        # Analyze polarity with TextBlob
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Transform the review using the TF-IDF vectorizer
        transformed_review = vectorizer.transform([review])

        # Predict sentiment using the Random Forest model
        prediction = rf_model.predict(transformed_review)
        probabilities = rf_model.predict_proba(transformed_review)[0]  # Get probabilities for confidence scores

        # Map prediction to sentiment
        if prediction[0] == 0:
            sentiment_label = "Negative Review"
            emotion = "Sad 😢"
            image_path = "sad.png"  # Replace with actual path to your sad image
        else:
            sentiment_label = "Positive Review"
            emotion = "Happy 😊"
            image_path = "happy.jpg"  # Replace with actual path to your happy image

        # Display results
        st.subheader(f"Sentiment: {sentiment_label}")
        st.write(f"Emotion: {emotion}")
        st.image(image_path, width=150)

        # Display confidence score
        confidence = max(probabilities) * 100
        st.write(f"**Confidence Score:** {confidence:.2f}%")

        # Display polarity and subjectivity
        st.write(f"**TextBlob Polarity:** {polarity:.2f}")
        st.write(f"**TextBlob Subjectivity:** {subjectivity:.2f}")

        # Explain the prediction by showing top influential words
        st.subheader("Key Words Influencing the Prediction")
        feature_names = vectorizer.get_feature_names_out()
        feature_array = transformed_review.toarray()[0]
        top_indices = np.argsort(feature_array)[::-1][:5]  # Top 5 features
        top_words = [(feature_names[i], feature_array[i]) for i in top_indices if feature_array[i] > 0]

        # Generate explanation based on top influential words
        if top_words:
            word_list = ", ".join([f"'{word}'" for word, _ in top_words])
            explanation = (
                f"The review was classified as **{sentiment_label.lower()}** primarily due to the presence of words like {word_list}, "
                f"which influenced the sentiment prediction."
            )
        else:
            explanation = (
                "The review was classified as **neutral** because it did not contain strong indicators of positive or negative sentiment."
            )

        # Display the explanation
        st.write(explanation)

        # Display top words if any
        if top_words:
            st.info("The following words had the most influence on the prediction:")
            for word, importance in top_words:
                st.info(f"- **{word}** (TF-IDF Score: {importance:.4f})")
        else:
            st.write("No significant words were found in this review.")
    else:
        st.warning("Please enter a valid review.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
