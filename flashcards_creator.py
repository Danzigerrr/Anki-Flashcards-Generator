import genanki
import random


def generate_random_id():
    return random.randrange(1 << 30, 1 << 31)


def define_model(model_name):
    model_id = generate_random_id()
    my_model = genanki.Model(
        model_id,
        model_name,
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    return my_model


def create_deck(deck_name):
    deck_id = generate_random_id()
    deck = genanki.Deck(deck_id, deck_name)
    return deck


def create_notes(questions_and_answers):

    model = define_model("Basic Flashcards Model")

    notes = []
    for q_and_a in questions_and_answers:
        note = genanki.Note(
            model=model,
            fields=[q_and_a['question'], q_and_a['answer']])
        notes.append(note)
    return notes


def create_deck_with_notes(notes, deck_name):
    deck = create_deck(deck_name)

    for note in notes:
        deck.add_note(note)
    return deck


def write_deck_to_file(deck, filename):
    genanki.Package(deck).write_to_file(filename + '.apkg')


def create_flashcards(questions_and_answers):
    deck_name = "English to German words"

    notes = create_notes(questions_and_answers)
    deck = create_deck_with_notes(notes, deck_name)
    write_deck_to_file(deck, deck_name)
