#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv) - 1
    try:
        if argc > 1:
            scores = [int(x) for x in sys.argv[1:]]
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}\n")
        else:
            print(f"No scores provided. Usage: python3 {sys.argv[0]}"
                  f" <score1> <score2> ...")
    except ValueError:
        print("Error: All scores must be valid integers.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ft_score_analytics()
