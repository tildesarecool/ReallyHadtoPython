'''
i was trying to start this excercise but kept getting python interpreter errors
i thought there was something wrong with the code below the "don't edit below this" line
but upon looking at the solution i now realize the whole point was the use the try/excepts
to catch those errors and deal accordingly


description:
PURCHASING
Now we need to use our purchase function to process an entire list of purchase orders.

CHALLENGE
Complete the make_purchases function. It takes a list of purchase orders. Each order is a dictionary. Look through the main() function to see the shape of this data.

First, create an empty list of leftovers.

Then, loop over the list of purchase orders.

For each order, try to process the order with the purchase function. If an exception is raised, print this string, Purchase exception: ERROR, where ERROR is the exception's text.

If there is not an error, then the purchase was successful. Append the remaining amount to the leftovers list. If there is an error, don't add anything to the leftovers.

Be sure to loop over the entire list of purchase orders. At the end of the loop, return the leftovers list.

Keep the same order of purchases, but with the unsuccessful purchases removed.


'''


def make_purchases(purchase_orders):
    leftovers = []
    for purchase_order in purchase_orders:
        try:
            price = purchase_order["price"]
            money_available = purchase_order["money_available"]
            leftover = purchase(price, money_available)
            leftovers.append(leftover)
        except Exception as e:
            print(f"Purchase exception: {e}")
    return leftovers


# Don't edit below this line


def main():
    print("Making purchases...")
    leftovers = make_purchases(
        [
            {"price": 10.00, "money_available": 125.00},
            {"price": 5.00, "money_available": 2.00},
            {"price": 20.01, "money_available": 5.20},
            {"price": 1.04, "money_available": 254.00},
            {"price": 40.20, "money_available": 6.00},
            {"price": 16.00, "money_available": 235.01},
            {"price": 10.70, "money_available": 254.10},
            {"price": 12.00, "money_available": 2.30},
        ]
    )
    print("Purchases complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase(price, money_available):
    if money_available < price:
        raise Exception(f"{money_available:.2f} is not enough for {price:.2f}")
    return money_available - price


main()
