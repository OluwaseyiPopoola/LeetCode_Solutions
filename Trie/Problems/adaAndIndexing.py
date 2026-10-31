"""
Ada the Ladybug has many things to do and almost no time. She wants to to save time while searching for something so she have decided to make a search engine.

She has many words in her TODO list. It costs her precious time to find out, whether a word is in it so she seeks your help. You will get list and some queries. You will be asked, to find out how many words in TODO list have a word as prefix.

Input
The first line contains N, Q: the number words in TODO list and number of queries.

N lines follow, with words (of TODO list) consisting of lowercase letters. The sum of their lengths won't be greater than 10**6

Q lines follow, with words (queries) consisting of lowercase letters. The sum of their lengths won't be greater than 10**6

Output
For each query print the number of words in TODO list which have actual word as prefix.

Example
InputCopy	
12 6
bulldog
dog
dogged
doggedly
doggerel
dogma
dogmatic
dogmatism
dogs
catastroph
catastroph
doctor
cat
dog
dogg
do
doctrinography
dogge

OutputCopy
2
8
3
9
0
3
"""

def letAnum(xx):
    return ord(xx) - ord("a")  # chr to integer


def dfs(x, s):
    vis[x] = True
    if D[x]:
        print(s)
    gradSal = B[x]  # the degree of x, contains characters
    gradSal.sort()
    for yy in range(len(gradSal)):
        y = gradSal[yy]
        if not vis[F[x][letAnum(y)]]:
            dfs(F[x][letAnum(y)], s + y)


B = [[]]  # vertex -> letter
F = [[-1 for i in range(26)]]  # letter -> vertex

A = ["aba", "hola", "abc", "ho", "z"]  # the set of words
D = [False]  # This says which vertices are terminal (or words)

for i in range(len(A)):  # we iterate over words
    r = 0  # root
    for j in range(len(A[i])):  # we iterate over characters of each word
        iden = letAnum(A[i][j])
        if F[r][iden] == -1:  # I have not seen iden as a child of r
            idenArbol = len(B)  # identification new vertex
            B.append([])
            F.append([-1 for k in range(26)])
            B[r].append(A[i][j])  # vertex r has as a child letter A[i][j]
            F[r][iden] = idenArbol
            D.append(False)
        if j == len(A[i]) - 1:
            D[F[r][iden]] = True
        r = F[r][iden]

print("B:", B)
print("F:", F)
print("D:", D)

print("\nDFS Output:")
vis = [False for i in range(len(B))]
dfs(0, "")