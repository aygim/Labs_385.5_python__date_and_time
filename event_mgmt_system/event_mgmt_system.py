# Imports
from datetime import datetime, date

#Allocarion of memory for temporary db
events = {}

def add_event():
    event_name = input('Enter the event name:')
    date_input = input('Enter the event date (YYYY-MM-DD):')

    #Error handing block
    try:
        # Convert string into a datetime object with '.strptime()'
        # used .date() to remove the timestamp but keep the date
        event_date = datetime.strptime(date_input,'%Y-%m-%d').date()
        print(event_date)
    except ValueError:
        print('Invalid date format. Please use YYY-MM-DD')
        return #this return will exit the function

    events[event_name] = event_date

    print(f'🎉Success.Added {event_name} to events!')


# Helper function to use as key function for sorting
def get_event_date(tup):
    # return the date from the (eventname, evenDate)
    return tup[1]




def list_events():
    if len(events) == 0:
        print('No upcoming events')
        return #return will exit this function
    
    print('\n🌟🌟Upcoming Events!')

    #sort events by date
    #items() method makes a dictionary into a list of tuples
    sorted_events = sorted(events.items(),key=get_event_date)

    # Loop over our sorted_events list, prints name and date of event
    for e_name, e_date in sorted_events:
        today = date.today()
        days_remaining = (e_date - today).days

        print(f'{e_name} - {e_date} - {days_remaining} days until event!')

# Create a delete function
# check if event exists in object
# if exist del
# let user know it has been deleted

def delete_event():
    event_to_delete = input('Enter name of event to delete: ')

    # print(event_to_delete in events)

    # Use the 'in' keyword to check if key is in dictionary
    if event_to_delete in events:
        del events[event_to_delete]
        print(f'✅ Successfully Deleted {event_to_delete}')
        return
    else:
        print('Event not in database, check spelling')



def main():
    while True:
        print('\nEvent Management System')
        print('1. Add Event')
        print('2. List Events')
        print('3. Delete Event')
        print('4. Quit')

        choice = input('Enter your choice: ')
    
        if choice == '1':
            add_event()
        elif choice == '2':
            list_events()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            print('Program has been closed. Goodbye')
            break
        else:
            print('Invalid Option. Try again.')


        # Calculate the number of dates, from todays until the event
    

#This makes sure if imported function doesnt 
# automatically run on import
if __name__ == "__main__":
    main()
    