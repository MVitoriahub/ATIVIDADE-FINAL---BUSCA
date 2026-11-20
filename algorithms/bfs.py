from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):
    """Busca em Largura (Breadth-First Search) em grafo.

    Expande os nós por níveis usando uma fila FIFO. Com custo uniforme (1 por
    movimento), encontra a solução de menor número de movimentos (ótima).
    O teste de objetivo é feito na geração do nó.
    """

    def search(self, initial: State) -> SearchResult:
        if not initial.is_solvable:
            return SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        nodes_generated = 1

        if initial.is_goal:
            return SearchResult(solution=initial, nodes_generated=nodes_generated,
                                max_frontier_size=1, depth=initial.cost)

        frontier = deque([initial])
        reached = {initial.tiles}          # estados já gerados (fronteira + explorados)
        nodes_expanded = 0
        max_frontier_size = 1

        while frontier:
            node = frontier.popleft()
            nodes_expanded += 1

            for child in node.neighbors():
                nodes_generated += 1
                if child.tiles in reached:
                    continue
                if child.is_goal:
                    return SearchResult(
                        solution=child,
                        nodes_expanded=nodes_expanded,
                        nodes_generated=nodes_generated,
                        max_frontier_size=max_frontier_size,
                        depth=child.cost,
                    )
                reached.add(child.tiles)
                frontier.append(child)

            max_frontier_size = max(max_frontier_size, len(frontier))

        return SearchResult(solution=None, nodes_expanded=nodes_expanded,
                            nodes_generated=nodes_generated,
                            max_frontier_size=max_frontier_size)
