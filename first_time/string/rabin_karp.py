class Rabin_Karp:
    def __init__(self):
        self.D = 256
        self.Q = 9997
    def __call__(self, txt, pat):
        M, N = len(txt), len(pat)
        txthash, pathash = int(0), int(0)
        # cal initial txt hash and pat hash(len = M)
        for i in range(N):
            pathash = (self.D * pathash + ord(pat[i])) % self.Q
            txthash = (self.D * txthash + ord(txt[i])) % self.Q
        
        highestpow = 1
        for i in range(N-1):
            highestpow = (highestpow * self.D) % self.Q
        
        for i in range(M-N+1):
            if pathash == txthash:
                # if pass the Fuzzy comparison，then compare between single char
                for j in range(N):
                    if txt[i+j] != pat[j]:
                        break
                if j == N-1:
                    return i
            
            if i < M-N:
                # update txthash
                txthash = (self.D * (txthash - ord(txt[i]) * highestpow) + ord(txt[i+N])) % self.Q
                if txthash < 0:
                    txthash += self.Q
        
        
if __name__ == '__main__':
    txt = 'iamyourheart'
    pat = 'heart'
    rb = Rabin_Karp()
    print(rb(txt, pat))