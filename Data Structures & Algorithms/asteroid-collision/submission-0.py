class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for asteroid in asteroids:
            cur = True

            while ans and (ans[-1] > 0 and asteroid < 0):
                if (ans[-1] < -asteroid):
                    ans.pop()
                elif ans[-1] == -asteroid:
                    ans.pop()
                    cur = False
                    break
                else:
                    cur = False
                    break

            if cur:
                ans.append(asteroid)
            else:
                continue

        return ans
