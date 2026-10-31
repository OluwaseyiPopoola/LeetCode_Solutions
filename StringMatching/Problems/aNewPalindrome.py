def main():
    t = int(input())

    for _ in range(t):

        palindrome = input()
        n = len(set(list(palindrome[0:len(palindrome)//2])))


        if n > 1:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()