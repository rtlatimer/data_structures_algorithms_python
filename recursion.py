def get_fib(position):
	if position == 0 or position == 1:
		return position
	return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print get_fib(1)
print get_fib(2)
print get_fib(3)
print get_fib(4)
print get_fib(5)
print get_fib(6)
print get_fib(9)
print get_fib(11)
print get_fib(0)
print get_fib(20)
print get_fib(30)