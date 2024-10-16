import genanki
from csv_reader import read_csv_file
from flashcards_creator import create_flashcards

if __name__ == '__main__':
    questions_and_answers = read_csv_file('data.csv')
    create_flashcards(questions_and_answers)

