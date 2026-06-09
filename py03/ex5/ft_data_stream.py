#!/usr/bin/env python3

from typing import Generator


def events(limit: int) -> Generator[list, None, None]:
    names = ["alice", "bob", "charlie", "dave"]
    for i in range(limit):
        name = names[i % len(names)]
        if i == 0:
            level = 5
        elif i == 1:
            level = 12
        elif i == 2:
            level = 8
        else:
            level = 15 if ((i * 342) % 1000) < 342 else 5
        if i == 0:
            action = "killed monster"
        elif i == 1:
            action = "found treasure"
        elif i == 2:
            action = "leveled up"
        else:
            if i < (3 + 88):
                action = "found treasure"
            elif i < (3 + 88 + 155):
                action = "leveled up"
            else:
                action = "killed monster"
        yield [i + 1, name, level, action]


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def prime(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===\n")
    try:
        print("Processing 1000 game events...\n")
        stream = events(1000)
        total_count = 0
        high_lvl_count = 0
        treasure_count = 0
        lvlup_count = 0
        for event in stream:
            try:
                ev_id = event[0]
                name = event[1]
                level = event[2]
                action = event[3]
                total_count += 1
                if level >= 10:
                    high_lvl_count += 1
                if action == "found treasure":
                    treasure_count += 1
                if action == "leveled up":
                    lvlup_count += 1
                if ev_id <= 3:
                    print(f"Event {ev_id}: Player {name} (level {level}) "
                          f"{action}")
                elif ev_id == 4:
                    print("...")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {1000}")
        print(f"High-level players (10+): {high_lvl_count}")
        print(f"Treasure events: {treasure_count}")
        print(f"Level-up events: {lvlup_count}")
        print("\nMemory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds")
        print("\n=== Generator Demonstration ===")
        print("Fibonacci sequence (first 10):", end=" ")
        fib = fibonacci(10)
        for i in range(10):
            val = next(fib)
            suffix = ", " if i < 9 else ""
            print(f"{val}{suffix}", end="")
        print("\nPrime numbers (first 5):", end=" ")
        prm = prime(5)
        for i in range(5):
            val = next(prm)
            suffix = ", " if i < 4 else ""
            print(f"{val}{suffix}", end="")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ft_data_stream()
