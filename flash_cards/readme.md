# 🧠 Flashcard Forge

## 📖 About the Project
**Flashcard Forge** is a working web app built from scratch with Python. Its main goal is to help you escape "Inert Knowledge" (stuff you memorize but can't use) and achieve "Deep Learning" by engineering a solution to the "Forgetting Curve".

This project was built using the principle of **Separation of Concerns**, dividing the logic (Backend) from the visuals (Frontend). The engineer's toolbox for this project includes:
*   **Python (The Engine):** The core programming language.
*   **OOP (The Architecture):** Object-Oriented Programming concepts used to build blueprints (Classes) and specific instances (Objects) for modularity.
*   **Pandas (The Librarian):** A data handler used to read and manipulate the raw data.
*   **Streamlit (The Face):** The framework used to create an instant Web UI and manage persistent memory across the session.

## 📂 File Structure
The project is organized into four main files to keep the code clean and modular:
*   `flashcards.csv` 🗂️: **The Data**. A raw text file with no headers containing your questions and answers.
*   `flashcard.py` 🧱: **The Brick / Unit**. Defines the `Flashcard` class and its constructor, setting the initial state (question and answer).
*   `deck.py` 🗃️: **The Manager**. Defines the `Deck` class, which loads the data from the CSV, owns the cards (Composition), and handles the logic to shuffle or get the next card.
*   `main.py` 🖥️: **The Interface**. Wires the main circuit, initializes the persistent session state, and creates the dashboard controls (Shuffle, Flip, Next buttons) on the web page.

## 🚀 How to Run the Program in the Terminal

Because this application uses **Streamlit** to generate a web interface, it runs on `localhost` (your computer acts as the server). 

1. Open your terminal.
2. Navigate to your project directory (`project_folder/`).
3. Execute the following command:

```bash
streamlit run main.py
```

Once you hit *Enter*, your default web browser will automatically open a new tab displaying your interactive Flashcard Forge dashboard!
