def Sale(barcode):
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


class sale:
    def __init__(self, barcode):
        self.barcode = barcode

    def displayprice(self):
        return products.values()

    def emptybarcode(self):
        return "Scanning error: empty barcode"

    def productnotfound(self):
        return "Product not found for:" + self.barcode

    def selloneitem(self):
        if self.barcode == "":
            sale.emptybarcode(self.barcode)
            # introduce lookup table
        elif self.barcode in products.keys():
            sale.displayprice(self.barcode)
        else:
            sale.productnotfound(self.barcode)

products = dict({"12345": "$11.50",
                 "23456": "$12.50",
                 "56789": "$22.50"})

#display empty barcode
#display product not found
#display price


