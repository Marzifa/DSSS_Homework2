import random
import unittest

if __name__ == "__main__":
    unittest.main()
    print("hi ")

# Random Number will be chosen by random library
def function_random_number(min, max):
    """
    Random integer.
    """
    print("random", random.randint(min, max))
    return random.randint(min, max)


# Random operator will be chosen ('+','-','*')
def function_random_operators():
    return random.choice(['+', '-', '*'])


# Final function will be made here
def function_final(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a


# number of loop here is (t_q = 4)
def math_quiz():
    s = 0
    t_q = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
#range of random numbers for n1 is (1,10) and for n2 is (1,5)
    for _ in range(t_q):
        n1 = function_random_number(1, 10);
        n2 = function_random_number(1, 5);
        o = function_random_operators()

        PROBLEM, ANSWER = function_final(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

