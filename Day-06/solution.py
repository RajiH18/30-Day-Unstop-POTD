def longest_steady_window(speed, n, limit):
    left = 0
    answer = 0

    min_dq = []
    max_dq = []

    for right in range(n):

        while min_dq and speed[min_dq[-1]] >= speed[right]:
            min_dq.pop()
        min_dq.append(right)

        while max_dq and speed[max_dq[-1]] <= speed[right]:
            max_dq.pop()
        max_dq.append(right)

        while speed[max_dq[0]] - speed[min_dq[0]] > limit:
            if min_dq[0] == left:
                min_dq.pop(0)

            if max_dq[0] == left:
                max_dq.pop(0)

            left += 1

        current_length = right - left + 1

        if current_length > answer:
            answer = current_length

    return answer


if __name__ == '__main__':
    n, limit = map(int, input().split())
    speed = list(map(int, input().split()))
    result = longest_steady_window(speed, n, limit)
    print(result)