import random
feet_in_mile = 5280
meters_in_kilometer = 1000
nba_player =  ["Kevin Durant", "Pascal Siakam", "Kyrie Irving", "Stephen Curry", "LeBron James"]

def get_files_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)