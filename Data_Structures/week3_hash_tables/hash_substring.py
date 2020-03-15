# python3
import numpy as np

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(S,p,x):
    hash_value = 0
    for i in range(len(S)-1, -1, -1):
        hash_value = (hash_value*x + ord(S[i])) %p
    return hash_value

def PrecomputeHashes(text, pattern_size, p, x):
    pre_computed_hash_values = np.empty((len(text) - pattern_size + 1), dtype=int)
    S = text[-pattern_size:]
    pre_computed_hash_values[-1] = PolyHash(S,p,x)
    y = 1
    for i in range(1, pattern_size+1):
        y = (y*x)%p
    for i in range(len(pre_computed_hash_values)-2,-1,-1):
        pre_computed_hash_values[i] = (x*pre_computed_hash_values[i+1] + ord(text[i]) - y*ord(text[i+pattern_size]))%p
    return pre_computed_hash_values

def get_occurrences(pattern, text):
    prime_no = 982451653 
    x = np.random.randint(1,prime_no,1)
    result = []
    pHash = PolyHash(pattern, prime_no, x)
    preComputedHashes = PrecomputeHashes(text, len(pattern), prime_no, x)
    for i in range(len(text) - len(pattern)+1):
        if pHash != preComputedHashes[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

