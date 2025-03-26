"""a program that will run a version of wordle"""

__author__: str = "730572179"


def contains_char(og_word: str, character: str) -> bool:
    """determines if a character is in the og word at any index"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(og_word):
        if og_word[idx] == character:
            return True
        elif og_word[idx] != character:
            idx = idx + 1
    else:
        return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """returns a Wordle-like string of emojis after a word is guessed"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guessed_word) == len(secret_word), "Guess must be same length as secret"

    idx: int = 0
    emoji_output: list[str] = []

    while idx < len(guessed_word):
        if guessed_word[idx] == secret_word[idx]:
            emoji_output.append(GREEN_BOX)
            idx = idx + 1
        elif contains_char(og_word=secret_word, character=guessed_word[idx]) == True:
            emoji_output.append(YELLOW_BOX)
            idx = idx + 1
        else:
            emoji_output.append(WHITE_BOX)
            idx = idx + 1
    return "".join(emoji_output)


def input_guess(n: int) -> str:
    """prompts user to guess character length"""
    guess = input(f"Enter a {n} character word:")
    while len(guess) != n:
        guess = input(f"That wasn't {n} chars! Try again:")
    return str(guess)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(n=len(secret))
        print(emojified(guessed_word=guess, secret_word=secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        else:
            turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
