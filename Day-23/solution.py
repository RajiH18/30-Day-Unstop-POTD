def calculate_max_profit(orders):
    import heapq

    
    orders.sort(key=lambda x: x[1])

    selected = []

    for profit, deadline in orders:
        
        heapq.heappush(selected, profit)

       
        if len(selected) > deadline:
           
            heapq.heappop(selected)

    max_profit = sum(selected)
    num_accepted_orders = len(selected)

    return max_profit, num_accepted_orders


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0]) 
    orders = []
    index = 1
    for _ in range(n):
        p = int(data[index])
        d = int(data[index + 1])
        orders.append((p, d))
        index += 2

    
    max_profit, num_accepted_orders = calculate_max_profit(orders)
    print(max_profit, num_accepted_orders)


if __name__ == "__main__":
    main()