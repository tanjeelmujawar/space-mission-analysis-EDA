# 🚀 Space Mission Analysis

## Overview
This project explores **global space missions**, analyzing rockets, launch sites, mission success rates, and country contributions. The goal is to understand **which countries and rockets dominated space exploration**, **why certain launch sites were preferred**, and **seasonal trends in rocket launches**.

The analysis is beginner-friendly and uses **Python (pandas, matplotlib, seaborn)** to visualize and interpret the data.

---

## Dataset
The dataset contains historical space mission data with columns like:

- `Company` – Company responsible for the space mission 
- `Location` – Location of the launch 
- `Date` – Date of the launch 
- `Time` – Time of the launch (UTC)  
- `Rocket` – Name of the rocket used for the mission
- `Mission` – Name of the space mission (or missions)
- `RocketStatus` - Status of the rocket as of August 2022 (Active or Inactive)
- `Price` - Cost of the rocket in millions of US dollars
- `MissionStatus` -  Status of the mission (Success, Failure, Partial Failure, Prelaunch Failure)

---

## Steps I Followed

1. **Data Understanding:** Explored dataset columns, checked missing values and data types.  
2. **Data Cleaning & Feature Engineering:** Created `SuccessFlag` and `Still_active_rockets`.  
3. **Exploratory Data Analysis (EDA):** Analyzed success rates, rocket usage, launch sites, and monthly trends.  
4. **Visualization:** Created bar and pie charts with high-resolution colormaps.  
5. **Insights & Interpretation:** Combined historical, geographical, and technical context to explain trends.  
6. **Documentation:** Wrote beginner-friendly explanations and conclusions in the notebook and Final Interpretation document.

---

## Analysis Performed

1. **Mission Success by Country**  
   - Created a `SuccessFlag` column to mark successful missions.  
   - Analyzed success rates by country.  
   - **Historical context:** Russia leads due to the early space race; Japan and India lagged due to WWII, nuclear disasters, and colonial rule.

2. **Rocket Analysis**  
   - Counted launches per rocket and identified top rockets like **Cosmos-3M, Voskhod, and Soyuz U**.  
   - Created `Still_active_rockets` to track which rockets are still active.  
   - Discussed rocket specifications, reliability, and payload specialization.

3. **Launch Site Analysis**  
   - Identified top launch locations and their mission success rates.  
   - Explained **geography, climate, and environmental reasoning**:  
     - **Baikonur Cosmodrome (Kazakhstan)** – remote, flat, safe for debris.  
     - **Plesetsk Cosmodrome (Russia)** – ideal for polar orbits.  
     - **Kennedy Space Center (USA)** – over the Atlantic for safe trajectories.  
     - **ELA-2, Guiana (France)** – near the equator for natural boost.  

4. **Monthly Launch Trends**  
   - Counted launches per month to observe seasonal patterns.  
   - Explained variations due to **weather, daylight, orbital mechanics, and operational planning**.

---

## Visualizations

- Bar charts for top rockets, launch sites, and monthly launches  
- Pie charts for mission success rates by country and launch site  
- Rocket status (Active/Retired) visualizations  
- High-resolution charts (`dpi=600`) with colormaps like `viridis`, `coolwarm`, `rainbow`, `plasma`  

These visuals make it easy to **understand patterns and trends** in space missions.

---

## Key Insights

- **Russia and USA** dominate space exploration, followed by Kazakhstan (launch sites) and China.  
- A few **reliable rockets** handled most launches (Cosmos-3M, Voskhod, Soyuz U).  
- **Launch sites** were chosen based on **geography, climate, and safety**, not randomly.  
- Seasonal trends exist, with more launches in months with favorable **weather and orbital windows**.  
- Historical events like **WWII, nuclear disasters, and colonial rule** affected the timing and frequency of launches for some countries.

---

## Tools & Libraries
` EDA & Data Cleaning`

`Python`

`pandas`

`matplotlib`

`seaborn`

---

## ✨ Author
Mujawar Tanjeel Mahamadrafik.

