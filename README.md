## Catalyst_Crew_COVID-19_Global_Trend_Dashboard

**Group Members**

Jiya Patel - KU2407U412
<br/>Himanshu Kumar Singh - KU2407U406
<br/>Jiya Chaudhari - KU2407U411
<br/>Chaitya Shah - KU2407U503

---

**Objective Of The Project**

Analyze and visualize COVID-19 case trends and vaccination data by country.

**Tools And Libraries Used**

* Visual Studio Code
* NumPy 
* Pandas
* Matplotlib

---

**Data Source**

Johns Hopkins University COVID-19 Dataset
Our World in Data (OWID)
World Health Organization (WHO)

---

**Execution Steps**

1. Install VS Code
Download and install VS Code from Visual Studio Code.


2. Install Python
Download and install Python from Python.org.
During installation, check the box to "Add Python to PATH."


3. Install Required Libraries
Open a terminal in VS Code (Ctrl+` shortcut) and install the necessary Python libraries:
bash
Copy code
pip install pandas matplotlib


4. Prepare the Dataset
Ensure the covid_trends_vaccination.csv file exists in the same directory as the script.
The file must have the following columns:
Date: Date of the data in YYYY-MM-DD format.
Country: Name of the countries.
New Cases: Number of new COVID-19 cases.
Vaccinations: Number of vaccinations administered.


5. Create the Python Script
Open VS Code.
Create a new file and name it graph_output.py.
Copy and paste the revised code provided earlier into the file.
Save the file.


6. Run the Script
In VS Code:

Open the terminal (Ctrl + ).
Run the script using the command:
bash
Copy code
python graph_output.py


7. View Results
The script will display four graphs sequentially:

Total New Cases by Country
Total Vaccinations by Country
New Cases Trend Over Time
Vaccinations Trend Over Time
These graphs will also be saved as PNG files in the same directory:

total_new_cases_by_country.png
total_vaccinations_by_country.png
new_cases_trend_over_time.png
vaccinations_trend_over_time.png

---

**Summary Of Result**

Case Trends:

The total number of COVID-19 cases varies significantly by country, highlighting differences in outbreak severity.
Over time, case numbers fluctuate, likely reflecting surges, seasonal effects, or interventions like lockdowns.


Vaccination Trends:

Vaccination counts show a progressive increase over time but vary in rate and total by country.
Some countries may demonstrate quicker and more widespread vaccination campaigns than others.


Key Takeaways:

The visualizations highlight disparities in COVID-19 response and the ongoing impact of the pandemic on public health.


**Challenges Faced**

* Misrepresentation: Avoiding the spread of misinformation due to weak analysis or presentation of data.
* Dynamic changes in policies, testing, and vaccine introduction lead to the need for adaptive analysis methods.
* Accessibility: The repository should be accessible to both technical and non-technical users.


