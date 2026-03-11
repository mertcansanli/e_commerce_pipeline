import pandas as pd
import random
from datetime import datetime, timedelta

# kaç satır üretilecek
N = 1200

product_categories = ["Laptop", "Phone", "Tablet", "Wearable"]
segments = ["Consumer", "Corporate", "Enterprise"]
regions = {
    "APAC": ["China", "Japan", "Australia"],
    "NA": ["US", "Canada"],
    "EMEA": ["Germany", "France"],
    "LATAM": ["Brazil"]
}

us_states = ["CA", "NY", "WA", "IL", "TX", "GA", "OH"]

shipping_types = ["Standard", "Express", "Same Day"]
order_channels = ["Online", "Retail", "Partner"]
payment_methods = ["Credit Card", "PayPal", "Apple Pay", "Gift Card"]

# kategori bazlı ortalama fiyat
price_ranges = {
    "Laptop": (900, 3000),
    "Phone": (400, 1500),
    "Tablet": (300, 1200),
    "Wearable": (150, 700)
}

start_date = datetime(2024,1,1)
end_date = datetime(2025,12,31)

rows = []

for i in range(N):

    order_id = f"ORD-{30001+i}"

    order_date = start_date + timedelta(
        days=random.randint(0, (end_date-start_date).days)
    )

    category = random.choice(product_categories)
    segment = random.choice(segments)

    quantity = random.randint(1,7)

    base_price = random.uniform(*price_ranges[category])
    sales = round(base_price * quantity, 2)

    margin = random.uniform(0.15, 0.35)
    profit = round(sales * margin, 2)

    returned = random.choices(["Y","N"], weights=[0.1,0.9])[0]
    delivered_on_time = random.choices(["Y","N"], weights=[0.85,0.15])[0]

    region = random.choice(list(regions.keys()))
    country = random.choice(regions[region])

    state = ""
    if country == "US":
        state = random.choice(us_states)

    shipping = random.choice(shipping_types)
    channel = random.choice(order_channels)
    payment = random.choice(payment_methods)

    customer_id = f"CUST-{random.randint(1000,1500)}"

    rows.append([
        order_id,
        order_date.strftime("%m/%d/%y"),
        category,
        segment,
        quantity,
        sales,
        returned,
        delivered_on_time,
        region,
        country,
        shipping,
        state,
        channel,
        payment,
        profit,
        customer_id
    ])

columns = [
    "Order ID",
    "Order Date",
    "Product Category",
    "Segment",
    "Quantity",
    "Sales",
    "Returned?",
    "Delivered On Time?",
    "Region",
    "Country",
    "Shipping Type",
    "US State",
    "Order Channel",
    "Payment Method",
    "Profit",
    "Customer ID"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("ecommerce_dataset2.csv", index=False)

print("CSV oluşturuldu: ecommerce_dataset2.csv")