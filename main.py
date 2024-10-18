from csv_reader import read_csv_file
from flashcards_creator import create_flashcards

if __name__ == '__main__':
    csv_filename = 'data.csv'
    csv_delimiter = ','

    questions_and_answers = read_csv_file(csv_filename, csv_delimiter)
    create_flashcards(questions_and_answers)

