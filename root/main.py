import time
import random

timer_length = random.choice([1, 2, 3, 4, 5])
best_time = None

def game_beginning():
    answer = input(
        "Welcome to The Reaction Game. When the computer says GO, press Enter as fast as possible to see your reaction time. Are you ready? ").strip().lower()

    if answer == "yes":
        return "yes"

    elif answer == "no":
        print("Ok. Goodbye 👋")
        return "no"
    else:
        print("Invalid input. Are you ready to play?")
        return "invalid"
game_beginning()

def game_start():
    print("Get ready...")
    time.sleep(timer_length)

    print("Andele Amigo!")
    start_time = time.monotonic()
    input()

    end = time.monotonic()
    reaction_time = end - start_time
    print(f"Your reaction time was: {reaction_time} seconds")
    return reaction_time


print("Great! You will complete 5 attempts.")

best_time = None

for attempt in range(1,6):
    print(f"Attempt {attempt}:")
    time_taken = game_start()

    if best_time is None or time_taken < best_time:
        best_time = time_taken

print("All attempts complete!")
print(
    f"Your fastest reaction time was: {best_time} seconds, "
    f"but if you pressed enter before 'GO' .........................................................................................................................................................................................(You're a big fat cheater😒🫥)"
)

