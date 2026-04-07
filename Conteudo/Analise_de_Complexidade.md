# Análise de complexidade
### Apenas ao analizar as restrições do problema, já podemos ter uma noção da solução esperada.

| Tamanho de N | Complexidade Máxima Aceita | Abordagem/Algoritmo Esperado                                                                               |
|--------------|----------------------------|------------------------------------------------------------------------------------------------------------|
| N≤20         | O(O!) ou O(2N)             | "Força Bruta Pura. Backtracking, recursão exaustiva, Bitmask."                                             |
| N≤100        | O(N3) ou O(N4)             | "Força Bruta com 3 laços. Grafos com Floyd-Warshall, DP 3D."                                               |
| N≤1.000      | O(N2)                      | "Força Bruta Otimizada. Laços duplos. Programação Dinâmica 2D, travessia de matrizes."                     |
| N≤105 a 106  | O(NlogN) ou O(N)           | "Otimização Pesada. Ordenação, Busca Binária, Two Pointers, Sweep Line, Grafos (BFS/DFS), Prefix Sum."     |
| N≥109        | O(logN) ou O(1)            | "Matemática. Busca Binária pura, Teoria dos Números, ou fórmulas diretas. Esqueça laços for tradicionais." |
