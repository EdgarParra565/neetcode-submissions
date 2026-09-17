class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            total = 0
            numS = str(num)
            for i in numS:
                k = int(i)
                total += (k * k)
            return total
        
        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))


        return fast == 1