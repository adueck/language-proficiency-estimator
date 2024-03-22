import os
import csv

# row numbers for data of interest in BEST.csv
AGE = 1
EDUCATION = 3
PERCENT = 7
INTERVIEW = 13
START = 16
PICTURE_TEST = 19
LEXTALE = 22

x_data = []
y_data = []

# creates an average percentage score to be used as our proficiency level
def get_proficiency(interview, picture_test, lextale):
  avg = ((interview * 20) + (picture_test * (100/65)) + lextale) / 3
  return avg

def get_education(education):
  if education == "High School":
    return 0
  if education == "Professional Training":
    return 1
  if education == "University":
    return 2
  if education == "Postgraduate":
    return 3

# read csv dataset and assemble x and y data for model 
with open(os.path.join('data', 'BEST.csv')) as f:
  reader = csv.reader(f)
  i = 0
  for (i, row) in enumerate(reader):
    if (i > 0):
      x_data.append([int(row[AGE]), get_education(row[EDUCATION]), float(row[PERCENT])])
      proficiency = get_proficiency(int(row[INTERVIEW]), int(row[PICTURE_TEST]), float(row[LEXTALE]))
      y_data.append([proficiency])