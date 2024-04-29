import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Reading dataset from csv file
ds = pd.read_csv('vaccinations.csv')

# Converted data column to datetime object in pyhton for easier handling
ds['date'] = pd.to_datetime(ds['date'])


# exluded these rows from dataset to filter countries names data only
countriesOnly=ds[~ds['location'].isin(['World', 'Low income', 'Lower middle income', 'Upper middle income', 'High income', 'Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania'])]

# List of continent names
continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania']

# Filter the DataFrame to include only rows where the location is a continent
continentData = ds[ds['location'].isin(continents)]

# function to create a lino plot
def visualization1():
     total = countriesOnly.groupby('date')['total_vaccinations'].sum() # Makes a group of data and total_vaccination column

     # Plotting the Line Plot for Total Vaccinations over time
     plt.figure(figsize=(10, 6))
     sns.lineplot(total)
     plt.title('Total Vaccinations Over Time')
     plt.xlabel('Date')
     plt.ylabel('Total Vaccinations')
     plt.show()

     pass

# Ploting a Pie Chart for Percentage of Vaccinated Peopple in the Continents
def visualization2():
     continentData = ds[ds['location'].isin(['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania'])]

     # Groupinh data by continent and sum the total people vaccinated
     vaccinatedByContinent = continentData.groupby('location')['people_vaccinated'].sum()

     # Creating the pie chart
     plt.figure(figsize=(8, 8))
     plt.pie(vaccinatedByContinent, labels=vaccinatedByContinent.index, autopct='%1.1f%%', startangle=140)
     plt.title('People Vaccinated in Continents (of the total people vaccinated)')
     plt.show() 

     pass

# Function to Plot Line graph for total vaccinations and daily vaccination
def visualization3():
     # Grouping the data by date and sum the total vaccinations and total boosters
     grouped = countriesOnly.groupby('date').agg({'total_vaccinations':'sum', 'daily_vaccinations':'sum'}).reset_index()

     # Seting up the figure and axes
     plt.figure(figsize=(12, 6))

     # Ploting the line for total vaccinations
     plt.plot(grouped['date'], grouped['total_vaccinations'], label='Total Vaccinations', color='blue', marker='o')

     # Ploting the line for total boosters
     plt.plot(grouped['date'], grouped['daily_vaccinations'], label='Daily Vaccinations', color='red', marker='o')

     # Seting labels and title
     plt.xlabel('Date')
     plt.ylabel('Total')
     plt.title('Total Vaccinations vs Total Boosters Over Time')
     plt.legend()

     # Show plot
     plt.grid(True)
     plt.tight_layout()
     plt.show()

     pass

# Function to plot line plot for  vaccinated people vs fully vaccinated peole
def visualization4():
     # Group the data by date and sum the people vaccinated and people fully vaccinated
     grouped1 = countriesOnly.groupby('date').agg({'people_vaccinated':'sum', 'people_fully_vaccinated':'sum'}).reset_index()

     # Seting up the figure and axes
     plt.figure(figsize=(12, 6))

     # Ploting the line for people vaccinated
     plt.plot(grouped1['date'], grouped1['people_vaccinated'], label='People Vaccinated', color='blue', marker='o')

     # Ploting the line for people fully vaccinated
     plt.plot(grouped1['date'], grouped1['people_fully_vaccinated'], label='People Fully Vaccinated', color='green', marker='o')

     # Seting labels and title
     plt.xlabel('Date')
     plt.ylabel('Total')
     plt.title('People Vaccinated vs People Fully Vaccinated Over Time')
     plt.legend()

     # Show plot
     plt.grid(True)
     plt.tight_layout()
     plt.show()

     pass

# funtion to plot stack bar chart for total vaccinations vs people vaccinated
def visualization5():
     

     # filtering the Dataset to include only the rows besides the last date for each continent
     latestContinentData = continentData[continentData['date'] == continentData.groupby('location')['date'].transform('max')]

     # Grouping data by continent and summing up the total vaccinations and total people vaccinated
     continentSum = latestContinentData.groupby('location')[['total_vaccinations', 'people_vaccinated']].sum()

     # Creating the plot
     fig, ax = plt.subplots(figsize=(10, 6))
   
     # Plotting total vaccinations and people vaccinated for each continent
     continentSum.plot(kind='bar', stacked=True, ax=ax)

     # Adding labels and title
     ax.set_xlabel('Continent')
     ax.set_ylabel('Number of Vaccinations')

     # Setinh up y-axis labels in millions format
     ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}B'.format(x * 1e-9)))

     ax.set_title('Total Vaccinations and People Vaccinated per Continent (2021-08-11)')

     ax.legend(labels=['Total Vaccinations', 'People Vaccinated'])


     # Displaying the plot
     plt.tight_layout()
     plt.show()
    

     pass

