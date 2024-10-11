def wavelength_colour(w):
    if w>=380 and w<450:
        return "Violet"
    elif w>= 450 and w < 495:
        return "Blue"
    elif w >= 495 and w < 570:
        return "Green"
    elif w>= 570 and w < 590:
        return "Yellow"
    elif w >= 590 and w< 620:
        return "Orange"
    elif w>= 620 and w <= 750:
        return "Red"
    else:
        print("Please enter the wavelength in between 380 to 750.")
def main():
    wavelength=int(input("Enter the wavelength between 380 nm to 750 nm (without unit): "))
    result=wavelength_colour(wavelength)
    print(f"The colour at wavelength {wavelength}nm is {result}.")
if __name__ == "__main__":
    main()


