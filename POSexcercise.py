def Sale(barcode):
    global amount
    if barcode == "":
        emptybarcode()
    # introduce lookup table
    elif barcode in products.keys():
        amount = products[barcode]
    else:
        productnotfound(barcode)


products = dict({"12345": "$11.50",
                 "23456": "$12.50",
                 "56789": "$22.50"})

def last_text_displayed():
    return amount


def emptybarcode():
    return "Scanning error: empty barcode"

def productnotfound(barcode):
    return "Product not found for:" + barcode