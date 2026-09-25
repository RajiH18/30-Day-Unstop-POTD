def compute_exposure_scores(n, hourly_readings, Q, review_windows):
    MOD = 1000000007

    queries_by_r = [[] for _ in range(n)]

    for query_index, (l, r) in enumerate(review_windows):
        queries_by_r[r - 1].append((l - 1, query_index))

    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def update(node, start, end, left, right, value):
        if left > end or right < start:
            return

        if left <= start and end <= right:
            tree[node] += value * (end - start + 1)
            lazy[node] += value
            return

        mid = (start + end) // 2

        update(node * 2, start, mid, left, right, value)
        update(node * 2 + 1, mid + 1, end, left, right, value)

        tree[node] = (
            tree[node * 2]
            + tree[node * 2 + 1]
            + lazy[node] * (end - start + 1)
        )

    def query(node, start, end, left, right, carry=0):
        if left > end or right < start:
            return 0

        if left <= start and end <= right:
            return tree[node] + carry * (end - start + 1)

        mid = (start + end) // 2
        new_carry = carry + lazy[node]

        return (
            query(node * 2, start, mid, left, right, new_carry)
            + query(node * 2 + 1, mid + 1, end, left, right, new_carry)
        )

    results = [0] * Q

    stack = []

    for r in range(n):
        current = hourly_readings[r]
        end_position = r - 1

        while stack and stack[-1][0] <= current:
            old_value, start_position = stack.pop()

            if start_position <= end_position:
                update(
                    1,
                    0,
                    n - 1,
                    start_position,
                    end_position,
                    current - old_value
                )

            end_position = start_position - 1

        stack.append((current, end_position + 1))

        # Starting exactly at r
        update(
            1,
            0,
            n - 1,
            r,
            r,
            current
        )

        for left, query_index in queries_by_r[r]:
            results[query_index] = (
                query(1, 0, n - 1, left, r) % MOD
            )

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    hourly_readings = list(map(int, data[idx:idx+n]))
    idx += n
    Q = int(data[idx])
    idx += 1
    review_windows = []
    for _ in range(Q):
        l = int(data[idx])
        r = int(data[idx+1])
        review_windows.append((l, r))
        idx += 2
    results = compute_exposure_scores(n, hourly_readings, Q, review_windows)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()