def user_logic(n, m, belt, requirements):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the belt.
        m (int): Number of distinct required component types.
        belt (str): String containing the belt sequence.
        requirements (dict): Dictionary with component type as key and required count as value.
    Returns:
        int: Length of the shortest valid grab, or -1 if no grab can satisfy all requirements.
    """
    left = 0
    answer = n + 1

    current = {}
    satisfied = 0

    for right in range(n):
        char = belt[right]

        if char in requirements:
            current[char] = current.get(char, 0) + 1

            if current[char] == requirements[char]:
                satisfied += 1
        
        while satisfied == m:
            window_length = right - left + 1

            if window_length < answer:
                answer = window_length

            left_char = belt[left]
            if left_char in requirements:
                current[left_char] -= 1

                if current[left_char] < requirements[left_char]:
                    satisfied -= 1

            left += 1

    if answer == n + 1:
        return -1

    return answer

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Belt length
    m = int(data[1])  # Number of distinct required component types
    
    belt = data[2]  # Belt sequence
    
    requirements = {}
    index = 3
    for _ in range(m):
        component_type = data[index]  # Component type
        count = int(data[index + 1])  # Required count
        requirements[component_type] = count
        index += 2
    
    # Call user logic function and print the output
    result = user_logic(n, m, belt, requirements)
    print(result)

if __name__ == "__main__":
    main()