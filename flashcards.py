# Read the file with the flashcard data
def read_file(filename):
    with open(filename, "r") as flashcards_file:
        return flashcards_file.readlines()


FILE_PATH = "flashcards_data.txt"

raw_flashcards = read_file(FILE_PATH)

# Extract flashcards into usable format (dictionary)
flashcards_dict = {}

for card in raw_flashcards:
    card = card.strip()
    question, answer = card.split(":")
    flashcards_dict[question] = answer

# Show the user the flashcards, question first, then answer
print("Press Enter to reveal answer for each question.")
for question, answer in flashcards_dict.items():
    input(f"Question: {question}")
    print(f"Answer: {answer}")