# function to create line lot for total vaccinations per hundred vs people vaccinated per hundren in USA and Pakistan
def visualization6():
     usaPakData = ds[ds['location'].isin(['United States', 'Pakistan'])]

     # Pivoting the Dataset to have separate columns for each atrribute (total_vaccinations_per_hundred and people_vaccinated_per_hundred)
     usaPakP = usaPakData.pivot(index='date', columns='location', values=['total_vaccinations_per_hundred', 'people_vaccinated_per_hundred'])

     # Ploting the data
     fig, ax = plt.subplots(figsize=(10, 6))

     # Ploting lines for total vaccinations per hundred and people vaccinated per hundred for USA
     ax.plot(usaPakP.index, usaPakP[('total_vaccinations_per_hundred', 'United States')], label='Total Vaccinations per Hundred (USA)', color='blue')
     ax.plot(usaPakP.index, usaPakP[('people_vaccinated_per_hundred', 'United States')], label='People Vaccinated per Hundred (USA)', color='green')

     # Ploting lines for total vaccinations per hundred and people vaccinated per hundred for Pakistan
     ax.plot(usaPakP.index, usaPakP[('total_vaccinations_per_hundred', 'Pakistan')], label='Total Vaccinations per Hundred (Pakistan)', color='orange')
     ax.plot(usaPakP.index, usaPakP[('people_vaccinated_per_hundred', 'Pakistan')], label='People Vaccinated per Hundred (Pakistan)', color='red')

     # Adding labels, title, and legend
     ax.set_xlabel('Date')
     ax.set_ylabel('Vaccination Rate per Hundred')
     ax.set_title('Comparison of Vaccination Rates per Hundred between USA and Pakistan')
     ax.legend()

     # Rotate x-axis labels for better readability
     plt.xticks(rotation=45)

     # Show plot
     plt.tight_layout()
     plt.show()
     pass


def visualization7():
     # Filtering European countries
     europeanCountries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
                      'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
                      'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania',
                      'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia',
                      'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia',
                      'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City']

     europeanDs = ds[ds['location'].isin(europeanCountries)]

# Grouping data by country and sum the total number of vaccinated people
     countryVaccinations = europeanDs.groupby('location')['people_vaccinated'].max().sort_values(ascending=False)

# Selecting the top ten most vaccinated countries in Europe
     topEuropeanCountries = countryVaccinations.head(10)

# Converting numbers to millions
     topeuropeanCountriesM = topEuropeanCountries / 1e6

# Creating the horizontal bar chart
     fig, ax = plt.subplots(figsize=(10, 6))

# Ploting the data
     topeuropeanCountriesM.plot(kind='barh', color='lightblue', ax=ax)

# Adding labels and title
     ax.set_xlabel('Total Number of Vaccinated People (Millions)')
     ax.set_ylabel('Country')
     ax.set_title('Top Ten Most Vaccinated Countries in Europe')

# Display the plot
     plt.tight_layout()
     plt.show()

     pass

def visualization8():

     #filtering to choose the data from just income type rows
     incomeTypes = ['Low income', 'Lower middle income', 'Upper middle income', 'High income']
     incomeData = ds[ds['location'].isin(incomeTypes)]

     #Grouping data by income type and find the maximum value for each group
     incomeSummary = incomeData.groupby('location')[['people_vaccinated', 'people_fully_vaccinated']].max()

     #Converted numbers to billions
     incomeSummaryB = incomeSummary / 1e9  

     #Created the grouped bar chart
     incomeSummaryB.plot(kind='bar', figsize=(10, 6))  

     #Adding labels and title
     plt.xlabel('Income Type')
     plt.ylabel('Number of People (Billion)') 
     plt.title('Comparison of Maximum Vaccinated and Fully Vaccinated People by Income Type')

     #Updating legend labels
     plt.legend(['Max People Vaccinated', 'Max People Fully Vaccinated'])

     #Show the plot
     plt.tight_layout()
     plt.show()

     pass

def visualization9():
     # Selecting required columns for the grouped bar chart
     selectedColumn = ['people_vaccinated', 'people_fully_vaccinated', 'total_boosters']

     # Calculateing the mean of each column
     columnMean = countriesOnly[selectedColumn].mean()

     # Creating the grouped bar chart
     plt.figure(figsize=(10, 6))
     columnMean.plot(kind='bar', color=['blue', 'orange', 'green'])

     # Adding labels and title
     plt.xlabel('Vaccination Attribute')
     plt.ylabel('Mean Value')
     plt.title('Comparison of Vaccination Attributes')
     plt.xticks(range(len(columnMean)), ['People Vaccinated', 'People Fully Vaccinated', 'Total Boosters'])

     # Show the plot
     plt.tight_layout()
     plt.show()

     pass

