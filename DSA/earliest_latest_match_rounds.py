from typing import List
from functools import lru_cache


    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1  
        secondPlayer -= 1

        @lru_cache(None)
        def dfs(players: tuple, round_num: int) -> List[int]:
            l, r = 0, len(players) - 1

            
            while l < r:
                if {players[l], players[r]} == {firstPlayer, secondPlayer}:
                    return [round_num, round_num]
                l += 1
                r -= 1

            res = [float('inf'), -float('inf')]

            
            def next_round(index: int, current: List[int]):
                if index >= len(players) // 2:
                    if len(players) % 2:
                        current.append(players[len(players)//2])
                    res_round = dfs(tuple(sorted(current)), round_num + 1)
                    res[0] = min(res[0], res_round[0])
                    res[1] = max(res[1], res_round[1])
                    return

                l = index
                r = len(players) - 1 - index
                a, b = players[l], players[r]

                
                if firstPlayer in (a, b) or secondPlayer in (a, b):
                    winner = firstPlayer if firstPlayer in (a, b) else secondPlayer
                    next_round(index + 1, current + [winner])
                else:
                    next_round(index + 1, current + [a])
                    next_round(index + 1, current + [b])

            next_round(0, [])
            return res

        return dfs(tuple(range(n)), 1)
