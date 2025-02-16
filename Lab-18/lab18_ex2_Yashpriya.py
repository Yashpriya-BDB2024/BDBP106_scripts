#To reduce the fraction to lowest terms.
from lab18_ex1_Yashpriya import greatest_common_divisor
def reduce_fraction(n, d):
    if n > 0 and d > 0:
        gcd_val=greatest_common_divisor(n, d)
        reduced_n = n // gcd_val
        reduced_d = d // gcd_val
        return reduced_n, reduced_d
def main():
    numerator=int(input("Enter the positive integer as numerator: "))
    denominator=int(input("Enter the positive integer as denominator: "))
    result_n,result_d = reduce_fraction(numerator, denominator)
    print("The reduced fraction is: ", result_n,"/",result_d)
if __name__ == "__main__":
    main()

