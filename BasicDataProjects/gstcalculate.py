def gst_calculator():
    try:
        price = float(input("Enter item price: "))
        gst = float(input("Enter GST %: "))

        gst_amount = (price * gst) / 100
        final_price = price + gst_amount

        print("GST Amount:", gst_amount)
        print("Final Price:", final_price)

    except ValueError:
        print("Please enter valid numbers!")

gst_calculator()