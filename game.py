import streamlit as st
import mysql.connector

# Function to connect to the MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gungun22",
        database="murder_history"
    )

# Function to get clues and suspects from the database
def get_clues():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clues")
    clues = cursor.fetchall()
    cursor.close()
    connection.close()
    return clues

# Function to display the game
def display_game():
    st.title("Murder Mystery Game")
    st.write("Welcome to the Murder Mystery Game! Can you solve the mystery?")

    clues = get_clues()

    if not clues:
        st.write("No clues found in the database.")
        return

    st.write("Here are the clues:")
    for clue in clues:
        st.write(f"- {clue[1]} (Suspect: {clue[2]})")

    st.write("### Make your guess!")
    guess = st.text_input("Who do you think is the murderer?")

    if st.button("Submit Guess"):
        if guess:
            st.success(f"You guessed: {guess}")
            # You can add logic to check if the guess is correct
        else:
            st.error("Please enter a guess.")

# Run the game
if __name__ == "__main__":
    display_game()
