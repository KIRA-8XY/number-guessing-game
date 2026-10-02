# number-guessing-game

A short terminal game where the player has 7 attempts to guess a secret number between 1 and 100. After each guess, the program says whether it is too low or too high. When the game ends, the player can choose to play again.

## How to run

```
python main.py
```

## Features

- Input validation: typing letters or a number outside the range does not use up an attempt
- Limited attempts (7), with the secret number revealed after a loss
- Play again option
- Clean exit with Ctrl+C

## What to add later

- Let the player choose the number range instead of always using 1 to 100
- Add difficulty levels (a different number of attempts for each level)

## What I learned

- Input handling with `input()` and `int()`
- Loops (`while`) and conditionals
- Error handling with `try` / `except`
- Using constants for values that never change
- Splitting a program into functions with parameters and `return`
- Using `break` and `continue` to control loops
- Writing a project's history on GitHub with small commits