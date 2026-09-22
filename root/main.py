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

while True:
    result = game_beginning()

    if result == "yes":
        break
    elif result == "no":
        exit()
    else:
        print("Please type yes or no.")


print("Great! You will complete 5 attempts.")



for attempt in range(5):
    print(f"Attempt {attempt}:")
    time_taken = game_start()
    attempt_times = attempt_times + [time_taken]  # no append
    print(f"Your reaction time was: {time_taken} seconds")

fastest = min(attempt_times)
print("All attempts complete!")
print(f"Your fastest reaction time was: {fastest} seconds, "
      f"but if you pressed enter before {"Go"} .........................................................................................................................................................................................(You're a big fat cheater😒🫥)")

