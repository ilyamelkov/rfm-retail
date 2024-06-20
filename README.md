# RFM Analysis of Retail Store Customers
 This repository contains notebooks with data cleaning, RFM scores calculations and various RFM visualisations.

 Chronological order of notebooks:
  - rfm_retail_data_prep.ipynb
  - rfm_retail_rfm_calc.ipynb
  - rfm_retail_vis.ipynb
  - rfm_retail_seg_flows.ipynb

RFM calculations were performed based on the 33rd and 66th percentiles, leading to 27 possible RFM scores for each customer. The highest possible score for R, F, and M is 3.
Each customer was assigned one of 6 labels/segments based on their respective RFM score. The 'rfm3366_labels_eng_ru.xlsx' is where labels and segments can be examined. The analysis of customer segment changes from year to year resulted in recommendations (rfm_retail_seg_flows.ipynb) for the upcoming period.

 Data Source:  https://www.kaggle.com/datasets/mathchi/online-retail-ii-data-set-from-ml-repository/data

 'rfm_fun.py' contains functions related to RFM. Results of a function which calculates RFM scores can be seen in a folder called 'rfm_tables' 
