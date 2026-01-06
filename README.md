📌 Overview

This project explores the application of Machine Learning and Geo-Spatial Analysis to classify earthquake strength using historical seismic data. The study integrates geological reasoning with data-driven methods to understand how spatial location and focal depth influence earthquake energy release patterns.
The work is designed as an exploratory GeoAI mini-project, suitable for academic portfolios and graduate-level research preparation.


🎯 Objectives

Analyze global earthquake data using machine learning techniques
Classify earthquakes into Weak and Strong categories
Investigate the influence of spatial clustering and depth on seismic strength
Apply model explainability to validate geological reasoning behind predictions


🗂 Data Source

United States Geological Survey (USGS) Earthquake API
Parameters used:
Latitude
Longitude
Focal depth (km)
Magnitude
Time of occurrence
All data used are open-source and publicly available.


🧠 Methodology

Retrieval of historical earthquake data using the USGS API
Data cleaning and preprocessing
Feature selection using spatial coordinates and focal depth
Earthquake strength classification using a Random Forest model
Handling class imbalance with balanced class weighting
Model robustness assessment using Stratified K-Fold Cross-Validation
Model interpretability using SHAP (SHapley Additive exPlanations)
Geological visualization using spatial maps and seismic cross-sections


🛠 Tools & Technologies

Python
Pandas, NumPy
Scikit-Learn
SHAP
Matplotlib, Seaborn
Folium (Geospatial Visualization)


📊 Results & Visualizations

Classification of earthquake strength (Weak vs Strong)
Spatial clustering of strong seismic events along tectonically active regions
SHAP-based feature importance highlighting the role of depth and spatial location
Seismic depth–magnitude profile to examine vertical seismicity structure


🧠 Model Discussion and Geological Interpretation

The model utilizes spatial proxies (latitude and longitude) together with focal depth to classify earthquake strength based on historical seismicity patterns. Latitude and longitude act as indirect indicators of tectonic settings, enabling the Random Forest classifier to learn clustering behavior along major plate boundaries, including circum-Pacific and other globally active seismic belts.
The inclusion of depth_km plays a critical role in the model’s logic. SHAP-based explainability analysis indicates that focal depth contributes significantly to classification outcomes, reflecting well-established differences between shallow crustal earthquakes and deeper subduction-zone events. These depth-dependent variations are consistent with seismological understanding of brittle upper-crustal failure versus deeper slab-related seismicity.
To address the natural rarity of large-magnitude earthquakes, balanced class weighting was applied during model training. This prevents bias toward low-magnitude events and allows a more representative classification of seismic energy release patterns. Overall, the model captures geologically meaningful trends rather than relying solely on spatial memorization.


🌍 Geological Context

This study interprets seismic classification in the context of the Gutenberg–Richter magnitude–frequency relationship, where high-magnitude earthquakes represent greater energy release but occur less frequently.
Spatial coordinates serve as surrogates for tectonic boundaries, while focal depth reflects variations in deformation regimes across the lithosphere. The integration of SHAP explainability enables transparent interpretation of how spatial location and depth jointly influence earthquake strength classification, aligning machine-learning outputs with established principles of earthquake generation and tectonic processes.


🔮 Scope for Further Improvement

While the current framework is appropriate for a mini-project and exploratory GeoAI study, further enhancements could be introduced at a graduate research or master’s thesis level:
Tectonic Feature Engineering: Incorporating distance to the nearest plate boundary or fault system using geological or GeoJSON datasets to reduce reliance on latitude–longitude as indirect spatial proxies.
Spatio-Temporal Features: Introducing temporal variables such as time since the last significant seismic event within a defined spatial radius to better capture seismic recurrence and clustering behavior.
Such extensions would move the framework toward advanced seismic risk modeling rather than purely spatial classification.


👤 Author

Bikrant Kumar Mishra
B.Sc. Geology
Interests: GeoAI, Machine Learning, Seismology, Earth System Analysis
