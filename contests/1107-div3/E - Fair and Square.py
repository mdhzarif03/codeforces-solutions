import sys
import math

# Increase recursion depth for deep tree traversals
sys.setrecursionlimit(300000)

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(math.isqrt(n))
    return r * r == n

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1
            
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
            
        subtree_size = [0] * (n + 1)
        
        # Iterative DFS or manual stack to avoid recursion overhead in Python
        # Order of nodes for post-order processing
        order = []
        stack = [1]
        parent = [0] * (n + 1)
        visited = [False] * (n + 1)
        visited[1] = True
        
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
                    
        # Compute subtree sizes in reverse post-order
        for u in reversed(order):
            subtree_size[u] = 1
            for v in adj[u]:
                if v != parent[u]:
                    subtree_size[u] += subtree_size[v]
                    
        total_good_triplets = 0
        
        for u in range(1, n + 1):
            if not is_perfect_square(a[u]):
                continue
                
            component_sizes = []
            sum_of_children = 0
            
            for v in adj[u]:
                if v != parent[u]:
                    component_sizes.append(subtree_size[v])
                    sum_of_children += subtree_size[v]
                    
            parent_component_size = n - 1 - sum_of_children
            if parent_component_size > 0:
                component_sizes.append(parent_component_size)
                
            S1 = 0
            S2 = 0
            S3 = 0
            for s in component_sizes:
                S1 += s
                S2 += s * s
                S3 += s * s * s
                
            # Ways to choose 3 nodes from 3 completely distinct branches
            ways_3 = (S1 * S1 * S1 - 3 * S1 * S2 + 2 * S3) // 6
            # Ways to choose node 'u' itself, and 2 nodes from 2 distinct branches
            ways_2 = (S1 * S1 - S2) // 2
            
            total_good_triplets += (ways_3 + ways_2)
            
        out.append(str(total_good_triplets))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()