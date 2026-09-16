def calculate_peak_readings(n, k, readings):
    # Placeholder function for user logic
    peaks = []
    # User should implement their logic here
    dq = []     
    front = 0 


    for i in range(n):

       
        while front < len(dq) and dq[front] <= i - k:
            front += 1

        
        while len(dq) > front and readings[dq[-1]] <= readings[i]:
            dq.pop()

        
        dq.append(i)

        
        if i >= k - 1:
            peaks.append(readings[dq[front]])

    return peaks

if __name__ == '__main__':
    n, k = map(int, input().split())
    readings = list(map(int, input().split()))
    
    result = calculate_peak_readings(n, k, readings)
    
    print(' '.join(map(str, result)))
