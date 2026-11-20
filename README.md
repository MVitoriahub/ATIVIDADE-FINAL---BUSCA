# 8-Puzzle — Busca em Espaço de Estados

## O que implementar

### `puzzle/state.py`
- `neighbors()` — gera os estados filhos a partir do espaço vazio
- `path()` — reconstrói a sequência de estados do inicial até este
- `actions()` — retorna a sequência de ações usando `path()`

### `algorithms/bfs.py`
- `BFS.search(initial)` — Busca em Largura

### `algorithms/dfs.py`
- `DFS.search(initial)` — Busca em Profundidade

### `algorithms/a_star.py`
- `AStar.heuristic(state)` — função heurística admissível
- `AStar.search(initial)` — Busca A*

## Estrutura

```
├── puzzle/
│   ├── state.py        # State — IMPLEMENTAR neighbors, path, actions
│   ├── result.py       # SearchResult — não alterar
│   └── base_search.py  # Interface BaseSearch — não alterar
├── algorithms/
│   ├── bfs.py          ← IMPLEMENTAR
│   ├── dfs.py          ← IMPLEMENTAR
│   └── a_star.py       ← IMPLEMENTAR
└── main.py
```


## Implementação

- **Ações:** nomeadas pelo movimento do espaço vazio (`UP`, `DOWN`, `LEFT`, `RIGHT`), custo 1 por movimento.
- **BFS:** fila FIFO + conjunto de estados alcançados; teste de objetivo na geração. Ótima (menor nº de movimentos).
- **DFS:** pilha LIFO com limite de profundidade (padrão 50); um estado só é revisitado se alcançado por caminho mais curto. Não é ótima.
- **A\*:** `f(n) = g(n) + h(n)` com heurística da **distância de Manhattan** (admissível e consistente). Ótima.
- **Solubilidade:** `State.is_solvable` verifica a paridade das inversões; estados insolúveis retornam "não encontrado" imediatamente.
  O exemplo original do `main.py` `(2, 8, 3, 1, 6, 4, 7, 0, 5)` é insolúvel para o objetivo `1 2 3 / 4 5 6 / 7 8 _`.

## Executar

```bash
python main.py
python -m pytest -q
```
