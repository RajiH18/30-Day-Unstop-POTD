from bisect import bisect_left, bisect_right


def user_logic(n, k, scores):
    
    values = sorted(set(scores))
    size = len(values)

    
    bit = [0] * (size + 1)

    def update(index):
        while index <= size:
            bit[index] += 1
            index += index & -index

    def query(index):
        total = 0

        while index > 0:
            total += bit[index]
            index -= index & -index

        return total

    results = []

    for score in scores:
        
        left = bisect_left(values, score - k)
        right = bisect_right(values, score + k)

        
        count = query(right) - query(left)
        results.append(count)

        
        position = bisect_left(values, score) + 1
        update(position)

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    k = int(data[1])
    
    scores = list(map(int, data[2:n + 2]))
    
    results = user_logic(n, k, scores)
    
    for result in results:
        print(result)


if __name__ == "__main__":
    main()