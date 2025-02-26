
#### main.py

```python
#!/usr/bin/env python3
import random

events = [
    "476 AD - Fall of the Western Roman Empire.",
    "1066 - The Norman conquest of England.",
    "1492 - Columbus discovers the Americas.",
    "1789 - The French Revolution begins.",
    "1969 - Apollo 11 lands on the Moon."
]

def get_random_event():
    return random.choice(events)

def main():
    print("Welcome to Equinox Historical Events!")
    print("Here's a random historical event:")
    print(get_random_event())

if __name__ == "__main__":
    main()
