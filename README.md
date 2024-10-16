# Flashcard Generator

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)

This project is a simple flashcard generator that reads a CSV file containing questions and answers, 
creates flashcards, and exports them as an Anki deck (`.apkg` file). It uses the [genanki library](https://github.com/kerrickstaley/genanki) 
to create the deck and notes for studying.

The generated flashcards can be used with the [Anki app](https://apps.ankiweb.net/), which is a program designed to make 
remembering things easy. Anki is much more efficient than traditional study methods, allowing you to either greatly
decrease your time spent studying or significantly increase the amount you learn.
It benefits anyone who needs to remember information in their daily life.

## Table of Contents
   * [Project Structure](#project-structure)
   * [Requirements](#requirements)
   * [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
   * [Usage](#usage)
   * [How it Works](#how-it-works)
   * [License](#license)

### Project Structure:
- **`main.py`**: The entry point of the application. It reads the CSV data and triggers the flashcard creation process.
- **`csv_reader.py`**: Contains the `read_csv_file` function, which reads the CSV file and returns a list of dictionaries with questions and answers.
- **`flashcards_creator.py`**: Contains functions to generate the Anki deck and write it to an `.apkg` file.
- **`data.csv`**: The CSV file containing the questions and answers. You can edit this file to add more flashcards.
- **`English to German words.apkg`**: The output Anki deck generated by the program. This file can be imported into Anki.
- **`requirements.txt`**: Lists the Python dependencies needed for the project.

## Requirements

This project requires Python 3.8 or higher. To manage dependencies, it's recommended to set up a virtual environment.

## Setting Up a Virtual Environment

1. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:

    - On Windows:

      ```bash
      .venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source .venv/bin/activate
      ```

3. **Install the necessary dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the CSV file**: The `data.csv` file should contain your questions and answers in the following format:

   ```csv
   question,answer
   Hallo,Hello
   Danke,Thank you
   ```

2. **In `main.py` define `csv_filename`, `csv_delimiter`, and the name of the deck to be created (`deck_name`)**:
   ```python
    csv_filename = 'data.csv'
    csv_delimiter = ','
    questions_and_answers = read_csv_file(csv_filename, csv_delimiter)
   
    deck_name = "English to German words"
    create_flashcards(questions_and_answers, deck_name)
   ```

3. **Run the Application**:
   Execute the `main.py` script to generate the Anki flashcards.

   ```bash
   python main.py
   ```

4. **Output**: The generated Anki deck with the defined deck name will be saved in the project directory. 
You can import this file into your Anki app for study.

## How it Works

1. The `main.py` script reads the `data.csv` file using the `read_csv_file` function from `csv_reader.py`.
2. The questions and answers are passed to the `create_flashcards` function in `flashcards_creator.py`.
3. Flashcards are created and stored in an Anki deck, which is then exported as an `.apkg` file.

Note: The names of the decks, models, and other elements in the code are just examples. Feel free to modify them as needed.

## License

This project is licensed under the MIT License. You can view the license [here](https://github.com/Danzigerrr/Anki-Flashcards-Generator?tab=MIT-1-ov-file) and original template [here](https://opensource.org/licenses/MIT).


