#this is a file make just as a example
import random
feet_in_mile = 5280
meter_in_kilometer = 1000
beatles = ["John","Paul","George"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)