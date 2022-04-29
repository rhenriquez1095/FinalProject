import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data from a big city!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nSelect one of the cities below:")
        print("\n Chicago, New York City, Washington")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\n Oops!!it seems you enter a diferent city from: Chicago, New York City, Washington ")

        print(f"\nYou selected the city: {city.title()} ")

    # TO DO: get user input for month (all, january, february, ... , june)
    selected_month = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in selected_month.keys():
        print("\nSelect a month between January to June. If you want to see all six month information please select all")
        month = input().lower()

        if month not in selected_month.keys():
            print("\n Oops! Invalid input. Please try again a correct month allowed.")

    print(f"\nYou have chosen {month.title()} as your month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_selected = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    day = ''
    while day not in day_selected:
      print("\nPlease enter the day of the week that you're interest in. If you want all seven days informaction select all")
      day = input().lower()

      if day not in day_selected :
        print("\nOpps! please enter a valid day of the week")

      print (f"\nYou have selected: {day.title()} ")


    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print(f"The most common month: {common_month}")

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print(f"The most common day: {common_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print(f"\nMost Popular common Hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(f"The most common station to start is: {common_start}")

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(f"The most common station to end is: {common_end}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    trip = df['Start To End'].mode()[0]
    print(f"\nThe most frequent trips are from {trip}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration = df['Trip Duration'].sum()
    duration_hr = duration/3600
    print(f"\nThe total travel time is: {duration_hr} hours.")

    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print(f"\nThe average trip takes {avg_duration} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"There type or users are: {user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"The genders are: {gender}")
    except:
        print(f"Theres is not Gender information for this city")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])

        print(f"\nThe earliest year of birth is {earliest}. The most recent year of birth is {recent} and the most common year of           birth is {common_year}")
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # Display 5 raw data
def display_data(df):
    answer = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in answer:
        print("\nDo you wish to view the raw data? (yes/no)")
        rdata = input().lower()


        if rdata == "yes":
            print(df.head())
        elif rdata not in answer:
            print("\nSelect a correct answer")

    #Continue viewing data
    while rdata == 'yes':
        print("Do you want to see more raw data?")
        counter += 5
        rdata = input().lower()
        #displays 5 more rows
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
