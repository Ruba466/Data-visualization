import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Interactive Data Visualization App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.subheader("Preview of Dataset")
    st.write(df.head())
    
    #Histogram of total_bill
    st.subheader("Histogram of Total Bill")
    if 'total_bill' in df.columns:
        fig1, ax1 = plt.subplots()
        sns.histplot(df['total_bill'], bins=20, kde=True, color='lightgreen', edgecolor='black', ax=ax1)
        st.pyplot(fig1)
    else:
        st.warning("Column 'total_bill' not found.")
        
    #Boxplot of tip
    st.subheader("Boxplot of Tip Amount")
    if 'tip' in df.columns:
        fig2, ax2 = plt.subplots()
        sns.boxplot(y=df['tip'], color='lightblue', ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("Column 'tip' not found.")
        
    #Pie chart of gender distribution
    st.subheader("Pie Chart of Gender Distribution")
    if 'sex' in df.columns:
        gender_counts = df['sex'].value_counts()
        fig3, ax3 = plt.subplots()
        ax3.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90,
                colors=['lightpink', 'lightblue'], wedgeprops={'edgecolor': 'black'})
        ax3.axis('equal')
        st.pyplot(fig3)
    else:
        st.warning("Column 'sex' not found.")
        
    #Bar chart of average total bill by day
    st.subheader("Bar Chart of Avg Total Bill by Day")
    if 'day' in df.columns and 'total_bill' in df.columns:
        avg_total_by_day = df.groupby('day')['total_bill'].mean().sort_index()
        fig4, ax4 = plt.subplots()
        sns.barplot(x=avg_total_by_day.index, y=avg_total_by_day.values, color='lightblue', ax=ax4)
        ax4.set_xlabel("Day")
        ax4.set_ylabel("Avg Total Bill")
        st.pyplot(fig4)
    else:
        st.warning("Columns 'day' and/or 'total_bill' not found.")
else:
    st.info("Please upload a CSV file to begin.")