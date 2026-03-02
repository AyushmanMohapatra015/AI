from collections import deque
import time

class MissionariesCannibals:
    def __init__(self):
        self.start = (3, 3, 1)
        self.goal = (0, 0, 0)

    # Check if state is valid
    def is_valid(self, state):
        M, C, _ = state
        M_right = 3 - M
        C_right = 3 - C

        if M < 0 or C < 0 or M > 3 or C > 3:
            return False

        if M > 0 and C > M:
            return False

        if M_right > 0 and C_right > M_right:
            return False

        return True

    # Generate successor states
    def get_successors(self, state):
        M, C, boat = state
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        successors = []

        for m, c in moves:
            if boat == 1:
                new_state = (M - m, C - c, 0)
            else:
                new_state = (M + m, C + c, 1)

            if self.is_valid(new_state):
                successors.append(new_state)

        return successors

    # ---------------- BFS ----------------
    def bfs(self):
        start_time = time.time()
        queue = deque([(self.start, [])])
        visited = set()
        nodes_expanded = 0

        while queue:
            state, path = queue.popleft()
            nodes_expanded += 1

            if state == self.goal:
                end_time = time.time()
                return path + [state], nodes_expanded, end_time - start_time

            if state not in visited:
                visited.add(state)

                for successor in self.get_successors(state):
                    queue.append((successor, path + [state]))

        return None, nodes_expanded, 0

    # ---------------- DFS ----------------
    def dfs(self):
        start_time = time.time()
        stack = [(self.start, [])]
        visited = set()
        nodes_expanded = 0

        while stack:
            state, path = stack.pop()
            nodes_expanded += 1

            if state == self.goal:
                end_time = time.time()
                return path + [state], nodes_expanded, end_time - start_time

            if state not in visited:
                visited.add(state)

                for successor in self.get_successors(state):
                    stack.append((successor, path + [state]))

        return None, nodes_expanded, 0

    # ---------------- Depth Limited Search ----------------
    def dls(self, state, path, depth_limit, visited):
        if state == self.goal:
            return path + [state]

        if depth_limit <= 0:
            return None

        visited.add(state)

        for successor in self.get_successors(state):
            if successor not in visited:
                result = self.dls(successor, path + [state], depth_limit - 1, visited)
                if result:
                    return result

        return None

    # ---------------- Iterative Deepening ----------------
    def iddfs(self, max_depth):
        start_time = time.time()
        nodes_expanded = 0

        for depth in range(max_depth + 1):
            visited = set()
            result = self.dls(self.start, [], depth, visited)
            nodes_expanded += len(visited)

            if result:
                end_time = time.time()
                return result, nodes_expanded, end_time - start_time

        return None, nodes_expanded, 0


# ---------------- MAIN ----------------
if __name__ == "__main__":
    problem = MissionariesCannibals()

    print("\n=== BFS ===")
    bfs_solution, bfs_nodes, bfs_time = problem.bfs()
    print("Solution Path:", bfs_solution)
    print("Nodes Expanded:", bfs_nodes)
    print("Time Taken:", bfs_time)

    print("\n=== DFS ===")
    dfs_solution, dfs_nodes, dfs_time = problem.dfs()
    print("Solution Path:", dfs_solution)
    print("Nodes Expanded:", dfs_nodes)
    print("Time Taken:", dfs_time)

    print("\n=== IDDFS ===")
    iddfs_solution, iddfs_nodes, iddfs_time = problem.iddfs(20)
    print("Solution Path:", iddfs_solution)
    print("Nodes Expanded:", iddfs_nodes)
    print("Time Taken:", iddfs_time)
