📊 Walmart Sales Forecasting & Demand AnalysisAn end-to-end Machine Learning project designed to predict weekly retail sales for Walmart stores. This system leverages historical data, economic indicators, and seasonal patterns to provide actionable business insights for inventory and resource management.🔍 OverviewThis project focuses on building a robust forecasting pipeline using the Walmart Recruiting Dataset. Beyond just predicting numbers, this project interprets how external factors like Unemployment, Fuel Prices, and Holidays impact retail performance.Model: Random Forest Regressor (Chosen for its ability to handle non-linear seasonal spikes).Accuracy: Achieved an R-squared score of 0.89, indicating high reliability for retail planning.Goal: To forecast demand and provide "Business-Ready" recommendations for store managers.📁 Repository StructurePlaintextwalmart-sales-forecasting/
│
├── exploration.ipynb       ← Detailed EDA (Trend, Correlation, & Holidays)
├── sales_forecasting.py    ← Final Machine Learning Script
├── Walmart.csv             ← Historical Dataset (Sales, CPI, Unemployment)
├── requirements.txt        ← Library dependencies
├── README.md
│
└── outputs/
    ├── sales_forecast_plot.png  ← Actual vs. Predicted Visual
    └── forecast_results.csv     ← Exported model predictions
▶️ How to RunClone the repo:git clone https://github.com/Mohith140306/FUTURE_ML_01.git
Install dependencies:pip install pandas numpy scikit-learn matplotlib jupyter
Run the model:python sales_forecasting.py
🗂️ Project WalkthroughThe project follows a structured data science lifecycle:Data Loading: Parsing dates and handling the Walmart-specific CSV structure.Feature Engineering: Extracting Week, Month, and Year to capture holiday seasonality.Exploratory Data Analysis (EDA): Visualizing the massive sales spikes during Black Friday and Christmas.Train/Test Split: Time-series splitting (80% training / 20% testing).Modeling: Training a Random Forest Regressor with 100 estimators.Evaluation: Measuring success via Mean Absolute Error (MAE) and R2 Score.Business Insights: Converting technical metrics into retail strategy.
📊 Model PerformanceThe model was tested on a 20% hold-out "future" period with the following results:MetricResultInterpretationR-squared (R2)0.8929Excellent fit; captures ~90% of sales variance.MAE$97,076On average, predictions are within ~10% of actual values.
📈 Visualizations1. Actual vs. Predicted TrendThis plot confirms that the model accurately anticipates the "spikes" in demand that occur every holiday season.2. Feature ImportanceOur analysis revealed that Store Size and Department ID are the strongest predictors of sales, while Unemployment shows a gradual long-term impact on purchasing power.
🏢 Business Insights & RecommendationsBased on the forecast, the following actions are recommended for Walmart Store Managers:Inventory Optimization: Increase stock levels for top-performing departments 3 weeks prior to the identified "Peak Weeks" (November-December).Labor Scheduling: Schedule additional temporary staff during weeks where the model predicts sales exceeding $1.5M.Economic Buffering: During periods of rising Unemployment, pivot marketing toward "Value" and "Essential" categories to maintain sales volume.
🛠️ Tech StackPython 3: Core logicPandas/NumPy: Data manipulationScikit-Learn: Random Forest modelingMatplotlib/Seaborn: Data visualization
Walmart Recruiting Store Sales Forecasting Dataset — a real-world retail dataset containing historical sales data for 45 Walmart stores located in different regions.
6,435 weekly sales records across various stores and departments.
Date range: February 2010 – October 2012.
Features:
Store: The store number.
Date: The week of sales.
Weekly_Sales: The sales for the given store (Target Variable).
Holiday_Flag: Whether the week is a special holiday week (Super Bowl, Labor Day, Thanksgiving, Christmas).
Temperature: Temperature on the day of sale.
Fuel_Price: Cost of fuel in the region.
CPI: Consumer Price Index.
Unemployment: The prevailing unemployment rate.
Source: Kaggle — Walmart Recruiting - Store Sales Forecasting
👤 Author
[Dappadi Mohith]
Second Year Artificial Intelligence and Machine Learning(AIML) Student
Projects: College Bus Tracking App | Resume Screening System | Sales Forecasting
Built as part of an ML for Business course project | February 2026
