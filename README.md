🛒 Smart Product Recommendation System
(Market Basket Analysis using Apriori Algorithm)

This project is a Smart Product Recommendation System built using Python and Streamlit.
It recommends products to users based on items already added to their cart using Market Basket Analysis and the Apriori algorithm.

🔗 Live Deployed App:
https://market-basket-zhnxnv4br6nwdnub3c92rb.streamlit.app/

📌 Project Description

Market Basket Analysis is a technique used to discover relationships between products purchased together.
This application uses association rules (support, confidence, lift) to recommend products in real time.

The app is mobile-friendly and provides:

Cart-based recommendations

Adjustable confidence & lift thresholds

Frequent itemset and rule insights

🚀 Features

🔍 Search and select products dynamically

🧺 Add multiple products to cart

🎯 Get smart product recommendations

🎚️ Adjustable:

Minimum Confidence

Minimum Lift

📊 View:

Frequent Itemsets

Association Rules

📱 Optimized for mobile screens

☁️ Deployed on Streamlit Cloud

🧠 Technologies Used

Python

Streamlit

Pandas

Pickle

mlxtend (Apriori Algorithm)

⚙️ How the System Works

A pre-trained Apriori model is loaded using pickle

User selects products in the Cart tab

The system:

Matches cart items with rule antecedents

Filters rules using confidence & lift

Displays recommended products with:

Confidence

Lift

Support

🖥️ Application Tabs
🧺 Cart

Search products

Select multiple items

View selected cart items

🎯 Recommendations

Set minimum confidence & lift

Get top product recommendations

Sorted by lift and confidence

📊 Insights

View frequent itemsets

View association rules

📂 Project Structure
├── app.py
├── market_basket_model.pkl
├── requirements.txt
├── README.md

▶️ Run Locally
git clone https://github.com/your-username/product-recommendation-system.git
cd product-recommendation-system
pip install -r requirements.txt
streamlit run app.py

📊 Output

Recommended products based on cart

Rule metrics:

Support

Confidence

Lift

Interactive tables

🎯 Use Cases

Retail recommendation systems

E-commerce analytics

Customer purchase pattern analysis

Business intelligence projects
