def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row):
        if row == n:
            solution = [''.join(row) for row in board]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

def solve_n_queens_heuristic(n):
    import random

    def min_conflicts(board, n, max_steps=1000):
        for i in range(n):
            board[i] = random.randint(0, n-1)
        
        for _ in range(max_steps):
            conflicts = []
            for row in range(n):
                cnt = 0
                for r in range(n):
                    if r == row:
                        continue
                    if board[r] == board[row] or abs(r - row) == abs(board[r] - board[row]):
                        cnt += 1
                if cnt > 0:
                    conflicts.append(row)
            
            if not conflicts:
                return board
            
            row = random.choice(conflicts)
            min_conf = float('inf')
            best_cols = []
            for col in range(n):
                if col == board[row]:
                    continue
                cnt = 0
                for r in range(n):
                    if r == row:
                        continue
                    if board[r] == col or abs(r - row) == abs(board[r] - col):
                        cnt += 1
                if cnt < min_conf:
                    min_conf = cnt
                    best_cols = [col]
                elif cnt == min_conf:
                    best_cols.append(col)
            
            board[row] = random.choice(best_cols)
        
        return None

    board = [0] * n
    solution = min_conflicts(board, n)
    if solution:
        res = [['.' for _ in range(n)] for _ in range(n)]
        for row in range(n):
            res[row][solution[row]] = 'Q'
        return [''.join(r) for r in res]
    return []

import time
def compare_algorithms(n=8):
    start = time.time()
    backtrack_sol = solve_n_queens(n)
    backtrack_time = time.time() - start
    
    start = time.time()
    heuristic_sol = solve_n_queens_heuristic(n)
    heuristic_time = time.time() - start
    
    print(f"=== {n}皇后算法对比 ===")
    print(f"回溯法：找到 {len(backtrack_sol)} 个解，耗时 {backtrack_time:.4f}s")
    print(f"最小冲突法：找到 1 个解，耗时 {heuristic_time:.4f}s")
    if heuristic_sol:
        print("最小冲突法解示例：")
        for row in heuristic_sol:
            print(row)

if __name__ == "__main__":
    n = 8
    results = solve_n_queens(n)
    print(f"八皇后问题（回溯法）共有 {len(results)} 种解法")
    print("\n第一种解法：")
    for row in results[0]:
        print(row)
    
    print("\n" + "="*50)
    compare_algorithms(8)
    print("\n" + "="*50)
    compare_algorithms(100)