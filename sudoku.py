from pulp import *

# Tabuleiro de teste sabidamente VÁLIDO e VIÁVEL
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Definir o problema de otimização linear
prob = LpProblem("Sudoku_Solver", LpMinimize)

rows = range(9)
cols = range(9)
digits = range(1, 10)

# Variáveis de decisão contínuas
x = LpVariable.dicts("x", (rows, cols, digits), 0, 1, LpContinuous)

# Função objetivo nula
prob += 0, "Arbitrary Objective"

# 1. Cada célula deve conter exatamente um dígito
for r in rows:
    for c in cols:
        prob += lpSum([x[r][c][k] for k in digits]) == 1

# 2. Cada linha deve conter cada dígito exatamente uma vez
for r in rows:
    for k in digits:
        prob += lpSum([x[r][c][k] for c in cols]) == 1

# 3. Cada coluna deve conter cada dígito exatamente uma vez
for c in cols:
    for k in digits:
        prob += lpSum([x[r][c][k] for r in rows]) == 1

# 4. Cada bloco 3x3 deve conter cada dígito exatamente uma vez
for block_row in range(3):
    for block_col in range(3):
        for k in digits:
            prob += lpSum([
                x[r][c][k] 
                for r in range(block_row * 3, (block_row + 1) * 3)
                for c in range(block_col * 3, (block_col + 1) * 3)
            ]) == 1

# 5. Restrições para as pistas iniciais
for r in rows:
    for c in cols:
        if sudoku_grid[r][c] != 0:
            val = sudoku_grid[r][c]
            prob += x[r][c][val] == 1

# Executar o solver
prob.solve()

print("Status:", LpStatus[prob.status])

if prob.status == 1:
    print("\nSolução do Sudoku:")
    for r in rows:
        linha_resolvida = []
        for c in cols:
            for k in digits:
                if x[r][c][k].varValue and x[r][c][k].varValue > 0.99:
                    linha_resolvida.append(k)
        print(linha_resolvida)
else:
    print("Nenhuma solução encontrada.")