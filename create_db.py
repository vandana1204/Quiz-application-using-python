# create_db.py

import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL
    )
    ''')

    # Insert sample data
    sample_data = [
        ("What is the capital of France?", "Berlin", "London", "Paris", "Madrid", "Paris"),
        ("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "Mars"),
        ("What is the largest ocean on Earth?", "Atlantic", "Indian", "Arctic", "Pacific", "Pacific"),
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway", "Harper Lee"),
        ("What is the smallest prime number?", "0", "1", "2", "3", "2"),
        ("What is the chemical symbol for water?", "H2O", "O2", "CO2", "NaCl", "H2O"),
        ("What is the speed of light?", "299,792 km/s", "150,000 km/s", "1,080,000 km/s", "300,000 km/s", "299,792 km/s"),
        ("Who painted the Mona Lisa?", "Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "Leonardo da Vinci"),
        ("What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", "Diamond"),
        ("Who developed the theory of relativity?", "Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei", "Albert Einstein")
    ]

    cursor.executemany('''
    INSERT INTO questions (question, option1, option2, option3, option4, answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and sample data inserted.")
