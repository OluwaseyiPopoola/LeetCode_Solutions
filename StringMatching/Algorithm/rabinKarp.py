def main():
    pattern = input("Pattern: ")
    text = input("Text: ")
    index = find_pattern(pattern, text)
    print(f"pattern ({pattern}) located at indices ({index})")

def test():
    text_str = "aceg"
    print(rabin_karp(text = text_str, pattern= "eg"))
    pass


def find_pattern(pattern, text):
    return rabin_karp(pattern, text)


def rabin_karp(pattern, text):
    prime = 29
    mod = 1e9 + 9

    prime_pow = [1]
    for _ in range(max(len(pattern), len(text)) - 1):
        prime_pow.append(prime_pow[-1]*prime % mod)


    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash  + (ord(pattern[i]) - ord('a') + 1)*prime_pow[i]) % mod

    # print(f"pattern_hash: {pattern_hash}")

    prefix_text_hash = [0]*(len(text) + 1)
    for i in range(len(text)):
        ptv_idx = i + 1
        prefix_text_hash[ptv_idx] = (prefix_text_hash[i] + (ord(text[i]) - ord('a') + 1)*prime_pow[i]) % mod 

    

    occurences = []
    i = 0
    while i + len(pattern) - 1 < len(text):
        # print("\n")
        # print(i)
        # print(i + len(pattern))

        text_substr_hash = ((prefix_text_hash[i + len(pattern)] + mod) - prefix_text_hash[i]) % mod
        print(text_substr_hash)
        if text_substr_hash == (pattern_hash*prime_pow[i]) % mod:
            # print(i)
            occurences.append(i)
        i += 1

    return occurences





"""
text = abced

pth   = [
            0,
            a,
            a + bx,
            a + bx + cx2
            a + bx + cx2 + ex3,
            a + bx + cx2 + ex3 + dx4,
        ]


pattern = c + ex + dx2
initial = a + bx + cx2


i = 0








"""


    



    

    

    




if __name__ == "__main__":
    main()