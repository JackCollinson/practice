'''
When squirrels get together for a party, they like to have cigars. A squirrel
party is successful when the number of cigars is between 40 and 60, inclusive.
Unless it is the weekend, in which case there is no upper bound on the number of
cigars. Return True if the party with the given values is successful, or False
otherwise.
'''

def cigar_party(cigars, is_weekend):
    if cigars < 40: return False
    if not is_weekend and cigars > 60: return False
    return True

'''
You and your date are trying to get a table at a restaurant. The parameter "you"
is the stylishness of your clothes, in the range 0..10, and "date" is the
stylishness of your date's clothes. The result getting the table is encoded as
an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or
more, then the result is 2 (yes). With the exception that if either of you has
style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe)
'''

def date_fashion(you, date):
    if date you < 3 or date < 3: return 0
    if you > 7 or date > 7: return 2
    return 1

'''
The squirrels in Palo Alto spend most of the day playing. In particular, they
play if the temperature is between 60 and 90 (inclusive). Unless it is summer,
then the upper limit is 100 instead of 90. Given an int temperature and a
boolean is_summer, return True if the squirrels play and False otherwise.
'''

def squirrel_play(temp, is_summer):
    lower = 60
    upper = 90
    if is_summer: upper = 100
    return lower <= temp <= upper

'''
You are driving a little too fast, and a police officer stops you. Write code to
compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big
ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80
inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it
is your birthday -- on that day, your speed can be 5 higher in all cases.
'''

def caught_speeding(speed, is_birthday):
    cushion = 0
    if is_birthday: cushion = 5

    if speed <= 60 + cushion: return 0
    if speed <= 80 + cushion: return 1
    return 2

'''
Given 2 ints, a and b, return their sum. However, sums in the range 10..19
inclusive, are forbidden, so in that case just return 20.
'''

def sorta_sum(a, b):
    sum = a + b
    if 10 <= sum <= 19:
        sum = 20
    return sum

'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
indicating if we are on vacation, return a string of the form "7:00" indicating
when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
the weekend it should be "10:00". Unless we are on vacation -- then on weekdays
it should be "10:00" and weekends it should be "off".
'''

def alarm_clock(day, vacation):
    if vacation:
        if 1 <= day <= 5:
            return "10:00"
        else:
            return "off"
    else:
        if 1 <= day <= 5:
            return "7:00"
        else:
            return "10:00"
