# Aim: Implementation of Rabin-Karp Algorithm for Pattern Searching

def rabin_karp_matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0  # hash value for pattern
    t = 0  # hash value for text window
    result = []

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Sliding the pattern over text
    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                result.append(s)
        if s < n - m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + m])) % q
            t = (t + q) % q  # make sure t is positive

    return result

# Example usage
text = "Hello World"
pattern = "World"
d = 256  # number of characters in the input alphabet
q = 101  # a prime number

print("Pattern found at index(es):", rabin_karp_matcher(text, pattern, d, q))
