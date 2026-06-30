import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx+1]
        idx += 2
        
        total_inv = 0
        zeros_count = 0
        for char in reversed(s):
            if char == '0':
                zeros_count += 1
            else:
                total_inv += zeros_count

        core = s.lstrip('0').rstrip('1')
        
        if not core:
            out.append("Bob")
        elif total_inv % 2 == 1:
            out.append("Alice")
        else:
            o = core.count('1')
            z = core.count('0')
            if o % 2 == 0 and z % 2 == 0:
                out.append("Bob")
            else:
                out.append("Alice")
                
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()