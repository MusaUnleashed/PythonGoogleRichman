# product = input("What is the product name?")
# priceWithoutVat = float(input("What is the price in NIS (without V.A.T)?"))
# vat = priceWithoutVat * 0.18
# total = priceWithoutVat + vat
# print(
#     f"The price of {product} is {priceWithoutVat:.3f}NIS + {vat :.3f} VAT = {total:.4f}  TOTAL."
# )
# / more simple approch
try:
    product = input("What is the product name?")
    price_input = float(input("What is the price in NIS ?"))
    is_vat_included = (
        input("If the price includes VAT enter y (or otherwise anything else): n  ")
        == "y"
    )
    vat_rate = 0.18

    if is_vat_included:
        price_without_vat = price_input / (1 + vat_rate)
        # Calculate VAT amount
        vat_amount = price_input - price_without_vat
        total = price_input
        print(
            f"The price of {product} is {price_without_vat:.2f} NIS + {vat_amount:.2f} VAT = {total:.2f}  TOTAL."
        )
    else:
        price_without_vat = price_input
        vat_amount = price_input * vat_rate
        total = price_without_vat + vat_amount
        print(
            f"The price of {product} is {price_without_vat:.2f} NIS + {vat_amount:.2f} VAT = {total:.2f}  TOTAL."
        )

except Exception as e:
    print(f"An unexpected error occurred: {e}")
