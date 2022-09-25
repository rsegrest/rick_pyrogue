from random import Random

class RandomX(Random):
    def __init__(self,l):
        super().__init__(l)
        self.P=0x7fffffff # Mask for random number generator (?)
    
    def percent(self, n):
        return (self.randint(0,self.P) & self.P) % 100 < n

    def coin(self):
        return 0 != (self.randint(0,self.P) & 1)

    def get(self, n0, n1):
        # return n0 >= n1 ? n0 : n0 + (self.nextInt() & P) % (1+n1-n0)
        pass

    def get(self, n):
        # return (self.thisInt() & P) % (1+n)
        pass

    # Object permute(Object o[])[]{
    #   int j = o.length
    #   while(--j > 0) {
    #       int i = get(j) // was j-1?
    #       Object t = o[j]
    #       o[j] = o[i]
    #       o[i] = t
    #   return o

    # int permute(int b[])[] { }

    # int permute(n)[] {
    # }


