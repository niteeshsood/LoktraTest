class Hashit:

    def __init__(self):
        self.letters = 'acdegilmnoprstuw'
        self.h = 7

    def undohash(self, n):
        ans = ''
        while n>0:
            i = n % 37
            try:
                ans+=self.letters[i]
            except Exception,e:
                print 'Hashed value invalid'
            n = int((n-i)/37)

            if n == self.h:
                return ans[::-1]
            if n < self.h:
                print 'Hashed value invalid'


if __name__ == '__main__':
    hh = Hashit()
    print(hh.undohash(930846109532517))
    print(hh.undohash(680131659347))
