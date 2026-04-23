import sys

def solve():
    # Use generator to read from stdin to save memory
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word

    input_gen = get_input()

    while True:
        try:
            val = next(input_gen)
            n = int(val)
        except StopIteration:
            break

        disallowed = []
        for i in range(n):
            bad_pos = set()
            while True:
                pos = int(next(input_gen))
                if pos == 0: break
                bad_pos.add(pos)
            disallowed.append(bad_pos)

        used = [False] * n
        current_perm = [None] * n
        last_perm = [""] * n

        def backtrack(depth):
            if depth == n:
                # Output logic: compare with last_perm
                res = []
                diff_found = False
                for i in range(n):
                    char = current_perm[i]
                    if not diff_found and char == last_perm[i]:
                        res.append(" ")
                    else:
                        res.append(char)
                        diff_found = True
                        last_perm[i] = char
                sys.stdout.write("".join(res) + "\n")
                return

            for i in range(n):
                if not used[i]:
                    person_char = chr(65 + i)
                    # Position is depth + 1
                    if (depth + 1) not in disallowed[i]:
                        used[i] = True
                        current_perm[depth] = person_char
                        backtrack(depth + 1)
                        used[i] = False

        backtrack(0)

if __name__ == "__main__":
    solve()
