def calculate_total_price(no_of_items, unit_price, tax_rate):
    def calculate_tax(amount):
        return amount * tax_rate
    total_amount_of_all_items = no_of_items * unit_price
    tax_on_all_items = calculate_tax(total_amount_of_all_items)
    gross_amount = total_amount_of_all_items + tax_on_all_items
    return gross_amount

def main():
    no_of_items=int(input("Enter the no. of items: "))
    unit_price=float(input("Enter the unit price: "))
    tax_rate=float(input("Enter the tax rate: "))
    print(calculate_total_price(no_of_items, unit_price, tax_rate))

if __name__ == "__main__":
    main()
