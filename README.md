# Language Temple: Vietnamese Flashcard Game

**Language Temple** is a text-based Python game that makes learning Vietnamese vocabulary fun! As an explorer trapped in a mystical temple, you translate Vietnamese words to English to unlock doors and escape. With randomized puzzles, ASCII art, and a hint system, it’s both educational and engaging.

## Features

- **Randomized Puzzles**: 5 unique Vietnamese words per game, no repeats.
- **ASCII Art**: Visuals for rooms and gems enhance the experience.
- **Hint System**: Type `hint` for clues (e.g., `m _ _ n` for `moon`) at a 5-point cost.
- **Robust Input**: Handles invalid inputs, with a `quit` option.
- **Scoring & Inventory**: Earn points and collect gems for correct answers.

## How to Run

1. Save as `language_temple.py`.
2. Run with Python 3: `python language_temple.py`.
3. Translate words, use `hint`, or type `quit` to exit.

## Demo

Below is a sample gameplay session:

```
Welcome to the Language Temple!
You are an explorer trapped in a temple of knowledge.
To escape, translate Vietnamese words to English to unlock doors.
Type 'quit' to exit or 'hint' for a clue (costs 5 points).

    +----------+
    |  Room 1  |
    |  ~~~~~~  |
    |  [Door]  |
    +----------+
Room 1 of 5: The door has an inscription: 'Xin chào'
Translate this Vietnamese word to English (or 'quit', 'hint'): hint
Hint: h _ _ _ o (Cost: 5 points)
Translate this Vietnamese word to English (or 'quit', 'hint'): hello
Correct! The door unlocks, and you find a gem.

    *** Gem Collected! ***
       _____
      /     \
     /_______\
Inventory: gem
Score: 5

[... Skipping to Room 5 ...]

    +----------+
    |  Room 5  |
    |  ~~~~~~  |
    |  [Door]  |
    +----------+
Room 5 of 5: The door has an inscription: 'Căn nhà'
Translate this Vietnamese word to English (or 'quit', 'hint'): home
Correct! The door unlocks, and you find a gem.

    *** Gem Collected! ***
       _____
      /     \
     /_______\
Inventory: gem, gem, gem, gem, gem
Score: 45

Congratulations! You've unlocked all doors and escaped the temple!
Final Score: 45
Gems Collected: 5
```

Perfect for language learners and game enthusiasts!
