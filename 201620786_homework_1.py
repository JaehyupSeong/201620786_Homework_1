#!/usr/bin/env python3
import sys

def hw1_1():
    """
    Print out "Hello World!"
    Delete 'pass' keyword and write your code!
    """
    hello_world = ' \" Hello World \" '
    return hello_world


def hw1_2(tree_n):
    """
    Print the fowlloing chrismas tree
       *
      ***
     *****
    *******
    tree_n indicates the number of levels of the tree
    Each level contains 2n - 1 stars.
    Delete 'pass' keyword and write your code!
    """

    for idx in range(tree_n):
        star = '*' * (2 * (idx + 1) - 1)
        tree = print(star)
    return tree



def hw1_3(fac_n):
    """
    Compute n!
    Return the result with res variable
    Delete 'pass' keyword and write your code!
    """
    fac_n = 5
    res = 1
    for i in range(fac_n):
        res = (i+1) * res
    return res


def hw1_4(fib_n):
    """
    Compute the nth Fibonacci number
    Return the result
    Delete 'pass' keyword and write your code!
    """
    fib_n = 5
    res = [1, 1]
    for i in range(fib_n):
        idx = i + 2
        res.append(res[idx-2] + res[idx-1])

    return res[fib_n + 1]


"""
본 if문은 C의 main 함수와 유사한 역할을 합니다.
프로그램을 파이썬 인터프리터로 실행할 경우에 실행되는 블락입니다.
"""
if __name__ == "__main__":

    """
    sys.argv는 프로그램의 인자를 가진 리스트입니다.
    3가지 경우를 대비해 작성해 두었습니다.
    1) python hw1.py test.txt일 경우 텍스트 문서에 작성된 3개의 데이터를 할당합니다.
    2) python hw1.py tree_n fac_n fib_n일 경우 터미널에서 받은 인자를 할당합니다.
    3) python hw1.py일 경우 디폴트로 세팅된 3 10 10이 할당됩니다.
    """
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            data_list = f.readline().replace("\n", "").split(" ")
            tree_n = int(data_list[0])
            fac_n = int(data_list[1])
            fib_n = int(data_list[2])
    elif len(sys.argv) < 4:
        tree_n = 3
        fac_n = 10
        fib_n = 10
    else:
        tree_n = int(sys.argv[1])
        fac_n = int(sys.argv[2])
        fib_n = int(sys.argv[3])

    """
    출력을 터미널에서 확인하는 것이 아닌 텍스트 파일로 저장합니다. 
    결과를 확인하려면 텍스트파일을 확인해보세요.
    밑 코드에 학번이라 적힌 것을 지우고 자신의 학번을 기재해 주세요.
    """
    sys.stdout = open("output_201620786.txt", "w")

    print("Q1:", hw1_1())
    # HW 1-1 Func

    print("Q2:")
    # HW 1-2 Func
    hw1_2(tree_n)
    # HW 1-3 Func
    print("Q3:", hw1_3(fac_n))

    # HW 1-4 Func
    print("Q4:", hw1_4(fib_n))