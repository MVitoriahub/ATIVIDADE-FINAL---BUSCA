import heapq
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult

# Posição (linha, coluna) de cada peça no estado objetivo
_GOAL_POSITION = {tile: divmod(i, 3) for i, tile in enumerate(GOAL_STATE)}


class AStar(BaseSearch):
    """Busca A* com f(n) = g(n) + h(n).

    g(n): custo do caminho até n (número de movimentos).
    h(n): soma das distâncias de Manhattan de cada peça até sua posição no
          objetivo (o espaço vazio não é contado). É admissível e consistente,
          portanto o A* em grafo encontra a solução ótima.
    """

    def heuristic(self, state: State) -> int:
        distance = 0
        for i, tile in enumerate(state.tiles):
            if tile == 0:
                continue
            row, col = divmod(i, 3)
            goal_row, goal_col = _GOAL_POSITION[tile]
            distance += abs(row - goal_row) + abs(col - goal_col)
        return distance

    def search(self, initial: State) -> SearchResult:
        if not initial.is_solvable:
            return SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        tie = count()   # desempate estável (FIFO) para valores de f e h iguais
        h0 = self.heuristic(initial)
        frontier = [(initial.cost + h0, h0, next(tie), initial)]
        best_g = {initial.tiles: initial.cost}
        closed = set()
        nodes_generated = 1
        nodes_expanded = 0
        max_frontier_size = 1

        while frontier:
            _, _, _, node = heapq.heappop(frontier)

            if node.tiles in closed:
                continue                    # entrada obsoleta na fila

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=node.cost,
                )

            closed.add(node.tiles)
            nodes_expanded += 1

            for child in node.neighbors():
                nodes_generated += 1
                if child.tiles in closed:
                    continue
                if child.cost < best_g.get(child.tiles, float("inf")):
                    best_g[child.tiles] = child.cost
                    h = self.heuristic(child)
                    heapq.heappush(frontier, (child.cost + h, h, next(tie), child))

            max_frontier_size = max(max_frontier_size, len(frontier))

        return SearchResult(solution=None, nodes_expanded=nodes_expanded,
                            nodes_generated=nodes_generated,
                            max_frontier_size=max_frontier_size)
