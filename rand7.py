"""
This problem was asked by Two Sigma.
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
import random
def rand5():
    return random.choice(list(range(1,6)))

def rand7():
    """
    1 2 3 4 5
    1 2 3 4 5 6 7
    """
    return (rand5()+rand5()+rand5()) // 2

if __name__ == '__main__':
    for _ in range(50):
        print(rand7())