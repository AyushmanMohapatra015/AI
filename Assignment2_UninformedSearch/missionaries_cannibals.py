from collections import deque
import time

class MissionariesCannibals:
    def __init__(self):
        self.start = (3, 3, 1)
        self.goal = (0, 0, 0)

    # ---------------- VALID STATE CHECK ----------------
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

    # ---------------- SUCCESSOR FUNCTION ----------------
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
        start_time = time.perf_counter()

        queue = deque([(self.start, [])])
        visited = set()
        nodes_expanded = 0

        while queue:
            state, path = queue.popleft()
            nodes_expanded += 1

            if state == self.goal:
                end_time = time.perf_counter()
                return path + [state], nodes_expanded, end_time - start_time

            if state not in visited:
                visited.add(state)

                for successor in self.get_successors(state):
                    queue.append((successor, path + [state]))

        return None, nodes_expanded, 0

    # ---------------- DFS ----------------
    def dfs(self):
        start_time = time.perf_counter()

        stack = [(self.start, [])]
        visited = set()
        nodes_expanded = 0

        while stack:
            state, path = stack.pop()
            nodes_expanded += 1

            if state == self.goal:
                end_time = time.perf_counter()
                return path + [state], nodes_expanded, end_time - start_time

            if state not in visited:
                visited.add(state)

                for successor in self.get_successors(state):
                    stack.append((successor, path + [state]))

        return None, nodes_expanded, 0

    # ---------------- DEPTH LIMITED SEARCH ----------------
    def dls(self, state, path, depth_limit, visited, nodes):
        nodes[0] += 1

        if state == self.goal:
            return path + [state]

        if depth_limit <= 0:
            return None

        visited.add(state)

        for successor in self.get_successors(state):
            if successor not in visited:
                result = self.dls(successor, path + [state], depth_limit - 1, visited, nodes)
                if result:
                    return result

        return None

    # ---------------- IDDFS ----------------
    def iddfs(self, max_depth):
        start_time = time.perf_counter()
        total_nodes = 0

        for depth in range(max_depth + 1):
            visited = set()
            nodes = [0]

            result = self.dls(self.start, [], depth, visited, nodes)
            total_nodes += nodes[0]

            if result:
                end_time = time.perf_counter()
                return result, total_nodes, end_time - start_time

        return None, total_nodes, 0


# ---------------- MAIN ----------------
if __name__ == "__main__":
    problem = MissionariesCannibals()

    print("\n===== BFS =====")
    sol, nodes, t = problem.bfs()
    print("Solution Path:", sol)
    print("Nodes Expanded:", nodes)
    print("Time Taken: {:.10f} seconds".format(t))

    print("\n===== DFS =====")
    sol, nodes, t = problem.dfs()
    print("Solution Path:", sol)
    print("Nodes Expanded:", nodes)
    print("Time Taken: {:.10f} seconds".format(t))

    print("\n===== IDDFS =====")
    sol, nodes, t = problem.iddfs(20)
    print("Solution Path:", sol)
    print("Nodes Expanded:", nodes)
    print("Time Taken: {:.10f} seconds".format(t))
