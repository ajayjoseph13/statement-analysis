from tkinter import Tk, Label, Text, Button, END
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment():
    statement = text_input.get("1.0", END).strip()  # Get the text input
    if not statement:
        result_label.config(text="Please enter a statement.")
        return
    
    # Perform sentiment analysis
    blob = TextBlob(statement)
    sentiment_score = blob.sentiment.polarity
    
    # Determine if it's positive, negative, or neutral
    if sentiment_score > 0:
        sentiment = "Positive 😊"
    elif sentiment_score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    result_label.config(text=f"Sentiment: {sentiment} (Score: {sentiment_score:.2f})")

# Create the main application window
root = Tk()
root.title("Sentiment Analysis App")
root.geometry("400x300")
root.resizable(False, False)

# Create UI elements
Label(root, text="Enter your statement:", font=("Arial", 12)).pack(pady=10)
text_input = Text(root, height=5, width=40, wrap="word", font=("Arial", 10))
text_input.pack(pady=5)

Button(root, text="Analyze Sentiment", command=analyze_sentiment, font=("Arial", 12), bg="lightblue").pack(pady=10)
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
