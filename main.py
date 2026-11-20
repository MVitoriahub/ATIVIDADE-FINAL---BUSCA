"""Script de demonstração — útil para depurar manualmente."""

from puzzle.state import State
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.a_star import AStar


def print_result(name: str, result):
    print(f"\n{'='*40}")
    print(f"Algoritmo : {name}")
    if result.found:
        print(f"Solução   : {' → '.join(result.actions)}")
        print(f"Custo     : {result.path_cost}")
        print(f"Profund.  : {result.depth}")
    else:
        print("Solução   : NÃO ENCONTRADA")
    print(f"Expandidos: {result.nodes_expanded}")
    print(f"Gerados   : {result.nodes_generated}")
    print(f"Fronteira : {result.max_frontier_size} (máx)")


def run(initial: State):
    print("\nEstado inicial:")
    print(initial)
    if not initial.is_solvable:
        print("(estado insolúvel para o objetivo 1 2 3 / 4 5 6 / 7 8 _)")

    print_result("BFS",  BFS().search(initial))
    print_result("DFS",  DFS().search(initial))
    print_result("A*",   AStar().search(initial))


if __name__ == "__main__":
    # Exemplo original do template: tem número ímpar de inversões, portanto
    # é insolúvel para GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0).
    run(State((2, 8, 3, 1, 6, 4, 7, 0, 5)))

    # Exemplo solúvel (solução ótima com 20 movimentos)
    run(State((2, 5, 3, 8, 6, 7, 4, 1, 0)))
