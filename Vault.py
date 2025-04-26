# Final Project: Crack the Vault (Python)
# Intro to Programming - Secure Vault Challenge

import random

def generate_code():
    return str(random.randint(1000, 9999))

def give_hint(code, guess):
    correct_pos = sum(1 for a, b in zip(code, guess) if a == b)
    correct_digits = sum(min(code.count(d), guess.count(d)) for d in set(guess))
    wrong_pos = correct_digits - correct_pos
    return correct_pos, wrong_pos

def play_game():
    code = generate_code()
    attempts = 8

    print("\n Crack the Vault Game Started!")
    print("Guess the 4-digit code. You have 8 tries.\n")

    with open("vault_log.txt", "a") as log:
        log.write("\n--- New Game ---\n")
        # log.write(f"[DEBUG] Code: {code}\n")  # uncomment for testing

        while attempts > 0:
            guess = input("Enter a 4-digit code: ")

            if not guess.isdigit() or len(guess) != 4:
                print(" Please enter exactly 4 digits.\n")
                continue

            log.write(f"Guess: {guess}\n")

            if guess == code:
                print(" Correct! Vault unlocked!\n")
                log.write("Result: SUCCESS\n")
                break

            attempts -= 1
            correct_pos, wrong_pos = give_hint(code, guess)
            print(f" Wrong! Attempts left: {attempts}")
            print(f" Hint: {correct_pos} digit(s) in correct place, {wrong_pos} correct but wrong place.\n")

        else:
            print(f" Locked out! The code was: {code}")
            log.write("Result: LOCKED OUT\n")

while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
