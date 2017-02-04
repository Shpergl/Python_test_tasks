import re


# Set up file to parce
fname = 'task.in'

def readFile(fname):
    """Function for parcing and validating data from scepified file"""
    # Open file rof reading
    with open(fname, 'r') as f:
        content = f.readlines()

    amount = []
    price = []
    header = []
    # Getting data from first line in file to get farmerQuantity and amountNeeded
    try:
        data = map(int, re.findall(r'\d+', content[0]))
    except ValueError as err:
        print(err.args)
    # Validating values of first line
    # 0 <= farmerQuantity <= 100 000 000
    #0 <= amountNeeded <= 300 000 000
    if data[0] <= 100000000 and data[0] >= 0 and data[1] <= 300000000 and data[1] >= 0:
        header.append(data)
    else:
        raise ValueError('Input values not in limited range')

    #Starting to parse next lines
    for line in content[1:]:
        try:
            data = map(int, re.findall(r'\d+', line))
        except ValueError as err:
            print(err.args)
        # Validating values of next lines
        #0<= amount <= 300 000 000
        #1 <= price <= 1 000
        if data[0] <= 300000000 and data[0] >= 0 and data[1] <= 1000 and data[1] >= 1:
            amount  .append(data[0])
            price.append(data[1])
        else:
            raise ValueError('Input values not in limited range')
    return amount, price, header

# Get amount, price, farmerQuantity and amountNeeded
amount, price, header = readFile(fname)
farmerQuantity, amountNeeded = header[0]

totalPrice = 0

if sum(amount) < amountNeeded:
    totalPrice = 0
else:
    while amountNeeded > 0:
        # Get index of min price
        minPriceIndex = price.index(min(price))
        # Take last needed amount
        if amountNeeded < amount[minPriceIndex]:
            totalPrice += (price[minPriceIndex] * amountNeeded)
            break

        # Total price
        totalPrice += (price[minPriceIndex] * amount[minPriceIndex])
        # Remove already used price
        del price[minPriceIndex]
        amountNeeded -= amount[minPriceIndex]

# Create file task.out with received information
msg = "Total price for {} milk bottles is - {}".format(header[0][1], totalPrice)
with open('task.out', 'w') as file:
         file.write(msg)


