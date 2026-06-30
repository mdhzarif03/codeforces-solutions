import sys

def solve():
    # Read all inputs from standard input at once for maximum speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    pointer = 1
    for _ in range(t):
        x = int(input_data[pointer])
        y = int(input_data[pointer+1])
        pointer += 2
        
        # If x is divisible by y, it's always possible
        if x % y == 0:
            results.append("YES")
        else:
            results.append("NO")
            
    # Print all results separated by a newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()