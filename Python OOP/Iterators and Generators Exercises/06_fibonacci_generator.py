def fibonacci():

    first = 0
    second = 1

    while True:
        yield first

        first, second = second, first + second


generator = fibonacci()
for i in range(10):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
