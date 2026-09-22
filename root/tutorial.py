import time

start_time = time.monotonic()

timer_length = 1

while True:
    current_time = time.monotonic()

    elapsed_time = current_time - start_time

    if elapsed_time >= timer_length:
        print("Timer complete!")
        print("Hello")

        start_time = time.monotonic()

