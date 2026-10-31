"""
0 -> 00000
1 -> 00001
2 -> 00002

i -> 00010
i -> 00100
  


"""




def generateAllPlates(n):
    #sum = 10**5 + 26**0 + 10**4 + 26**1 + 10**4 + 26**2 + 1
    sum = 0

    for i in range(6):
        sum += 10**(5 - i) + 26**i


    n %= sum

    plate_num = [str(i) for i in range(10)]
    plate_char = plate_num + [ chr(i + ord("A")) for i in range(26)]


    plate =   [0, 0, 0, 0, 0]

    i = 0

    for j in range(6):

        a_start = 0 if j < 1 else 10
        a_stop = 10  if j < 1 else len(plate_char)
        for a in range(a_start, a_stop):
            plate[0] = str(plate_char[a])

            b_start = 0 if j < 2 else 10
            b_stop = 10  if j < 2 else len(plate_char)
            for b in range(b_start, b_stop):

                plate[1] = str(plate_char[b])

                c_start = 0 if j < 3 else 10
                c_stop = 10  if j < 3 else len(plate_char)
                for c in range(c_start, c_stop):

                    plate[2] = str(plate_char[c])

                    d_start = 0 if j < 4 else 10
                    d_stop = 10  if j < 4 else len(plate_char)
                    for d in range(d_start, d_stop):

                        plate[3] = str(plate_char[d])

                        e_start = 0 if j < 5 else 10
                        e_stop = 10  if j < 5 else len(plate_char)
                        for e in range(e_start, e_stop):

                            plate[4] = str(plate_char[e])

                            
                            if i == n:
                                print(plate)
                                return "".join(plate)

                            i += 1



if __name__ == "__main__":
    n = int(input())
    # n = (10**5 + 26**0 + 10**4 + 26**1 + 10**3 + 26**2 + 10**2 + 26**3 + 10**1 + 26**4 + 10**0 + 26**5) - 1
    print(generateAllPlates(n))
  
