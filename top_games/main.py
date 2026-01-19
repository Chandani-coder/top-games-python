# ---------------- TOP GAMES PROJECT ----------------
# Beginner-friendly Python project
# Concepts used: functions, loops, conditionals, file flow, error handling

# Global name so all functions can access it
name = input("Your good name please: ").title()


# ---------------- MENU FUNCTION ----------------
def menu():
    print("\n===== GAME MENU =====")
    print("1. Number Guessing Game")
    print("2. Rock Paper Scissor")
    print("3. Math Calculator Game")
    print("4. Know Your Secret")
    print("5. Exit")


# ---------------- CONTINUE FUNCTION ----------------
def want_continue():
    """
    Asks user whether they want to continue.
    Returns True if yes, False if no.
    """
    while True:
        choice = input("Do you want to continue (Y/N): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid choice. Please enter Y or N.")


# ---------------- NUMBER GUESSING GAME ----------------
def num_guess():
    import random
    print("\n-- Welcome to Number Guessing Game --")

    while True:
        try:
            comp = random.randint(1, 20)
            user = int(input("Guess a number between 1 to 20: "))

            print("Computer chose:", comp)

            if user == comp:
                print("🎉 Yay!", name, "you guessed it right!")
            elif user < comp:
                print("Too low!")
            else:
                print("Too high!")

            if not want_continue():
                break

        except ValueError:
            print("Please enter a valid number.")


# ---------------- ROCK PAPER SCISSOR ----------------
def rock_pap():
    import random
    print("\n-- Welcome to Rock Paper Scissor --")

    options = ["Rock", "Paper", "Scissor"]
    score = 0

    while True:
        user = input("Choose Rock / Paper / Scissor: ").title()

        if user not in options:
            print("Invalid choice.")
            continue

        comp = random.choice(options)
        print("Computer chose:", comp)

        if user == comp:
            print("🤝 Match Draw")
        elif (
            (user == "Rock" and comp == "Scissor") or
            (user == "Paper" and comp == "Rock") or
            (user == "Scissor" and comp == "Paper")
        ):
            score += 1
            print("🏆 You win!")
        else:
            score -= 1
            print("Computer wins!")

        print("Score:", score)

        if not want_continue():
            break


# ---------------- MATH CALCULATOR GAME ----------------
def math_calc():
    import random
    print("\n-- Welcome to Math Calculator Game --")

    while True:
        try:
            a = random.randint(1, 100)
            b = random.randint(1, 100)

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = int(input("Choose level (1-4): "))

            if choice == 1:
                correct = a + b
                print(f"{a} + {b} = ?")
            elif choice == 2:
                correct = a - b
                print(f"{a} - {b} = ?")
            elif choice == 3:
                correct = a * b
                print(f"{a} * {b} = ?")
            elif choice == 4:
                correct = a / b
                print(f"{a} / {b} = ?")
            else:
                print("Invalid level.")
                continue

            ans = float(input("Your answer: "))

            if ans == correct:
                print("🎉 Correct!")
            else:
                print("❌ Wrong. Correct answer is:", correct)

            if not want_continue():
                break

        except ValueError:
            print("Invalid input.")


# ---------------- KNOW YOUR SECRET ----------------
def know_secret():
    print("\n-- Know Your Secret --")
    print("• You are strong and capable.")
    print("• You learn from every mistake.")
    print("• You are building your future step by step.")
    print("• You should be proud of yourself.")


# ---------------- MAIN PROGRAM ----------------
while True:
    try:
        menu()
        choice = int(input("Choose (1-5): "))

        if choice == 1:
            num_guess()
        elif choice == 2:
            rock_pap()
        elif choice == 3:
            math_calc()
        elif choice == 4:
            know_secret()
        elif choice == 5:
            print("Goodbye,", name)
            break
        else:
            print("Invalid menu choice.")

    except ValueError:
        print("Please enter a number.")
