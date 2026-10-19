# project-auer-weather-data
# (Weather Time Machine) 🌤️

## Overview
Project Auer is a full-stack web application designed to calculate and visualize historical meteorological distributions for specific dates and global coordinates. By ingesting and processing decades of raw historical weather telemetry, the application provides data-driven weather risk assessments and probability modeling for long-term planning. 

Originally conceived to calculate optimal weather windows for high-stakes outdoor event planning (such as forecasting 2028 operational dates), the architecture is directly applicable to site-specific weather risk analysis and energy yield forecasting.

##The Tech Stack
* **Backend:** Python, FastAPI
* **Frontend/Visualization:** MapLibre GL
* **Data Processing:** Python (Pandas/NumPy) for cleaning, filtering anomalies, and statistical modeling of chaotic meteorological datasets.

## ⚙️ Core Engineering Features
* **Data Ingestion & Cleaning:** Built to handle the physical realities of messy meteorological data. The pipeline ingests raw time-series telemetry, handles missing values (NaNs), and filters out sensor anomalies before running statistical distributions.
* **Geospatial Processing:** Translates complex mathematical atmospheric probability into clean, readable MapLibre GL visualizations for immediate user comprehension.
* **FastAPI Architecture:** Lightweight, highly responsive backend designed to query large historical datasets efficiently.

## 🛠️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/project-auer.git](https://github.com/YourUsername/project-auer.git)
