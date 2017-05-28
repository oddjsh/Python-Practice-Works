x= 6

def example():

    globx = x
    print(globx)
    globx+= 5
    print(globx)

    return globx

example()
x = example()
print(x)



def example_2():

    globx = x
    print(globx)
    globx += 9
    print(globx)

example_2()
x = example_2()
print(x)
