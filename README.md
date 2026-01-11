# 📊 Commodity Price Trend Analysis Dashboard (India)

## 📌 Project Overview
This project analyzes agricultural commodity price trends across Indian markets using historical arrival and price data.  
The objective is to identify price movements over time, regional price variations, seasonal patterns, and commodity-wise volatility, and present insights through an interactive Power BI dashboard.

This project was developed as part of my internship work and demonstrates an end-to-end data analytics workflow — from raw data cleaning to dashboard creation.

---

## 📂 Dataset Description
The raw dataset consists of commodity-wise CSV files with the following columns:

- State  
- District  
- Market  
- Commodity  
- Commodity Code  
- Arrival Date  
- Minimum Price  
- Maximum Price  
- Modal Price  

Prices were originally recorded in **₹ per quintal**.

---

## 🔄 Data Cleaning & Preparation

### Data Transformation
- Converted all prices from ₹ per quintal to ₹ per kg
- Standardized column names and formats
- Handled missing and inconsistent values

### Outlier Handling
- Identified and removed unrealistic price ranges
- Applied price range corrections using Python scripts

### Feature Engineering
Derived additional analytical columns from arrival date:
- Year  
- Month  
- Month-Year  
- Season  

### Data Integration
- Combined 14 individual commodity CSV files into a single consolidated dataset
- Data cleaning and merging performed using Python (Pandas) in VS Code

---

## 🛠 Tools & Technologies Used
- Python (Pandas, NumPy) – Data cleaning & preprocessing  
- Power BI – Data modeling, DAX measures, dashboard creation  
- VS Code – Script development  
- GitHub – Version control and documentation  

---

## 📊 Power BI Dashboard Features

### Key Insights
- Average, minimum, and maximum price trends
- Year-wise and month-wise price movement
- Seasonal price behavior
- State-wise and district-wise price comparison
- Commodity-level price volatility
- Identification of most expensive and cheapest commodities

### Visuals Used
- KPI Cards
- Line Charts (price trends over time)
- Bar Charts (commodity & regional comparison)
- Filled Map (state-wise price overview)
- Interactive slicers for Commodity and Year

---

## 📸 Dashboard Preview
Screenshots of key dashboard pages are available in the `screenshots` folder.

---

## 🎯 Key Learnings
- Handling large real-world datasets
- Cleaning and validating price data
- Feature engineering for time-series analysis
- Building interactive dashboards in Power BI
- Structuring and documenting a professional data analytics project

---

## 📌 Conclusion
This project demonstrates practical experience in data cleaning, analysis, and visualization using real-world agricultural price data.  
It reflects the ability to manage complete analytics pipelines and present insights effectively for decision-making.

---

## 👧 Author
Prerna Rai   
<a href="https://www.linkedin.com/in/prerna-rai-11j/">LinkedIn Profile</a> 
