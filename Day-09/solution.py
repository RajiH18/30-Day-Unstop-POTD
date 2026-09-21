def analyze_depth_readings(n, W, depths):
    from collections import deque

    dq = deque()
    freq = {}
    distinct_count = 0
    results = []

    for i in range(n):
        value = depths[i]

        
        freq[value] = freq.get(value, 0) + 1

        if freq[value] == 1:
            distinct_count += 1

        
        while dq and depths[dq[-1]] <= value:
            dq.pop()

        dq.append(i)

       
        window_start = i - W + 1

        while dq and dq[0] < window_start:
            dq.popleft()

        
        if i >= W:
            old_value = depths[i - W]

            freq[old_value] -= 1

            if freq[old_value] == 0:
                del freq[old_value]
                distinct_count -= 1

        if i >= W - 1:
            peak = depths[dq[0]]
            results.append((peak, distinct_count))

    return results


def main():
    import sys

    data = sys.stdin.read().strip().split()

    n = int(data[0])
    W = int(data[1])

    depths = list(map(int, data[2:2 + n]))

    results = analyze_depth_readings(n, W, depths)

    for peak, distinct_count in results:
        print(peak, distinct_count)


if __name__ == "__main__":
    main()