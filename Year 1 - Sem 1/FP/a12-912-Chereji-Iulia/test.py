class SparseMatrix:
    def __init__(self, l, c):
        self._matrix = [[None for j in range(c)] for i in range(l)]
        self._l = l
        self._c = c

    def set_rows(self, val):
        self._l = val

    def set_cols(self, val):
        self._c = val

    def set(self, l, c, val):
        if int(l) > int(self.get_l)-1 or int(c) > int(self.get_c)-1:
            raise ValueError
        self._matrix[l][c]=val

    def get_val(self,i,j):
        return self._matrix[i][j]

    @property
    def get_l(self):
        return self._l

    @property
    def get_c(self):
        return self._c

    def __str__(self):
        str1=''
        for i in range(self.get_l):
            for j in range(self.get_c):
                if self._matrix[i][j]==None:
                    str1=str1+' 0 '
                else:
                    str1=str1+ ' '+str(self._matrix[i][j])+ ' '
            str1=str1+'\n'
        return str1

m1 = SparseMatrix(3,3)
# Value at [1,1] is 2
m1.set(1,1,2)
# Value at [2,2] is 4
m1.set(2,2,4)
print(m1)
try:
    m1.set(3,3,99)
except Exception as e:
    print(type(e))

m1.set(1,1,m1.get_val(1,1)+1)
print(m1)
