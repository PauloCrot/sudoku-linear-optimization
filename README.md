# Sudoku Solver - Otimização Linear Contínua 

Este projeto apresenta um solucionador de Sudoku desenvolvido em Python utilizando a biblioteca **PuLP**. 

O diferencial deste projeto é demonstrar, na prática, um conceito de Pesquisa Operacional: como um problema originalmente de Programação Linear Inteira (onde as decisões são binárias, 0 ou 1) pode ser resolvido de forma exata utilizando Programação Linear Contínua (onde as variáveis podem assumir qualquer valor fracionário entre 0 e 1), desde que o desafio possua uma solução única.

Relaxação Linear e Unimodularidade

A modelagem tradicional do Sudoku exige variáveis binárias ($x_{ijk} \in \{0, 1\}$) para determinar se a célula $(i,j)$ contém o dígito $k$. No entanto, este algoritmo define as variáveis como contínuas:

$$0 \le x_{ijk} \le 1$$


### Por que o modelo contínuo encontra uma solução inteira?
A estrutura das restrições do Sudoku (garantir um único dígito por célula, linha, coluna e bloco) compartilha propriedades com matrizes **Totalmente Unimodulares** e poliedros cujos pontos extremos (vértices) são garantidamente inteiros. Quando o desafio possui apenas uma solução válida, essa solução inteira é o único ponto extremo viável do poliedro. Portanto, qualquer algoritmo de Programação Linear (como o Simplex) convergirá diretamente para a solução inteira, sem a necessidade de ramificações complexas (Branch and Bound).

---

## Tecnologias Utilizadas

* **Python 3**
* **PuLP** (Biblioteca de modelagem de otimização matemática)

---

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/PauloCrot/sudoku-linear-optimization.git](https://github.com/PauloCrot/sudoku-linear-optimization.git)
   cd sudoku-linear-optimization