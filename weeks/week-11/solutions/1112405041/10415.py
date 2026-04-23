import sys

fingerings = {
    'c': [2, 3, 4, 7, 8, 9, 10],
    'd': [2, 3, 4, 7, 8, 9],
    'e': [2, 3, 4, 7, 8],
    'f': [2, 3, 4, 7],
    'g': [2, 3, 4],
    'a': [2, 3],
    'b': [2],
    'C': [3],
    'D': [1, 2, 3, 4, 7, 8, 9],
    'E': [1, 2, 3, 4, 7, 8],
    'F': [1, 2, 3, 4, 7],
    'G': [1, 2, 3, 4],
    'A': [1, 2, 3],
    'B': [1, 2]
}

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data: return

    t = int(input_data[0])
    for i in range(1, t + 1):
        melody = input_data[i]
        counts = [0] * 11 # 1-10
        current_state = [False] * 11

        for note in melody:
            target_fingers = fingerings[note]
            target_state = [False] * 11
            for f in target_fingers:
                target_state[f] = True

            for f in range(1, 11):
                if target_state[f] and not current_state[f]:
                    counts[f] += 1
            current_state = target_state

        print(*(counts[1:]))

if __name__ == "__main__":
    solve()
