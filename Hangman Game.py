import random
# Define word categories for each difficulty level
import selection
# Define hangman pictures for each difficulty level
import pic
def choose_difficulty():
    while True:
        # Display available difficulty levels
        print("Choose a difficulty level:")
        for difficulty in selection.categories.keys():
            print(difficulty)

        selected_difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").capitalize()

        # Check if the selected difficulty level exists
        if selected_difficulty in selection.categories:
            return selected_difficulty
        else:
            print("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")

def choose_word(difficulty, category):
    word_list = selection.categories[difficulty][category]
    return random.choice(word_list)

def choose_category(difficulty):
    while True:
        # Display available categories for the chosen difficulty level
        print(f"Choose a category for {difficulty} difficulty:")
        for category in selection.categories[difficulty].keys():
            print(category)

        selected_category = input("Enter the category: ").capitalize()

        # Check if the selected category exists for the chosen difficulty level
        if selected_category in selection.categories[difficulty]:
            return selected_category
        else:
            print(f"Invalid category. Please enter a valid category for {difficulty} difficulty.")

# Modify the play_game function to pass both difficulty and category
def play_game():
    while True:
        difficulty = choose_difficulty()
        category_name = choose_category(difficulty)
        chosen_word = choose_word(difficulty, category_name)
        num_spaces = len(chosen_word)

        # Adjust the number of lives based on difficulty
        if difficulty == "Easy":
            lives = 6
        elif difficulty == "Medium":
            lives = 4
        elif difficulty == "Hard":
            lives = 3

        # Initialize the display as a list of underscores
        display = ['_'] * num_spaces

        # Initialize guessed letters as an empty set
        guessed_letters = set()

        print(f"Category: {category_name}")
        print(f"{' '.join(display)}")  # Display underscores representing the word

        lives_lost = 0  # Track the number of lives lost

        game_over = False
        while not game_over:
            print(f"Lives: {lives - lives_lost}")  # Display remaining lives
            guessed_letter = input('Guessed a letter: ').lower()

            # Check if the letter has already been guessed
            if guessed_letter in guessed_letters:
                print("You've already guessed that letter.")
                continue

            guessed_letters.add(guessed_letter)  # Add the guessed letter to the set

            letter_guessed = False  # Flag to check if the guessed letter is in the word

            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guessed_letter:
                    display[position] = guessed_letter
                    letter_guessed = True  # Mark that the letter was guessed

            if not letter_guessed:
                lives_lost += 1
                if lives_lost >= lives:
                    game_over = True

            if '_' not in display:
                game_over = True

            print("\n" + " ".join(display))  # Display the word with guessed letters
            print(pic.hangman_pic[difficulty][lives - lives_lost])  # Display the appropriate hangman picture

            # Display guessed letters
            print(f"Letters guessed by you: {', '.join(guessed_letters)}")

        # Reveal the chosen word
        print(f"The word was: {chosen_word}")

        if '_' not in display:
            print("Congratulations! You've won!")
        else:
            print("Game over. You lose!")

        play_again = input("Do you want to play Hangman again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    print("Let's play Hangman!")
    play_game()
