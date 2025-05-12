import random

def display_room_art(room_number):
    print("""
    +----------+
    |  Room {}  |
    |  ~~~~~~  |
    |  [Door]  |
    +----------+
    """.format(room_number))


def display_gem_art():
    print("""
    *** Gem Collected! ***
       _____
      /     \\
     /_______\\
    """)


def get_hint(word, cost=5):
    """Generate a hint with first letter and underscores (e.g., m _ _ n for moon)."""
    if len(word) <= 2:
        return word[0] + " " + "_" * (len(word) - 1)
    return word[0] + " " + " ".join("_" for _ in word[1:])


def play_language_temple():
    print("Welcome to the Language Temple!")
    print("You are an explorer trapped in a temple of knowledge.")
    print("To escape, translate Vietnamese words to English to unlock doors.")
    print("Type 'quit' to exit or 'hint' for a clue (costs 5 points).")

    # Flashcard dictionary: Vietnamese word -> English translation
    flashcards = {
        "Xin chào": "hello",
        "Cảm ơn": "thank you",
        "Ngôi nhà": "house",
        "Cái cây": "tree",
        "Con sông": "river",
        "Bầu trời": "sky",
        "Bông hoa": "flower",
        "Biển cả": "sea"
    }

    # Select 5 words randomly without repetition
    total_rooms = 5
    words = random.sample(list(flashcards.keys()), total_rooms)

    inventory = []
    score = 0
    current_room = 0
    hint_used = False

    while current_room < total_rooms:
        word = words[current_room]
        display_room_art(current_room + 1)
        print(f"Room {current_room + 1} of {total_rooms}: The door has an inscription: '{word}'")

        while True:
            answer = input("Translate this Vietnamese word to English (or 'quit', 'hint'): ").lower().strip()

            # Input validation
            if answer == "":
                print("Empty input. Please enter a translation, 'quit', or 'hint'.")
                continue
            elif answer == "quit":
                print("\nYou abandon the temple. Game over.")
                print(f"Final Score: {score}")
                print(f"Gems Collected: {len(inventory)}")
                return
            elif answer == "hint":
                if hint_used:
                    print("You've already used a hint for this room. Try answering!")
                    continue
                if score < 5:
                    print("Not enough points for a hint (need 5). Keep trying!")
                    continue
                score -= 5
                hint = get_hint(flashcards[word])
                print(f"Hint: {hint} (Cost: 5 points)")
                hint_used = True
                continue
            elif not answer.replace(" ", "").isalpha():
                print("Invalid input. Please use letters only for the translation.")
                continue

            # Check answer
            if answer == flashcards[word]:
                print(f"Correct! The door unlocks, and you find a gem.")
                display_gem_art()
                inventory.append("gem")
                score += 10
                current_room += 1
                hint_used = False
                break
            else:
                print(f"Incorrect. The correct translation is '{flashcards[word]}'. Try again.")
                score -= 2
                break

        if inventory:
            print(f"Inventory: {', '.join(inventory)}")
        print(f"Score: {score}")

    print("\nCongratulations! You've unlocked all doors and escaped the temple!")
    print(f"Final Score: {score}")
    print(f"Gems Collected: {len(inventory)}")


if __name__ == "__main__":
    try:
        play_language_temple()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
        print("Final Score: 0")
        print("Gems Collected: 0")