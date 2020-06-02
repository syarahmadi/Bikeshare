 #------This project is thrid project of Udacity course-----------

 
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
      print('Hello! Let\'s explore some US bikeshare data!')
      print('Would you like to see data for Chicago, New York, or Washington?')
      city=input().lower()
      while city not in ['chicago','new york city','washington']:
        print('Entered city is invalid, try again')
        city=input().lower()
      print('Awesome, you chose {}'.format(city))
      df = pd.read_csv(CITY_DATA[city])
      print('Would you like to filter the data by month, day, both or not at all?\n (Please enter month, day, both or none)')
      word=input().lower()
      while word not in ['month', 'day', 'both','none']:
        print('Please enter month, day, both or none')
        word=input().lower()
      if word in ['month', 'both']:
        print('Which month - January, February, March, April, May, or June?')
        month=input().lower()
        while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
          print('please enter January, February, March, April, May, or June')
          month=input().lower()
      else:
        month='all'
      if word in ['day', 'both']:
        print('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n please give it as integer, Sunday=1')
        #print('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
        day=int(input())
        while day not in [1,2,3,4,5,6,7]:
        #while day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
          #print('please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.')
          print('please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.\n please give it as integer, Sunday=1')
          day=int(input())
      else:
        day='all'
      return city, month, day

      #---------------------------------

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
    # load data file into a dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    if month!= 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df
    #------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Month'] = df['Start Time'].dt.month
    popular_month = df['Month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    df['Day'] = df['Start Time'].dt.weekday
    popular_day = df['Day'].mode()[0]
    print('Most Popular day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#----------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most commonly used start station', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most commonly used end station', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["start_end"] = df['Start Station'].astype(str) + ' to ' + df['End Station']

    popular_start_and_end_station = df["start_end"].mode()

    print('Most commonly used start and end station', popular_start_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    travel_time = df["Trip Duration"].sum()
    print('Total travel time', travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print('Mean travel time', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
#----------------------------------------------
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('Counts of user types:',df['User Type'].value_counts())

    try:
      gender_types = df['Gender'].value_counts()
      print('Counts of gender:', gender_types)
    except:
      print('Gender information is not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      print('earliest year birth year is:', df["Birth Year"].min())
      print('most recent of brith year  is', df["Birth Year"].max())
      print('most common year of brith year is',df["Birth Year"].value_counts().idxmax())
    except:
      print('Brith year information is not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data= input('\nWould you see 5 raws of data? Enter yes or no.\n')
        start=0
        end=5
        while raw_data.lower()=='yes':
          print(df.iloc[start:end])
          start+=5
          end+=5
          raw_data= input('\nWould you see 5 more raws of data? Enter yes or no.\n')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
#-----------------------------------------------
if __name__ == "__main__":
	main()
