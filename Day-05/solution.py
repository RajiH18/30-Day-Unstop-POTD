def longest_affordable_streak(cost, n, budget):
    # User logic goes here
    left = 0
    total = 0
    answer = 0

    for right in range(n):
        total += cost[right]

        while total > budget:
            total -= cost[left]
            left += 1

        current_length = right - left + 1

        if current_length > answer:
            answer = current_length

    return answer
     # Placeholder return value

if __name__ == "__main__":
    n, budget = map(int, input().split())
    cost = list(map(int, input().split()))

    result = longest_affordable_streak(cost, n, budget)
    print(result)
