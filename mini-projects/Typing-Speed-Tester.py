# Typing Speed Tester.

import time

sentence = "Python programming improves problem solving skills"

print("Type the following sentence:")
print(f"\n{sentence}\n")

input("Press Enter when you are ready...")

start = time.time()
typed_text = input("\nType here: ")
end = time.time()

elapsed_time = end - start
words = len(typed_text.split())
speed = words / (elapsed_time / 60)

accuracy = sum(
    1 for a, b in zip(sentence, typed_text)
    if a == b
)

accuracy_percentage = accuracy / len(sentence) * 100

print("\n===== RESULTS =====")
print(f"Time: {elapsed_time:.2f} seconds")
print(f"Typing speed: {speed:.2f} WPM")
print(f"Character accuracy: {accuracy_percentage:.2f}%")