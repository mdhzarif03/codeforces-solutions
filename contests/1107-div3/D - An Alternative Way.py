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
        pointer += 1
        
        a = [int(x) for x in input_data[pointer : pointer + n]]
        pointer += n
        b = [int(x) for x in input_data[pointer : pointer + n]]
        pointer += n
        
        maxE = 0
        maxO = 0
        iswf = "YES"
        
        for i in range(1, n + 1):
            # Calculate f_i with alternating sign
            diff = b[i-1] - a[i-1]
            f_i = diff if i % 2 == 0 else -diff
            
            if i % 2 != 0:  # i is odd
                # Even operations cannot start, so E_i <= E_{i-1}
                # Also E_i must be >= max(0, f_i)
                if max(0, f_i) > maxE:
                    iswf = "NO"
                    break
                # Carry forward the maximum possible constraints
                maxO = maxE - f_i
            else:  # i is even
                # Odd operations cannot start, so O_i <= O_{i-1}
                # Also O_i must be >= max(0, -f_i)
                if max(0, -f_i) > maxO:
                    iswf = "NO"
                    break
                # Carry forward the maximum possible constraints
                maxE = maxO + f_i
                
        results.append(iswf)
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()