import time
import random

best_time = None

for _ in range(5):
    time.sleep(random.randrange(2,5))

    start_time = time.monotonic()

    input("Andele Amigo")
    end_time = time.monotonic()

    speed = end_time - start_time

    print(speed)

    if best_time is None:
        best_time = speed
    if speed > best_time:
        best_time = speed
print(f"Your fastest time is equal to {best_time}")