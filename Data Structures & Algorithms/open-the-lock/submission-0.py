class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"

        if start in dead:
            return -1

        queue = deque([(start, 0)])  # (state, moves)
        visited = {start}

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps

            for i in range(4):  # each wheel
                for delta in [-1, 1]:
                    # turn wheel
                    new_digit = (int(state[i]) + delta) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]

                    if new_state not in dead and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))

        return -1