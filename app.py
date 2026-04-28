import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Investment Scoring System", layout="wide")

st.title("📊 Investment Scoring System")
st.write("Analyze firms using return, volatility, and upward trend metrics.")

df = pd.read_excel(r"C:\Users\VAIBHAV\Downloads\investment-scoring-system-main\investment-scoring-system-main\data\Investment_features.xlsx")

# Dataset Preview
with st.expander("📂 View Dataset"):
    st.dataframe(df)

# Top Firms
if "investment_score" in df.columns:
    st.subheader("🏆 Top 10 Firms by Investment Score")
    top = df.sort_values("investment_score", ascending=False).head(10)
    st.dataframe(top)

    fig, ax = plt.subplots()
    ax.bar(top.index.astype(str), top["investment_score"])
    ax.set_title("Top Firms")
    ax.set_xlabel("Firm")
    ax.set_ylabel("Investment Score")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Risk vs Return
if "avg_return" in df.columns and "avg_volatility" in df.columns:
    st.subheader("📈 Risk vs Return")
    fig, ax = plt.subplots()
    ax.scatter(df["avg_volatility"], df["avg_return"])
    ax.set_xlabel("Average Volatility")
    ax.set_ylabel("Average Return")
    ax.set_title("Risk vs Return Scatterplot")
    st.pyplot(fig)

st.markdown("---")
st.caption("Built by Ash | Streamlit Portfolio Project")