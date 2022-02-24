def on_barcode(barcode):
    global amount
    if barcode == "":
        amount = "Scanning error: empty barcode"
    # introduce lookup table
    elif barcode in products.keys():
        amount = products[barcode]
    else:
        amount = "Product not found for:" + barcode


products = dict({"12345": "$11.50",
                 "23456": "$12.50",
                 "56789": "$22.50"})


def last_text_displayed():
    return amount





