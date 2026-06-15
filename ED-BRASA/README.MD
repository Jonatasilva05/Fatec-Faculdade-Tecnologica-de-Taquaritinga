# Estrutura de Dados

## Descrição

A disciplina de **Estrutura de Dados** é essencial para o desenvolvimento de soluções de software eficientes. Estruturas de dados são a base para a organização e manipulação de informações em sistemas computacionais, desempenhando um papel crucial no desempenho de algoritmos e sistemas.

### Para que serve:
Esta matéria prepara os alunos para compreender como organizar dados de maneira eficiente, abordando as estruturas essenciais que possibilitam manipulação, armazenamento e recuperação de informações. O aprendizado é vital para quem trabalha com programação, algoritmos e desenvolvimento de sistemas complexos.

### Onde será tratada e utilizada:
- **Desenvolvimento de Software**: Utilização em projetos de software onde a performance é crítica, como sistemas bancários, jogos e aplicações em tempo real.
- **Análise de Algoritmos**: Avaliação e implementação de algoritmos eficientes para tarefas como pesquisa, ordenação e processamento de grandes volumes de dados.
- **Inteligência Artificial**: Muitas técnicas de IA (como redes neurais) dependem do conhecimento em estruturas de dados para otimizar os cálculos e operações.

## Objetivos:
- Compreender os principais tipos de estruturas de dados.
- Implementar e manipular diferentes estruturas de dados.
- Analisar a complexidade de algoritmos e avaliar o impacto das escolhas de estrutura.

---

## Principais Estruturas de Dados:

1. **Arrays / Vetores**:
   - Estrutura básica para armazenamento sequencial de dados.
   - Acesso rápido, mas com limitações para inserção/remover.

2. **Listas Ligadas**:
   - **Simples** e **Duplas**: Cada elemento aponta para o próximo. Operações de inserção e remoção são eficientes, mas o acesso é mais lento.
   - **Circular**: O último elemento aponta para o primeiro, formando um ciclo.

3. **Pilha (Stack)**:
   - Estrutura **LIFO** (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido.
   - Usada em chamadas de função e algoritmos recursivos.

4. **Fila (Queue)** e **Fila Dupla (Deque)**:
   - **FIFO** (First In, First Out), onde o primeiro elemento inserido é o primeiro a ser removido.
   - Fila Dupla permite inserção e remoção de ambos os lados.

5. **Tabela Hash (Hash Table)**:
   - Estrutura que usa funções de hash para mapear chaves para valores, proporcionando operações rápidas (inserção, busca).

6. **Árvores**:
   - **Árvore Binária**: Cada nó tem no máximo dois filhos.
   - **Árvore de Busca Binária (BST)**: Estrutura ordenada para facilitar a busca.
   - **Árvores balanceadas** (como **AVL** e **Red-Black**): Garantem que a árvore permaneça equilibrada para buscas eficientes.
   - **B-tree e Trie**: Utilizadas em sistemas de banco de dados e busca de prefixos.

7. **Heap (Min/Max Heap)**:
   - Árvore binária onde o valor de cada nó é maior (ou menor) que os seus filhos. Usada principalmente em filas de prioridade.

8. **Grafos**:
   - Representações de grafos podem ser feitas por listas de adjacência ou matrizes de adjacência.
   - Grafos são fundamentais para algoritmos como **Busca em Largura (BFS)**, **Busca em Profundidade (DFS)** e **algoritmos de caminho mínimo** como Dijkstra.

---

## Operações Comuns

- **Inserção**: Adicionar um elemento à estrutura.
- **Remoção**: Remover um elemento da estrutura.
- **Busca**: Localizar um elemento na estrutura.
- **Atualização**: Modificar um elemento existente.
- **Iteração**: Percorrer os elementos da estrutura.
- **Ordenação e Busca**: Algoritmos como QuickSort, MergeSort, HeapSort, Busca Binária.

---

## Complexidade (Ordem de Grandeza):

- **Array**:
  - Acesso: O(1)
  - Inserção/Remoção: O(n)
  
- **Lista Ligada**:
  - Acesso: O(n)
  - Inserção/Remoção: O(1) (com ponteiro)
  
- **Pilha/Fila**:
  - Push/Pop: O(1)
  
- **Tabela Hash**:
  - Busca/Inserção: O(1) (média), O(n) (pior caso)
  
- **Árvore Binária Balanceada (BST)**:
  - Busca/Inserção: O(log n)
  
- **Heap**:
  - Inserção: O(log n)
  - Extrair min/max: O(log n)
  
- **Grafos (BFS/DFS)**:
  - O(V + E), onde V é o número de vértices e E é o número de arestas.

---

## Boas Práticas:

- **Escolher a estrutura certa**: Baseado na operação mais crítica para o problema, como inserção rápida, busca ou acesso sequencial.
- **Considerar a complexidade de memória**: Algumas estruturas são mais eficientes em termos de espaço, outras em termos de tempo.
- **Analisar casos médio/pior**: Entender o comportamento das estruturas em diferentes cenários.
- **Testes de desempenho**: Sempre que possível, meça o desempenho real das operações em seu código.

---

## Dicas de Estudo:

- **Implementar do zero**: Crie suas próprias implementações de cada estrutura para entender como funcionam.
- **Praticar problemas**: Use plataformas como [LeetCode](https://leetcode.com/), [SPOJ](https://www.spoj.com/), [HackerRank](https://www.hackerrank.com/) para resolver problemas práticos.
- **Visualizar operações**: Use ferramentas que permitem visualizar animações de estruturas de dados (como [VisuAlgo](https://visualgo.net/en)) para entender melhor o comportamento de cada estrutura.

---

## Materiais de Estudo:

- **Artigos**: [Geeks for Geeks](https://www.geeksforgeeks.org/)
- **Ferramentas**: IDEs como Visual Studio Code ou IntelliJ IDEA para implementação.
  
## Livros Recomendados:

- "Estruturas de Dados e Algoritmos em C" - Mark Allen Weiss
- "Introduction to Algorithms" - Thomas H. Cormen