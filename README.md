# GeoAI-Earthquake-Strength-Classification

📌 Overview

This project explores the use of Machine Learning and Geospatial Analysis to study historical earthquake data and learn spatial patterns of seismic activity.
Using data retrieved from the USGS Earthquake API, the model classifies earthquakes into Weak and Strong categories based on their geographic attributes.


⚠️ Important Note

This project does NOT claim deterministic earthquake prediction.
The term “prediction” is used strictly in a machine-learning sense, referring to post-event classification and pattern learning from historical seismic records.


🎯 Objectives

To analyze global and regional earthquake datasets using data-driven methods
To understand spatial distribution of seismic events
To classify earthquake strength using machine learning models
To visualize seismic risk patterns using geospatial maps


🗂 Data Source

United States Geological Survey (USGS) Earthquake API
Parameters include:
Latitude & Longitude
Magnitude
Depth
Time & Date
All data used in this project is open-source and publicly available.


🧠 Methodology

Data collection using USGS API
Data cleaning and preprocessing
Feature engineering (time, depth, spatial attributes)
Exploratory Data Analysis (EDA)
Machine Learning model development:
Classification (Weak vs Strong)
Regression (magnitude estimation for analysis)
Model evaluation using accuracy, confusion matrix, and R² (where applicable)
Geospatial visualization using maps


🛠 Tools & Technologies

Python
Pandas, NumPy
Scikit-learn
Matplotlib, Seaborn
Folium (Geospatial Visualization)
Google Colab / Jupyter Notebook


🌍 Study Regions

Global earthquake dataset
India-focused analysis
Regional case studies (Delhi, Odisha, Bhubaneswar, Berhampur)

⚠️ Regional models may suffer from data sparsity due to low seismic activity and are included as proof-of-concept demonstrations, not as statistically robust predictors.


📊 Results & Insights

The global model demonstrates meaningful learning of spatial seismic patterns
Machine learning models successfully differentiate weak and strong earthquakes based on historical data
Geospatial maps highlight seismic clustering along tectonically active regions


🚀 Limitations

Earthquake occurrence is governed by complex physical processes not fully captured by spatial features alone
Latitude and longitude cannot determine causation, only historical patterns
Localized regional models are limited by available data


🔮 Future Scope

Integration of tectonic plate boundaries and fault-line data
Use of deep learning and spatio-temporal models
Real-time data streaming for continuous seismic risk monitoring
Extension toward comprehensive Geo-AI risk assessment systems


👤 Author

Bikrant Kumar Mishra
B.Sc. Geology
Interests: Geo-AI, Machine Learning, Earth System Analysis
