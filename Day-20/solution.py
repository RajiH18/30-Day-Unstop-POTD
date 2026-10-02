def user_logic(n, K, entries):
   
    wait_values = [-1] * n

    
    team_stacks = {}

    for i in range(n):
        team, rating = entries[i]

        if team not in team_stacks:
            team_stacks[team] = []

        stack = team_stacks[team]

        
        while stack and entries[stack[-1]][1] < rating:
            previous = stack.pop()
            wait_values[previous] = i - previous

        stack.append(i)

    
    candidates = []

    for i in range(n):
        if wait_values[i] != -1:
            candidates.append((wait_values[i], i))

    
    candidates.sort(key=lambda x: (-x[0], x[1]))

    
    leaderboard_positions = []

    for i in range(min(K, len(candidates))):
        position = candidates[i][1] + 1
        leaderboard_positions.append(position)

    return wait_values, leaderboard_positions


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    K = int(data[1])
    entries = [(int(data[i*2+2]), int(data[i*2+3])) for i in range(n)]
    wait_values, leaderboard_positions = user_logic(n, K, entries)
    print(" ".join(map(str, wait_values)))
    print(" ".join(map(str, leaderboard_positions)))


if __name__ == "__main__":
    main()