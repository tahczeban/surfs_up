# surfs_up

***RESOURCES*** Jupyter notebook, Python, Flask, Pandas, Numpy, matplotlib, ORM, SQAlchemy, SQlite

***OVERVIEW***
The purpose of this project was to analyze various weather stations in Oahu, Hawaii to inquire if it is feasible to open a "surf 'n shake" shop year round, as oppposed to seasonally, with investor W.Avy. An indepth analysis of temperature and precipitation trends in Oahu, Hawaii for June and December was completed, as these 2 weather factors are the biggest contributors to optimal outdoor experiences of all types, particularly surfing and beach attendance. In order to accomplish this, the following had to be performed:
1. analyze advanced data storage with Python and Pandas
2. filter the date column of the measurements table from hawaii.sqlite db
3. retrieve temps and precipitation for june and dec
4. convert to a list and create a dataframe 
5. integrate the statistics with the dataframe 
6. create graphs and tables utilizing Python


In figure 1, the temperature and precipitation collected via weather station analysis was observed for the overall trends and translated to graphical format for easy interpretation. 

![temp](https://user-images.githubusercontent.com/90135381/147972203-6f0ab197-865e-4902-b1a4-96f758a6ed62.png)


![precip-by-date](https://user-images.githubusercontent.com/90135381/147970011-76bc208e-2d44-4349-a53c-7095e0461e35.png)

Figure 1: Graphs of Temperature and Precipitation trends

***RESULTS***

DELIVERABLE 1: Summary Statistics for June Temp was performed for comparison. The average temperature for June was 75, the minimum temp was 64 and the max temp was 85 (Fig 2).

<img width="227" alt="june_temp_df" src="https://user-images.githubusercontent.com/90135381/147968493-6072ea3b-72c7-4189-b545-a502046f43fc.png">
Figure 2: Statistical Data of June Temperatures

DELIVERABLE 2: Summary Statistics for December Temp was performed for comparison.The average temperature for December was 71, the min temp was 56 and the max temp was 83 (Fig 3).

<img width="186" alt="dec_temp_df" src="https://user-images.githubusercontent.com/90135381/147968505-2d54ab62-63f3-4b9c-9ca6-68f0d7b15630.png">
Figure 3: Statistical Data of December Temperatures


***SUMMARY***

*DELIVERABLE 3: An additional inquiry for Precipitation was performed, as the amount of rain for those two seasons would also likely be directly proportional to shop and beach attendance; hence, success. Junes precipitation average was 0.136, with max being 4.430 (Fig4).

<img width="218" alt="june_precipitation" src="https://user-images.githubusercontent.com/90135381/147968470-471cd76a-129d-45a1-bdb4-c90ae4df31d2.png">
Figure 4: Stats of June Precipitation

For December, the statistical data showed that the average rainfall was 0.217, with the max rainfall being 6.420 (Fig 5).

<img width="202" alt="dec_precipitation" src="https://user-images.githubusercontent.com/90135381/147968438-0714aad2-361d-433d-a666-06705aa417db.png">
Figure 5: Stats of December Precipitation


In conclusion, it can be ascertained that opening a year-round surf and shake shop at the beach would be a feasible business option. The average temperature variance was negligable (~4 deg) for the 2 most extreme months. Additionally, while the precipitation was more predominant in December, the amount was only by a small margin (~2); thus, making Oahu, Hawaii an optimal location for the "surf 'n shake" shop. 

***REFERENCES*** BSC, Google, StackOverflow, GitHub
