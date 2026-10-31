def calc_num_common_divisor(s1, s2):
    shortest_length = find_smallest_common_divisor(s1, s2)
    count = count_shortest_length_multiples_that_are_factors(shortest_length, len(s1), len(s2))
    return count

def find_smallest_common_divisor(s1, s2):
    prime = 29
    mod = 1e9 + 9
    mod = int(mod)

    prime_pow = [1]
    for i in range(1, max(len(s1), len(s2))):
        prime_pow.append(prime_pow[-1]*prime % mod)

    hashed_s1_prefix = [0]*(len(s1) + 1)
    for i in range(len(s1)):
        hsp_idx = i + 1
        hashed_s1_prefix[hsp_idx] = (hashed_s1_prefix[i] + (ord(s1[i]) - ord('a') + 1)*prime_pow[i]) % mod
    
    hashed_s2_prefix = [0]*(len(s2) + 1)
    for i in range(len(s2)):
        hsp_idx = i + 1
        hashed_s2_prefix[hsp_idx] = (hashed_s2_prefix[i] + (ord(s2[i]) - ord('a') + 1)*prime_pow[i]) % mod


    shortest_length = 0
    hashed_s1 = hashed_s1_prefix[-1]
    hashed_s2 = hashed_s2_prefix[-1]
    # print(f"hashed_s1: {hashed_s1_prefix}")
    # print(f"hashed_s2: {hashed_s2_prefix}")

    for i in range(1, len(hashed_s1_prefix)):
        pos_divisor = hashed_s1_prefix[i]
        prefix_size = i

        if divides(hashed_s1_prefix, pos_divisor, prefix_size, prime_pow) and divides(hashed_s2_prefix, pos_divisor, prefix_size, prime_pow):
            shortest_length = i
            # print(shortest_length)
            break

    return shortest_length



def count_shortest_length_multiples_that_are_factors(shortest_length, s1_length, s2_length):
    if shortest_length == 0:
        return 0

    count = 0
    multiplier = 1
    while (multiplier * shortest_length) - 1 < min(s1_length, s2_length):
        pos_divisor = shortest_length * multiplier

        if s1_length % pos_divisor == s2_length % pos_divisor == 0:
            count += 1

        multiplier += 1
    return count

    

def divides(hashed_str_prefix, pos_divisor, divisor_size, prime_pow, mod=1e9 + 9):
    if (len(hashed_str_prefix) - 1) % divisor_size != 0:
        return False

    j = 0
    while j + divisor_size  - 1 < len(hashed_str_prefix) - 1:
        substr_hashed = (hashed_str_prefix[j + divisor_size] + mod - hashed_str_prefix[j]) % mod
        if substr_hashed != pos_divisor*prime_pow[j] % mod:
            return False
        j += divisor_size

    return True
    
s1 = input()
s2 = input()

count = calc_num_common_divisor(s1, s2)
print(count)