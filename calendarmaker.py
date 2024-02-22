import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

print('Calendar Maker')

# Loop to get a year from the user.
while True:
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a number for the year, like 2022.')
    continue

# Loop to get a month from the user.
while True:
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if response.isdecimal():
        month = int(response)
        if 1 <= month <= 12:
            break

    print('Please enter a number from 1 to 12.')

# Function to create the calendar for the specified year and month.
def get_calendar_for(year, month):
    calendar_text = ''  # This will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calendar_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    calendar_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separates weeks:
    week_separator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blank_row = ('|          ' * 7) + '|\n'

    # Get the first date in the month.
    current_date = datetime.date(year, month, 1)

    # Roll back current_date until it is Sunday.
    while current_date.weekday() != 6:  # Sunday is represented as 6, not 0.
        current_date -= datetime.timedelta(days=1)

    # Loop over each week in the month.
    while True:
        calendar_text += week_separator

        # day_number_row is the row with the day number labels:
        day_number_row = ''
        for _ in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)  # Go to the next day.
        day_number_row += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calendar_text += day_number_row
        for _ in range(3):  # Add three blank rows.
            calendar_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calendar_text += week_separator
    return calendar_text

# Get the calendar text for the specified year and month.
calendar_text = get_calendar_for(year, month)

# Display the calendar.
print(calendar_text)

# Save the calendar to a text file:
calendar_filename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendar_filename, 'w') as file_obj:
    file_obj.write(calendar_text)

print('Saved to ' + calendar_filename)
