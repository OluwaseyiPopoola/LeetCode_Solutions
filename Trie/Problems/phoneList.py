def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        ps = []
        for _ in range(n):
            ps.append(input())

            
        vc = [[-1]*10]
        vc_t = [False]
        res = "YES"

        for i in range(len(ps)):
            
            r = 0
            for j in range(len(ps[i])):
                id = lNum(ps[i][j])

                if vc[r][id] != -1:
                    if j == len(ps[i]) - 1 or vc_t[vc[r][id]] == True:

                        
                        res = "NO"
                        break

                if vc[r][id] == -1:
                    vc[r][id] = len(vc)
                    vc.append([-1]*10)
                    vc_t.append(False)

                r = vc[r][id]

                if j == len(ps[i]) - 1:
                    vc_t[r] = True

            if res == "NO":
                break

        print(res)
            

def lNum(xx):
    return ord(xx) - ord('0')



if __name__ == "__main__":
    main()