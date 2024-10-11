def check_triangle_inequality(l1, l2, l3):
    if (l1+l2 >= l3) and (l2+l3 >= l1) and (l1+l3 >= l2):   #Triangle inequality law
        return True
    else:
        return False
def main():
    l1=int(input("Enter the length of side-1 of a triangle: "))
    l2=int(input("Enter the length of side-2 of a triangle: "))
    l3=int(input("Enter the length of side-3 of a triangle: "))
    result=check_triangle_inequality(l1, l2, l3)
    if check_triangle_inequality(l1, l2, l3):
        print(f"The sides {l1}cm, {l2}cm, and {l3}cm can form a triangle.")
    else:
        print(f"The sides {l1}cm, {l2}cm, and {l3}cm can't form a triangle.")
if __name__ == "__main__":
    main()