import random
def dice_sum():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    return dice1+dice2
def rolls():
    n=1000
    sum_list=[]
    for i in range(n):
        result=dice_sum()
        sum_list.append(result)
    sum_possibilities=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    freq=[sum_list.count(i) for i in range(2, 13)]
    observed_percent=[(i*100)/n for i in freq]
    expected_percent = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    print("Sum\t\tObserved %\t\tExpected %")
    for i, j, k in zip(sum_possibilities, observed_percent, expected_percent):
        print(f"{i}\t\t\t{j:.2f}\t\t\t{k}")    # \t - for spaces between columns; and .2f - upto 2 decimal places
def main():
    rolls()
if __name__ == '__main__':
   main()
