import fnmatch
import os

# open new file which will contain text of all scripts
exercises = open("exercises.txt", "w")

# get number of exercise scripts
directory = "/home/jack/Documents/code/python/practice/learnpython/"
number_of_exs =  len(fnmatch.filter(os.listdir(directory), 'ex*.py'))

# for every exercise, print text of exercise to txt file
for i in range(1, number_of_exs + 1):
    # get exercise text
    file_name = "ex" + str(i) + ".py"
    ex = open(file_name, "r")
    lines = ex.readlines()

    # write text to txt file
    exercises.write("--------------\n")
    exercises.write(file_name + "\n\n")
    for line in lines:
        exercises.write(line)
