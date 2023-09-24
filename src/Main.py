# separator	Main.py_0_false.txt

file_name = input()
x = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# separator	Main.py_1_true.txt

def func(M):
    c = ((-1)**M) / (2*M + 1)
    for i in range(x+1):
        M = int(open(file=file_name).read(i))
        for n in range(0, M+1):
            c = ((-1)**n) / (2*n + 1)
            print(c)
        print()
    return c



# separator	Main.py_2_false.txt
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

