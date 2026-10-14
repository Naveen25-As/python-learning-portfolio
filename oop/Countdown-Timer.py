# Countdown Timer

import time

try:
    seconds = int(input("Enter countdown duration in seconds: "))

    if seconds < 0:
        print("Enter a non-negative number.")
    else:
        while seconds > 0:
            minutes, remaining_seconds = divmod(seconds, 60)

            print(
                f"\rTime remaining: {minutes:02d}:"
                f"{remaining_seconds:02d}",
                end="",
                flush=True
            )

            time.sleep(1)
            seconds -= 1

        print("\nTime's up!")

except ValueError:
    print("Please enter a valid integer.")