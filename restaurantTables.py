# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

times = ['8am - 10am', '10:30am - 12:30pm','1pm - 3pm','3:30pm - 5:30pm', '6pm - 8pm','8:30pm - 10:30pm'] #6 time slots for each table and this is the correlating time
def assign_tables ():
    O = 'open'
    X = 'taken'
    tables = { 
        2: {
            "T1": [O,O,X,O,O,O], #Each table has 6 different time slots
            "T6": [O,O,O,X,O,X],
            "T3": [O,O,O,O,O,O]
    },
        4: {
            "T5": [O,O,O,O,X,X],
            "T2": [O,O,O,O,O,O]

    },#the tables with said number of seats
        6: [O,O,O,X,O,X]
    }# I really had trouble understanding how yall formulated the info in the dictionary so I made my own with the same info
    try:
        party_size = int(input('What is the size of your party?'))#the keys in the dictionary are integers so the input has to be too
        if party_size > 6:# I couldn't figure out how to combine tables so I reject parties that are too large
            print('Party size is too large for one table.')
            return None    #the party size is incompatible with any table we have so I return nothing
        if party_size in tables:# loops the party size through each key in the dictionary
                print(f'Availabe tables:\n{'\n'.join(tables[party_size])}')#learned '.join' from a python dictionary online
        # line 24 was the only line I needed outside resources for 
        else:
            print('Matching party size not found')
            return None #the party size is incompatible with any table we have so I return nothing
    except ValueError: 
        print('Enter only a number')
        return None
assign_tables()
#I ended up not being able to provide the user with info on time slots
