import streamlit as st

# Set page configuration to full-width layout
st.set_page_config(
    page_title="Movie Review Sentiment Analyzer",
    page_icon="🎬",
    layout="wide",  # Enables full-width layout
    initial_sidebar_state="expanded"
)

def add_custom_css():
    # Adding custom CSS for larger text and footer styling
    st.markdown(
        """
        <style>
        /* Remove Streamlit's default padding and add custom margins */
        .block-container {
            padding: 20px 50px; /* Top-bottom: 20px, Left-right: 50px */
            max-width: 100%; /* Ensure it stretches full width */
        }

        /* General Text Styling */
        h1, h2, h3, h4, h5, h6 {
            font-size: 1.5rem; /* Larger heading font size */
        }

        p, li {
            font-size: 1.2rem; /* Larger paragraph font size */
            line-height: 1.6; /* Add spacing between lines for readability */
        }

        .st-expander p {
            font-size: 1.1rem; /* Increase font size inside FAQ */
        }

        /* Footer Styling */
        .footer {
            background-color: #ff4d4d; /* Red background */
            color: white; /* White text */
            padding: 15px;
            text-align: center;
            font-size: 1.2rem; /* Larger footer text */
            width: 100%; /* Full width */
            margin-top: 50px; /* Add spacing above the footer */
            border-radius: 10px; /* Optional: rounded corners */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Add custom CSS
    add_custom_css()

    # Main Content
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Title and Introduction
    st.title("🎬 Movie Review Sentiment Analyzer")
    st.write("""
    Welcome to the Movie Review Sentiment Analyzer! 🎉  
    This application uses machine learning and natural language processing to analyze the sentiment of movie reviews.
    
    #### Key Features:
    - Classify reviews as **Positive** or **Negative** using a trained Random Forest model.
    - Analyze the **Polarity** and **Subjectivity** of the review using TextBlob.
    - Get an intuitive output with text labels, emojis, and more!
    
    #### How to Use:
    1. Go to the **Sentiment Analysis** page (if multi-page setup is used).
    2. Enter a movie review in the text box.
    3. Click the "Analyze" button to see the results.
    """)

    # Purpose of Sentiment Analysis
    st.header("🎯 Purpose of Movie Review Sentiment Analysis")
    st.write("""
    The primary purpose of analyzing movie reviews is to extract valuable insights and better understand audience opinions. Here are some of the main objectives:
    
    - **Understand Viewer Sentiment**: Determine whether viewers liked or disliked a movie.
    - **Help Moviegoers**: Provide insights to help audiences decide whether to watch a film.
    - **Improve Film Production**: Identify aspects of movies that resonate with viewers.
    - **Market Research**: Benchmark a movie's performance and audience reception against competitors.
    - **Trend Analysis**: Track evolving audience preferences and emerging themes in cinema.
    - **Enhance Streaming Platforms**: Curate and recommend content based on viewer sentiments.
    - **Automate Review Categorization**: Quickly classify thousands of reviews as positive, negative, or neutral.
    - **Improve Marketing Strategies**: Use sentiment data to craft more targeted campaigns.
    - **Academic Research**: Explore the emotional and linguistic aspects of movie reviews.
    """)

    # FAQ Section
    with st.expander("FAQ"):
        st.write("""
        **Q: What is Sentiment Analysis?**  
        A: Sentiment analysis is the process of determining the emotional tone behind words. It helps classify text as positive, negative, or neutral.

        **Q: How accurate is this app?**  
        A: The accuracy depends on the machine learning model and dataset used for training. For best results, the model was trained on a diverse dataset of movie reviews.

        **Q: What technologies power this app?**  
        A: This app uses a combination of Python libraries such as Streamlit for the interface, TextBlob for text analysis, and a Random Forest machine learning model for sentiment classification.

        **Q: Can this app analyze reviews in other languages?**  
        A: Currently, the app is optimized for English reviews. For non-English text, translation tools can be integrated in the future.

        **Q: What are Polarity and Subjectivity?**  
        A:  
        - **Polarity** measures how positive or negative a review is, with values ranging from -1 (negative) to 1 (positive).  
        - **Subjectivity** measures how opinionated the text is, with values ranging from 0 (factual) to 1 (opinion-based).

        **Q: Can I analyze multiple reviews at once?**  
        A: Currently, this app supports one review at a time. However, batch analysis can be added in the future for multiple reviews.

        **Q: Is my data secure?**  
        A: Yes, all reviews are processed locally and are not stored or shared with third parties.

        **Q: How can I contribute to this project?**  
        A: You can reach out to the creators for collaboration or suggestions. Your feedback is always welcome to improve the app!

        **Q: Why do I get "neutral" results sometimes?**  
        A: Neutral results occur when the text contains a mix of positive and negative words or lacks strong emotional tones.

        **Q: Can this app handle sarcasm or context?**  
        A: Sarcasm and complex context are challenging for most sentiment analysis models. While the app does its best, it might misclassify such cases.

        **Q: What's next for this app?**  
        A: Future updates may include support for additional languages, improved visualizations, integration with APIs (like movie databases), and batch review analysis.
        """)

    # Add a call to action or extra information
    st.info("Ready to get started? Head over to the app section and try it out!")

    # "Creators" Section
    st.header("👥 Meet the Creators")
    col1, col2, col3, col4 = st.columns(4)

    # Add images of creators
    with col1:
        st.image("images/Jestin.jpg", caption="Jestin John D. Verceles", use_column_width=True)
    with col2:
        st.image("images/Alana.jpg", caption="Christiana C. Alana", use_column_width=True)
    with col3:
        st.image("images/Andrei.jpg", caption="Andrei B. Manzanes", use_column_width=True)
    with col4:
        st.image("images/mary.jpg", caption="Mary Grace C. San Gaspar", use_column_width=True)

    # Add a paragraph about the creators
    st.write("""
    #### About the Creators
    This application was brought to life by a passionate team of developers and data enthusiasts. 
    With a shared love for movies and AI, we combined our skills to create an intuitive and fun tool for analyzing movie reviews. 
    Each of us brought a unique skill set to the table—from coding and design to machine learning and NLP. 
    We hope you enjoy using this application as much as we enjoyed building it! 🎥✨
    """)

    # End Main Content
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">Developed by [GROUP 1] | Powered by Streamlit 🚀</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