def visualization10():
     fullyVaccinatedData = countriesOnly[['date', 'people_fully_vaccinated']]

     # Converting date column to datetime type
     fullyVaccinatedData['date'] = pd.to_datetime(fullyVaccinatedData['date'])

     # Seting date column as index
     fullyVaccinatedData.set_index('date', inplace=True)

     # Creating the time series plot
     plt.figure(figsize=(12, 8))
     plt.plot(fullyVaccinatedData.index, fullyVaccinatedData['people_fully_vaccinated'], marker='o', linestyle='-')

     # Adding labels and title
     plt.xlabel('Date')
     plt.ylabel('Number of People Fully Vaccinated')
     plt.title('Time Series of People Fully Vaccinated Over Time')

     # Show the plot
     plt.grid(True)
     plt.tight_layout()
     plt.show()
     pass

def visualization11():
     ukData = ds[ds['location'] == 'United Kingdom']
     usData = ds[ds['location'] == 'United States']
     indiaData = ds[ds['location'] == 'India']

     # Creating the scatter plot
     plt.figure(figsize=(10, 6))
     plt.scatter(ukData['total_vaccinations_per_hundred'], ukData['people_vaccinated_per_hundred'], color='blue', label='United Kingdom')
     plt.scatter(usData['total_vaccinations_per_hundred'], usData['people_vaccinated_per_hundred'], color='red', label='United States')
     plt.scatter(indiaData['total_vaccinations_per_hundred'], indiaData['people_vaccinated_per_hundred'], color='green', label='India')
     # Adding labels and title
     plt.xlabel('Vaccinations per Hundred')
     plt.ylabel('People Vaccinated per Hundred')
     plt.title('Relationship between Vaccinations and People Vaccinated per Hundred in the UK,USA and INDIA')
     plt.legend()
     # Showing the plot
     plt.grid(True)
     plt.tight_layout()
     plt.show()
     pass

def visualization12():
    # Pivoting the data
    
    pivotData = continentData.pivot(index='date', columns='location', values='daily_vaccinations')
    pivotData.index = pivotData.index.date

    # Ploting the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivotData, cmap='viridis')
    plt.title('Daily Vaccinations Over Time in Continents')
    plt.xlabel('Continent')
    plt.ylabel('Date')
    plt.show() 
     
    pass

# This is main function, It gives user options to choose visualization options to view
def main():
    while True:
        print("Choose a visualization option:\n")
        print("1.  Line plot: Total Number of Vaccinations Over Time.\n")
        print("2.  Pie Chart: Percentage of Vaccinated People in the Continents\n")
        print("3.  Line plot: Total Vaccination vs Total Booster Shots Over Time\n")
        print("4.  Line plot: People Vaccinated Vs People Fully Vaccinated Over Time\n")
        print("5.  Stacked Bar Chart: Total Vaccination Vs People Vaccinated per Continent\n")
        print("6.  Line Plot: Comparison of Vaccines Rates per Hundred in USA and Pakistan\n")
        print("7.  Horizental Bar Chart: Top Ten Most VAccinated Countries in Europe\n")
        print("8.  Grouped Bar Chart: People VAccinated VS People Fully Vaccinated By Income\n")
        print("9.  Bar chart: Comparison of Vaccine Attributes (People vaccinated, People Fully Vaccinated, Total Boosters)\n")
        print("10. Time series: Numbe rof fully vaccinated People over time\n")
        print("11. Scatter Plot: Relationship between Vaccinations and People Vaccinated per Hundred in UK, USA, INDIA\n")
        print("12. Heatmap (Daily Vaccination in Continents Overtime)\n")

        print("13. Quit")

        choice = input("Enter your choice (1-13): ")

        if choice == '13':
            print("Exiting the program.")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            choice = int(choice)
            if choice == 1:
                visualization1()
            elif choice == 2:
                visualization2()
            elif choice == 3:
                visualization3()
            elif choice == 4:
                visualization4()
            elif choice == 5:   
                visualization5()
            elif choice == 6:
                visualization6()
            elif choice == 7:
                visualization7()
            elif choice == 8:
                visualization8()
            elif choice == 9:
                visualization9()
            elif choice == 10:
                visualization10()
            elif choice == 11:
                visualization11()
            elif choice == 12:  
                visualization12()                          
        else:
            print("Invalid input. Please enter a number between 1 and 13.")

if __name__ == "__main__":
    main()
