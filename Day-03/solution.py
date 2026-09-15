def user_logic(n, edges, queries):
    """
    Write your logic here.
    Parameters:
        n (int): Number of junctions.
        edges (list of tuple): List of edges connecting junctions.
        queries (list of tuple): List of queries to handle events.
    Returns:
        list of int: Result for each query of type 2.
    """
    # Placeholder for user logic
    # Return a list of integers, each representing the result of a type 2 query
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)

    stack = [1]
    parent[1] = -1
    stack_order = []

    while stack:
        node = stack.pop()
        stack_order.append(node)

        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                depth[neighbor] = depth[node] + 1
                stack.append(neighbor)
        
    size = [1] * (n + 1)

    for node in reversed(stack_order):
        if parent[node] != -1:
            size[parent[node]] += size[node]

        
    heavy = [-1] * (n + 1)

    for node in range(1, n + 1):
        largest_size = 0

        for neighbor in graph[node]:
            if parent[neighbor] == node:
                if size[neighbor] > largest_size:
                    largest_size = size[neighbor]
                    heavy[node] = neighbor

    head = [0] * (n + 1)
    position = [0] * (n + 1)

    current_position = 0

    stack = [(1, 1)]

    while stack:
        node, chain_head = stack.pop()

        while node != -1:
            head[node] = chain_head
            position[node] = current_position
            current_position += 1

            for neighbor in graph[node]:
                if parent[neighbor] == node and neighbor != heavy[node]:
                    stack.append((neighbor, neighbor))

            node = heavy[node]

    fenwick = [0] * (n + 1)

    def fenwick_add(index, value):
        index += 1

        while index <= n:
            fenwick[index] += value
            index += index & -index

    def fenwick_sum(index):
        total = 0
        index += 1

        while index > 0:
            total += fenwick[index]
            index -= index & -index

        return total

    def range_sum(left, right):
        if left > right:
            return 0

        return fenwick_sum(right) - fenwick_sum(left - 1)

    
    state = [0] * (n + 1)

    for node in range(2, n + 1):
        state[node] = 1
        fenwick_add(position[node], 1)

        
    def query_path(u, v):
        total = 0

        while head[u] != head[v]:

            if depth[head[u]] < depth[head[v]]:
                u, v = v, u

            total += range_sum(position[head[u]], position[u])

            u = parent[head[u]]

       
        if depth[u] > depth[v]:
            u, v = v, u

        
        total += range_sum(position[u] + 1, position[v])

        return total

   
    results = []

    for query in queries:

        if query[0] == 1:
            
            v = query[1]

            if state[v] == 1:
                state[v] = 0
                fenwick_add(position[v], -1)
            else:
                state[v] = 1
                fenwick_add(position[v], 1)

        else:
           
            u = query[1]
            v = query[2]

            results.append(query_path(u, v))

    return results

    # Temporary return
    return []


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    n = int(data[index])  
    index += 1
    
    edges = []
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    q = int(data[index])  
    index += 1
    
    queries = []
    for _ in range(q):
        query_type = int(data[index])
        if query_type == 1:
            v = int(data[index + 1])
            queries.append((query_type, v))
            index += 2
        elif query_type == 2:
            u = int(data[index + 1])
            v = int(data[index + 2])
            queries.append((query_type, u, v))
            index += 3

   
    results = user_logic(n, edges, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
