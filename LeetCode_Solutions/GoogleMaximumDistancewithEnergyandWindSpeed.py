"""Q1) 
you are given maximum initial energy k (k<1000) and array A of length n denoting wind speed on n days. 
he is stuck on a boat and each day he can either choose to move or stay put.. 
each day he decides to travel he will move ahead A[i] Dist 
and his energy decreases by 1 and if he decides to stay put his energy increases by 1.
What is the maximum distance he can travel without dropping his energy to negative after n days.

My clarIfications:
Can the array be empty ?
the K input is an integer ?
Should I assume k  <= n ?
Can k be negative ?
What's the maximum size of A ? 
"to travel" means "to move" ? 

Missed Clarification:
Can wind speed be negative?

k = 2
[10, 1, 4]
 i

 10, 2 i = 0
 |---1, 1 i = 1
     |---4, 0 i = 2  
     |
 




"""


def main():
    k = int(input())
    A = list(map(int, input().split()))


def findMaxDistance(i, k, A):
    
    if i == len(A):
        return 0

    travel = 0
    stayPut = findMaxDistance(i + 1, k + 1, A)

    if k > 0:
        travel = A[i] + findMaxDistance(i + 1, k - 1, A)

    return max(travel, stayPut)
    

"""
A = []
k = 4
fmd()

"""    
        



if __name__ == "__main__":
    main()