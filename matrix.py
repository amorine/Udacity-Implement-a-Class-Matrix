import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        # Initialise variable
        result = 0
        # If the matrix is 1x1, return result
        if self.h == 1:
            return self.g[0]
        # If the matrix is 2x2, return result
        if self.h == 2:
            return (self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        # Initialise variable
        result = 0
        # Calculate the sum of the diagonal matrix, return result
        for i in range(self.w):
            result += self.g[i][i]
        return result

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        # NOTE - based on the Udacity inverse matrix topic.
        inverse = []
        # Check if matrix is 1x1, then calculate inverse
        if self.w == 1:
            inverse.append([1 / self.g[0][0]])
        # Check if matrix is 2x2, then calculate inverse
        elif self.w == 2:
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise(ValueError, "The Matrix is not invertible.")
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
                
                factor = 1 / (a * d - b * c)
                
                inverse = [[d, -b],[-c, a]]
                
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
        return Matrix(inverse)
            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        # NOTE - based on the Udacity transpose matrix topic.
        # Initialise matrix to hold results
        matrix_transpose = []
        # Loop through columns on outside loop
        for i in range(self.w):
            new_row = []
            # Loop through columns on inner loop
            for j in range(self.h):
                # Column values will be filled by what were each row before
                new_row.append(self.g[j][i])
            matrix_transpose.append(new_row)
        return Matrix(matrix_transpose)
        
        
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # NOTE - based on the Udacity addition matrix topic.
        # Initialise matrix to hold results
        matrix_add = []
        # Initialise matrix to hold row for appending each element
        row = []
        # For loop within a for loop to iterate over the matrices
        for i in range(self.h):
            row = [] # reset the list
            for j in range(self.w):
                row.append(self[i][j] + other[i][j]) # Add the matrices
            matrix_add.append(row)
        return Matrix(matrix_add)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        # NOTE - based on the __add__ sub, but multiplied by -1
        # Initialise matrix to hold results
        matrix_neg = []
        # Initialise matrix to hold row for appending each element
        row = []
        # For loop within a for loop to iterate over the matrices
        for i in range(self.h):
            row = [] # reset the list
            for j in range(self.w):
                row.append(self.g[i][j] * -1) # Multiply matrix by -1 to produce negative number
            matrix_neg.append(row)
        return Matrix(matrix_neg)
                

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        # Initialise matrix to hold results
        # NOTE - based on the Udacity addition matrix topic and __add__ sub, but subtract.
        matrix_sub = []
        # Initialise matrix to hold row for appending each element
        row = []
        # For loop within a for loop to iterate over the matrices
        for i in range(self.h):
            row = [] # reset the list
            for j in range(self.w):
                row.append(self[i][j] - other[i][j]) # Subtract the matrices
            matrix_sub.append(row)
        return Matrix(matrix_sub)
        
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        # Initialise matrix to hold results
        matrix_mul = []
        # Initialise matrix to hold row for appending each element
        row = []
        # For loop within a for loop to iterate over the matrices
        for i in range(self.h):
            row = [] # reset the list
            for j in range(other.w):
                a = 0
                for k in range(other.h):
                    a += self.g[i][k] * other.g[k][j] # Multiply the matrices
                row.append(a)
            matrix_mul.append(row)
        return Matrix(matrix_mul)
                    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        #   
        # TODO - your code here
        #
        # NOTE - assistance from Udacity Knowledge
        # Initialise matrix to hold results
        matrix_rmul = []
        # Initialise matrix to hold row for appending each element
        row = []
        # For loop within a for loop to iterate over the matrices
        if isinstance(other, numbers.Number):
            for i in range(self.h):
                row = [] # reset the list
                for j in range(self.w):
                    row.append(other * self[i][j])
                matrix_rmul.append(row)
        return Matrix(matrix_rmul)
            