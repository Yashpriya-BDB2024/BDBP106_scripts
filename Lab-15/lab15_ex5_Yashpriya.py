bread_price=25.50
discount=0.6
#Get the no. of loaves of day old bread being purchased
day_old_loaves_num=int(input("Enter the number of day old loaves: "))
#Calculate the regular price & print
regular_price=day_old_loaves_num*bread_price
print("Regular price: %5.2f" % regular_price)
#Calculate the discount given & print
discount_amount=regular_price*discount
print("Discount: %5.2f" % discount_amount)
#Calculate the total price & print
total_price=regular_price-discount_amount
print("Total price: %5.2f" % total_price)


