#!/usr/bin/python3

"""

Defines function that returns a list of lists of integers

representing the Pascal's triangle of n

"""





def pascal_triangle(n):

    """

    Creates a list of lists of integers representing Pascal's triangle

    parameters:

        n [int]:

            the number of rows of Pascal's triangle to recreate

    return:

        [list of lists of ints]:

            representation of Pascal's triangle

    """

    if type(n) is not int:

        raise TypeError("n must be an integer")

    triangle = []

    if n <= 0:

        return triangle

    previous = [1]

    for row_index in range(n):

        rowlist = []

        if row_index == 0:

            rowlist = [1]

        else:

            for i in range(row_index + 1):

                if i == 0:

                    rowlist.append(0 + previous[i])

                elif i == (row_index):

                    rowlist.append(previous[i - 1] + 0)

                else:

                    rowlist.append(previous[i - 1] + previous[i])

        previous = rowlist

        triangle.append(rowlist)

#!/usr/bin/python3

"""

Pascal's Triangle

"""





def binomialCoeff(n, k):

    """ calculate the value of Binomial Coefficient """

    res = 1

    if (k > n - k):

        k = n - k

    for i in range(0, k):

        res = res * (n - i)

        res = res // (i + 1)

    return res





def pascal_triangle(n):

    """

    Returns  list of lists of integers representing

    the Pascal’s triangle of n or an empty list if n <= 0

    You can assume n will be always an integer

    """

    l1 = []

    for line in range(0, n):

        l2 = []

        for i in range(0, line + 1):

            l2.append(binomialCoeff(line, i))

        l1.append(l2)

    return l1

