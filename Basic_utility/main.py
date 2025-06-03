from unit_conventer import unitconverter
from matrix import matrix
from date_time import dob
from guess_the_number import guess_number
from ceaser_cipher import cipher
from sci_cal import scicalculator
def unit_conv():
    uc=unitconverter()
    print("\n--Unit converter--")
    print("1. Temperature")
    print("2. Weight")
    print("3. Length")
    choice=input("Choose conversion type:")