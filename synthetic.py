import pandas as pd
import random

# Load the CSV file
df = pd.read_csv('events.csv')

# Function to shuffle words in a string
def shuffle_words(string):
    if isinstance(string, str):  # Check if the input is a string
        words = string.split()
        random.shuffle(words)
        return ' '.join(words)
    return string  # Return the input as-is if it's not a string

# Apply the function to the 'title_details' column
df['title_details'] = df['title_details'].apply(shuffle_words)

# Save the modified DataFrame back to CSV
df.to_csv('events_shuffled.csv', index=False)
