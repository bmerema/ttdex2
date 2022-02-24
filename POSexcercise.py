def on_barcode(barcode):
    global amount
    if barcode =="":
        amount = "Scanning error: empty barcode"
    # introduce lookup table
    elif barcode in products.keys():
        amount = products[barcode]


    #elif barcode == '12345\n':
    #    amount = "$11.50"
    #elif barcode == '56789\n':
    #    amount = "$22.50"
    #    try:
    #        int(barcode)
    #        amount = "$12.50"
    #    except:
    #        amount = "invalid"

products = dict({"12345":"$11.50",
                 "56789":"$22.50"})

def last_text_displayed():
    return amount

#def sale():




