import numpy as np

class polinomial:
    '''
    A class of polynomial and related operations on polynomials
    '''

    def __init__(self, coef_list):
        self.coef = np.array(coef_list)
        self.degree = len(coef_list) - 1


    def __add__(self, other):
        '''
        Define '+' to be adding two polynomials together
        '''
        if self.degree > other.degree:
            sum_coef = self.degree
            for i in range(1, other.degree+2):
                sum_coef[-i] += other.coef[-i]
        else:
            sum_coef = other.degree
            for i in range(1, self.degree + 2):
                sum_coef[-i] += self.coef[-i]

        return polinomial(sum_coef)

    def deriv(self):
        '''
        Get the first derivative of the input polynomial
        '''
        # In the first derivative of the last term of the polynomial is zero.
        der_coef = [self.coef[i]*(self.degree-i) for i in range(self.degree )]
        return polinomial(der_coef)

    def disp(self):
        '''
        Display the input polynomial in a readable way.
        '''
        ploy_string = []
        # From beginning to the second last terms
        # The zero terms are skipped
        for i in range(self.degree):
            if self.coef[i] == 1:
                ploy_string += '+' + 'x^' + str(self.degree - i)
            elif self.coef[i] > 0:
                ploy_string += '+' + str(self.coef[i]) + 'x^' + str(self.degree - i)
            elif self.coef[i] == -1:
                ploy_string += '-' + 'x^' + str(self.degree - i)
            elif self.coef[i] < 0:
                ploy_string += str(self.coef[i]) + 'x^' + str(self.degree - i)
        # Get the last term
        if self.degree >= 0:
            if self.coef[-1] > 0:
                ploy_string += '+' + str(self.coef[-1])
            elif self.coef[-1] < 0:
                ploy_string += str(self.coef[-1])
        return ''.join(ploy_string)

poly1 = polinomial([1, 0, 0, -2, 5])
print(poly1.disp())

der_poly1 = poly1.deriv()
print(der_poly1.disp())

poly2 = polinomial([1, 2, 1])
print(poly2.disp())

poly3 = poly1 + poly2
print(poly3.disp())