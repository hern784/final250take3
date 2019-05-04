README for ML1.py

How to read machine learning design for ML1.py:

This ML1.py is designed to predict the cost for electric bill based on the data from April2018, August 2018, December 2018.
Total of 3 months.

daytime.txt has 92 data. 
The left value indicates the high temperature, and right value indicates the cost (kWh).
line 1 - 30 indicates the high temperature of april 2018
line 31 - 61 indicates the high temperature of august 2018
line 62 - 92 indicates the high temperature of december 2018
This is the weather for Los angeles back in 2018.
The website I am using to get this data is:
https://www.accuweather.com/en/us/los-angeles-ca/90027/april-weather/37860_pc?monyr=4/1/2018&view=table
https://www.accuweather.com/en/us/los-angeles-ca/90027/august-weather/37860_pc?monyr=8/1/2018&view=table
https://www.accuweather.com/en/us/los-angeles-ca/90027/month/37860_pc?monyr=6/01/2018
https://www.accuweather.com/en/us/los-angeles-ca/90027/december-weather/37860_pc?monyr=12/1/2018

For calculating the cost (kWh), I used the value from Table 2. HVAC Mode Energy Cost from procedure of the project.
The cost for kWh is 10 cents.
All temperatures are in Farenheit.
For left value:
Less than or equal to 65 uses heater. The cost rate for this is $0.35 (35cents).
Temperature between greater than 65 and 74.9 either opens the door or close the door. The cost rate for this is $0.00.
Temperature between 75 and 79.9 uses Fan. The cost rate for this is $0.05 (5cents).
Temperature higher than 80 uses AC. The cost rate for this is $0.45 (45cents).

The graph has a linear line, which predicts the minimum cost for electric bill depending on the temperature.
The equation of a linear line is y = -0.97412557 + 0.01550335x. x is the temperature variable, and y is the cost variable.

The average high temperature for april 2018 was 73 degree. If we plug 73 degree into a linear line we get $.1576 per day.
The average high temperature for august 2018 was 84 degree. If we plug 84 degree into a linear line we get $.328 per day.
The average high temperature for december 2018 was 68 degree. If we plug 68 degree into a linear line we get $0.08 per day.
The total cost for april 2018 is $.1576 times 30, we get $4.728.
The total cost for august 2018 is $.328 times 30, we get $10.17.
The total cost for december 2018 is $.0.08 times 30, we get $2.48.

The result from line 28 - 33 are prediction for minimum cost of electric bill.

The real value for the total cost(kWH) for april 2018 is $3.15.
The real value for the total cost(kWH) for august 2018 is $13.95.
The real value for the total cost(kWH) for april 2018 is $2.25.

You can predict minimum cost by using a linear line.
For example, the average high temperature for february 2018 was 70 degree. Then the cost of electric bill per day is 
$.1111. The total cost(kWH) for that month is $3.33.

The formula I used to implement ML1.py is Linear least squares solution.

