# product = input("What is the product name?")
# priceWithoutVat = float(input("What is the price in NIS (without V.A.T)?"))
# vat = priceWithoutVat * 0.18
# total = priceWithoutVat + vat
# print(
#     f"The price of {product} is {priceWithoutVat:.3f}NIS + {vat :.3f} VAT = {total:.4f}  TOTAL."
# )
# / more simple approch
product = input("What is the product name?")
priceWithoutVat = round(float(input("What is the price in NIS (without V.A.T)?")), 2)
vat = round(priceWithoutVat * 0.18, 2)
total = priceWithoutVat + vat
print(f"The price of {product} is {priceWithoutVat}NIS + {vat} VAT = {total}  TOTAL.")
