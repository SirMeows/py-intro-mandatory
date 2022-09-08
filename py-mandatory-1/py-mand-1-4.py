# Date Decoder.
# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
# Create a dict suitable for decoding month names to numbers.
# Create a function which uses string operations to split the date into 3 items using the "-" character.
# Translate the month, correct the year to include all of the digits.
# The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

date = '8-MAR-85'

months = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

def month_decoder(date):

    splitted = date.split('-')


    # handle day

    day_str = splitted[0]

    splitted[0] = int(day_str)


    # handle month

    month_input = splitted[1]

    if (len(month_input)) == 3:
        splitted[1] = months.get(month_input)


    # handle year

    year_input = splitted[2]

    divider_year = 70

    if len(year_input) == 2:

        two_digit_year = int(year_input)
        
        if divider_year < two_digit_year:
            splitted[2] = 1900 + two_digit_year

        else:
            splitted[2] = '20' + str(two_digit_year)
            

    return splitted

print(month_decoder(date))