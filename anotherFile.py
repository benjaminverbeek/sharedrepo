for i in range(1):
	print("Hello World")

# NOTE: some txt
def revolutionaryFunction(x):
	return lambda a: a**x

print(f"Revolutionary function in action: {revolutionaryFunction(3)(5)}")