import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    pointer = 1
    for _ in range(t):
        n = int(input_data[pointer])
        s = input_data[pointer+1]
        pointer += 2
        
        # Count how many times the character changes
        transitions = 0
        for i in range(n - 1):
            if s[i] != s[i+1]:
                transitions += 1
        
        # If there's exactly 1 transition, it reduces to "01" or "10"
        if transitions == 1:
            minwf = 2
        else:
            minwf = 1
            
        results.append(str(minwf))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()