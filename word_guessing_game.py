import random
import pyttsx3  # Text-to-speech for voice announcement
import winsound  # For sound effects (Windows)
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Category-based word lists
word_bank = {
    "Animals": ["tiger", "elephant", "giraffe", "dolphin"],
    "Cities": ["paris", "tokyo", "mumbai", "berlin"],
    "Fruits": ["apple", "banana", "cherry", "kiwi"]
}

def play_victory_sound(name):
    """Play personalized victory announcement"""
    engine.say(f"Congratulations {name}! You won the match!")
    engine.runAndWait()
    # Additional celebratory sound (Windows)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def play_feedback_sound(is_correct):
    """Play feedback sounds"""
    frequency = 1000 if is_correct else 200
    winsound.Beep(frequency, 300)  # 300ms beep

def main():
    print("=== WORD GUESSING GAME ===")
    name = input("Enter your name: ").strip().title()
    print(f"\nWelcome, {name}! Guess the word to win!\n")

    # Category selection
    print("Choose a category:")
    for i, category in enumerate(word_bank.keys(), 1):
        print(f"{i}. {category}")
    
    # Get valid category choice
    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(word_bank):
                selected_category = list(word_bank.keys())[choice-1]
                break
            print(f"Please enter 1-{len(word_bank)}!")
        except ValueError:
            print("Invalid input! Enter a number.")

    # Game setup
    word = random.choice(word_bank[selected_category])
    guesses = ""
    turns = 8
    print(f"\nCategory: {selected_category}")
    print(f"Word: {'_ ' * len(word)}")
    print(f"Turns left: {turns}\n")

    # Game loop
    while turns > 0:
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guesses:
            print("Already guessed!")
            continue
        
        guesses += guess

        # Check guess and play sound
        if guess in word:
            print("\nCorrect!")
            play_feedback_sound(True)
        else:
            turns -= 1
            print(f"\nWrong! Turns left: {turns}")
            play_feedback_sound(False)
        
        # Display progress
        display = [letter if letter in guesses else "_" for letter in word]
        print(f"Word: {' '.join(display)}")
        
        # Win condition
        if "_" not in display:
            print(f"\n🎉 CONGRATULATIONS, {name}! YOU WON! 🎉")
            play_victory_sound(name)
            print(f"The word was: {word.upper()}")
            break
    
    # Lose condition
    if turns == 0:
        print(f"\n💀 GAME OVER! The word was: {word.upper()}")

if __name__ == "__main__":
    main()
