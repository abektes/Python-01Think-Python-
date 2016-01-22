def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
	https://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """

    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

print ackermann(2, 2)

	""" Try to explain 125 steps with http://www.pythontutor.com/visualize.html#mode=displayxs"""