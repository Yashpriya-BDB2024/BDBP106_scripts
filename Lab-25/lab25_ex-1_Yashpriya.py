def checkList(L, i):
    try:
        print(L[i])
    except IndexError:
        print("Index error: Index is out of range.")
    except TypeError:
        print("Type error")
    except Exception as err:
        print(f"Something else broke: {err}")
def main():
    checkList([1,2,3,4,5], 2)
    checkList(['a', '1', '#'], 4)
    checkList("hello", 3)
    checkList("hello", -1)
    checkList(True, 1)
    checkList([1,2,3], 'a')
if __name__ == "__main__":
    main()

