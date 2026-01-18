import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Product Recommendation System",
    layout="centered"  # IMPORTANT for mobile
)

# ---------------- LOAD MODEL ----------------
with open("market_basket_model.pkl", "rb") as f:
    model = pickle.load(f)

rules = model["rules"]
frequent_itemsets = model["frequent_itemsets"]

# ---------------- PRODUCT LIST ----------------
all_products = sorted(
    set(item for items in frequent_itemsets["itemsets"] for item in items)
)

# ---------------- HEADER ----------------
st.title("🛒 Smart Product Recommendation")
st.caption("Market Basket Analysis using Apriori Algorithm")

# ---------------- TABS (MOBILE FRIENDLY) ----------------
tab1, tab2, tab3 = st.tabs(
    ["🧺 Cart", "🎯 Recommendations", "📊 Insights"]
)

# ================= TAB 1 : CART =================
with tab1:
    st.subheader("🛍️ Add Products to Cart")

    search_query = st.text_input(
        "🔍 Search Product",
        placeholder="Type product name..."
    )

    if search_query:
        filtered_products = [
            p for p in all_products if search_query.lower() in p.lower()
        ]
    else:
        filtered_products = all_products

    selected_products = st.multiselect(
        "Select Products",
        filtered_products
    )

    if selected_products:
        st.success("Products in Cart")
        for p in selected_products:
            st.write("•", p)
    else:
        st.info("No products selected yet")

# ================= TAB 2 : RECOMMENDATION =================
with tab2:
    st.subheader("🎯 Recommended Products")

    col1, col2 = st.columns(2)

    with col1:
        min_conf = st.slider(
            "Minimum Confidence",
            0.1, 1.0, 0.4
        )

    with col2:
        min_lift = st.slider(
            "Minimum Lift",
            1.0, 10.0, 1.0
        )

    if selected_products:
        cart = set(selected_products)
        recommendations = []

        for _, row in rules.iterrows():
            antecedents = set(row["antecedents"])
            consequents = set(row["consequents"])

            if antecedents.issubset(cart):
                if row["confidence"] >= min_conf and row["lift"] >= min_lift:
                    recommendations.append({
                        "Product": ", ".join(consequents),
                        "Confidence": round(row["confidence"], 2),
                        "Lift": round(row["lift"], 2),
                        "Support": round(row["support"], 2)
                    })

        if recommendations:
            rec_df = pd.DataFrame(recommendations)
            rec_df = rec_df.sort_values(
                by=["Lift", "Confidence"],
                ascending=False
            )

            st.success("Top Recommendations")
            st.dataframe(
                rec_df,
                use_container_width=True
            )
        else:
            st.warning("No strong recommendations found")
    else:
        st.info("Add products in Cart tab to get recommendations")

# ================= TAB 3 : INSIGHTS =================
with tab3:
    st.subheader("📦 Frequent Itemsets")
    st.dataframe(
        frequent_itemsets.sort_values("support", ascending=False),
        use_container_width=True
    )

    st.subheader("🔗 Association Rules")
    st.dataframe(
        rules[[
            "antecedents",
            "consequents",
            "support",
            "confidence",
            "lift"
        ]].sort_values("lift", ascending=False),
        use_container_width=True
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("📱 Optimized for Mobile | 🚀 Deployed on Streamlit")
