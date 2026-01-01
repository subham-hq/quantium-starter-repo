import csv
input_files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

with open('output_sales.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['Sales', 'Date', 'Region'])

    for file_path in input_files:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row['product'] == 'pink morsel':
                    sales = (int(row['quantity']) * float(row['price'].lstrip('$')))
                    date = row['date']
                    region = row['region']
                    print(sales, date, region)
                    writer.writerow([sales, date, region])


"""
    for row in reader:

        product = row[0]
        price = row[1]
        quantity = row[2]
        date = row[3]
        region = row[4]

        if product == "pink morsel":
            price_flt = price.lstrip("$")
            quantity_int = int(quantity)
            sales = float(price_flt) * quantity_int

            print(sales, date, region)
"""