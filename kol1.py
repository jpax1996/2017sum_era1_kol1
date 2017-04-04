from pprint import pformat as pf

class Matrix(object):
    def __init__(self, arrayOfRows=None, rows=None, cols=None):
        if arrayOfRows:
            self.data = arrayOfRows
        else:
            self.data = [[0 for c in range(cols)] for r in range(rows)]
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    @property
    def shape(self):          
        return (self.rows, self.cols)
    def __getitem__(self, i): 
        return self.data[i]
    def __str__(self):       
        return pf(self.data)

    @classmethod
    def map(cls, func, *matrices):
        assert len(set(m.shape for m in matrices))==1, 'Not all matrices same shape'

        rows,cols = matrices[0].shape
        new = Matrix(rows=rows, cols=cols)
        for r in range(rows):
            for c in range(cols):
                new[r][c] = func(*[m[r][c] for m in matrices], r=r, c=c)
        return new
    def __add__(self, other):
        return Matrix.map(lambda a,b,**kw:a+b, self, other)
    def __sub__(self, other):
        return Matrix.map(lambda a,b,**kw:a-b, self, other)


