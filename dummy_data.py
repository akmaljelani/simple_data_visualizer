import pandas as pd
import random
import string
#
# # Set the number of samples
# #n = 1000
#
# # Create a list of random customer IDs
# customer_ids = [''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for i in range(1000)]
#
# # Create a list of random genders
# genders = [random.choice(['male', 'female']) for i in range(1000)]
#
# # Create a list of random ages between 18 and 60
# ages = [random.randint(18, 61) for i in range(1000)]
#
# # Create a list of 15 random household items
# items = [random.choice(['Spark Plugs', 'Ignition Coils', 'Suspension', 'Wiper blade', 'Tyre', 'Air Freshener',
#                         'Brake Disc', 'All-Purpose Cleaner', 'Brake Pads']) for i in range(1000)]
#
# # Create a list of random price per unit for each product
# prices_per_unit = [random.uniform(50, 200) for i in range(1000)]
#
# # Create a list of random units purchased for each product
# units_purchased = [random.randint(1, 10) for i in range(1000)]
#
# # Calculate the total purchase for each product
# total_purchases = [price * units for price, units in zip(prices_per_unit, units_purchased)]
#
# # # Create a list of random dates between 1/1/2022 and 30/1/2022
# dates = [pd.date_range(start='1/1/2022', end='30/1/2022', freq='D').tolist() for i in range(1000)]
#
# # dates
# # Create a list of payment methods
# payment_methods = [random.choice(['cash', 'card', 'e-wallet']) for i in range(1000)]
#
# # Create a list of supermarket branches
# workshop_branches = [random.choice(['Kuala Lumpur', 'Ipoh', 'Pulau Pinang', 'Johor Bahru', 'Seremban']) for i in range(1000)]
#
# # Create a dictionary with the data
# data = {'customer_id': customer_ids, 'gender': genders, 'age': ages, 'product': items,
#         'price_per_unit': prices_per_unit, 'units_purchased': units_purchased, 'total_purchase': total_purchases,
#         'dates': dates, 'payment_method': payment_methods, 'workshop_branch': workshop_branches}
#
# #checking the length of each array
# # print(len(customer_ids), len(genders), len(ages), len(items), len(prices_per_unit),
# #       len(units_purchased), len(total_purchases), len(dates), len(payment_methods), len(workshop_branches))
# # # Create the pandas DataFrame
# df = pd.DataFrame(data)
# #
# # # View the DataFrame
# #print(df.head())
#
#
# #df.to_csv('workshop2_MY.csv', index=False)

# import pandas as pd
#
# # Load the DataFrame
# df = pd.read_csv('workshop_MY.csv', parse_dates=['dates'], date_parser=lambda x: pd.datetime.strptime(x, '%d/%m/%y %H:%M:%S'))
#
# # Change the date format of the 'date_purchased' column
# df['dates'] = df['dates'].dt.strftime('%d/%m/%y')
#
# # Display the DataFrame with the updated date format
# print(df.head())
