"""
File: class_reviews.py
Name: Jane Huang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
助教回饋:
1.忘記做case insensitive
2.也可以max、min 都設為第一筆的值
3.要增加一個判斷式
"""

# This constant controls when to stop，(因為是str 所以constant 也要是str)
EXIT = '-1'


def main():
    """
    This program computes the MAX, MIN, AVG for SC001 and SC101 courses
    """
    sc101_count = 0
    sc001_count = 0
    sc101_total = 0
    sc101_max = 0  # 建議改用 float('-inf')
    sc101_min = float('inf')
    sc001_total = 0
    sc001_max = 0
    sc001_min = float('inf')

    while True:
        # for user to input class and score
        stan_code_class = str(input('Which class? '))
        # While class value is not the EXIT number, keep asking
        if stan_code_class == EXIT:
            break
        score = int(input('Score: '))
        # 計算 101 的 statistics
        if stan_code_class == 'Sc101':
            sc101_count += 1
            sc101_total += score
            if score >= sc101_max:
                sc101_max = score
            if score <= sc101_min:
                sc101_min = score
        # 計算 001 的 statistics
        if stan_code_class == 'Sc001':
            sc001_count += 1
            sc001_total += score
            if score >= sc001_max:
                sc001_max = score
            if score <= sc001_min:
                sc001_min = score

    # EXIT 之後按照不同情況印出結果
    if sc101_count == 0 and sc001_count == 0:
        print('No class scores were entered')
    elif sc001_count == 0:  # 只有101有值
        print('=============SC001=============')
        print('No score for SC001')
        print('=============SC101=============')
        print('Max(101):' + str(sc101_max))
        print('Min(101):' + str(sc101_min))
        print('Avg(101):' + str(sc101_total/sc101_count))
    elif sc101_count == 0:
        print('=============SC001=============')
        print('Max(001):' + str(sc001_max))
        print('Min(001):' + str(sc001_min))
        print('Avg(001):' + str(sc001_total/sc001_count))
        print('=============SC101=============')
        print('No score for SC101')
    else:
        print('=============SC001=============')
        print('Max(001):' + str(sc001_max))
        print('Min(001):' + str(sc001_min))
        print('Avg(001):' + str(sc001_total / sc001_count))
        print('=============SC101=============')
        print('Max(101):' + str(sc101_max))
        print('Min(101):' + str(sc101_min))
        print('Avg(101):' + str(sc101_total/sc101_count))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
