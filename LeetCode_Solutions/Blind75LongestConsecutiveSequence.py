class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_idx = set()
        
        for num in nums:
            nums_idx.add(num)

        done = set()

        longest = 1
        for num in nums:
            if num in done:
                continue

            curr_longest = 1
            low = num - 1
            high = num + 1

            done.add(num)

            while low in nums_idx:
                curr_longest += 1
                done.add(low)
                low -= 1
                
            while high in nums_idx:
                curr_longest += 1
                done.add(high)
                high += 1

            longest = max(longest, curr_longest)

        return longest





            

            
            


        




        # prev = {num : None for num in nums}
        # done = {}
        # longest = 0

        # def explore(start, num, cl):
        #     # ident = (" "*cl) 
        #     # print(ident + f"explore({start, num, cl})")
        #     # print(ident + f"done: {done}")
        #     # print(ident + f"prev: {prev}")
        #     # print()

        #     nonlocal longest

        #     if num in done:
        #         cl += done[num]
        #         longest = max(cl, longest)
        #         done[start] = cl
        #         return

        #     if prev[num] != None:
        #         return
            
        #     cl += 1
        #     longest = max(cl, longest)

        #     next_num = num + 1

        #     if next_num not in prev:
        #         done[start] = cl
        #         return 
        #     # prev[next_num] = start

        #     prev[num] = start

        #     explore(start, next_num, cl)

        # for num in nums:
        #     if prev[num] != None:
        #         continue
        #     explore(num, num, 0)

        #     # print(f"longest: {longest}")
        #     # print("\n\n")

        # return  longest



        
