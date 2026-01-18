# Smart Product Recommendation System

## Market Basket Analysis using Apriori Algorithm

This project is a Smart Product Recommendation System built using Python and Streamlit.
It recommends products based on items added to the cart using Market Basket Analysis and the Apriori algorithm.

Live App:
https://market-basket-zhnxnv4br6nwdnub3c92rb.streamlit.app/

---

## Project Description

Market Basket Analysis is used to find relationships between products purchased together.
This application uses association rules such as support, confidence, and lift to recommend products in real time.

The application provides:

- Cart based recommendations
- Adjustable confidence and lift values
- Frequent itemset and association rule insights

---

## Features

- Search and select products
- Add multiple products to cart
- Smart product recommendations
- Adjustable minimum confidence
- Adjustable minimum lift
- View frequent itemsets
- View association rules
- Mobile friendly interface
- Deployed on Streamlit Cloud

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Pickle
- mlxtend (Apriori Algorithm)

---

## How the System Works

1. Pre-trained Apriori model is loaded using pickle
2. User selects products in the cart
3. Selected products are matched with rule antecedents
4. Rules are filtered using confidence and lift
5. Recommended products are displayed with support, confidence, and lift

---

## Application Tabs

### Cart Tab
- Search products
- Select multiple items
- View selected cart items

### Recommendations Tab
- Set minimum confidence
- Set minimum lift
- View top recommendations

### Insights Tab
- View frequent itemsets
- View association rules

---

## Run Locally

git clone https://github.com/your-username/product-recommendation-system.git  
cd product-recommendation-system  
pip install -r requirements.txt  
streamlit run app.py  

---

## Output

- Recommended products based on cart items
- Support, confidence, and lift values
- Interactive tables

---

## Use Cases

- Retail recommendation systems
- E-commerce analytics
- Customer behavior analysis
- Business intelligence projects

---

## Author

Divyanshi Kumari 

---

## License

This project is for educational and academic purposes only.

