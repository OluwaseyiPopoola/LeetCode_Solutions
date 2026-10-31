def main():
    str_1 = input()
    str_2 = input()

    levStr1: set = getLevStr(str_1)
    levStr2: set = getLevStr(str_2)

    lst = list(levStr1.intersection(levStr2))
    print(lst)

    for word in sorted(lst):
        print(word)

def getLevStr(str):

    setStr = set()
    for i in range(len(str)):

        for k in range(26):
            char = chr(ord("a") + k)
            copy = str[:i] + char + str[i:]
            setStr.add(copy)

    for i in range(26):
        char = chr(ord("a") + i)
        copy = str + char
        setStr.add(copy)

    for i in range(len(str)):
        setStr.add(str[:i] + str[i + 1:])

    for i in range(len(str)):
            
            for k in range(26):
                char = chr(ord("a") + k)
                copy = str[:i] + char + str[i + 1:]
                setStr.add(copy)
    print(setStr)
    return setStr
    













if __name__ == "__main__":
    main()