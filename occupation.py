import random
csv = open("occupations.csv","r")
list_of_lines = csv.readlines()

del list_of_lines[0]

# print(list_of_lines)

jobs = {}

for line in list_of_lines:
    # print(line)
    if line[0] == '"':
        delimited = line.split('",')
        
        #print(delimited)
        
        delimited[0] = delimited[0][1::]
        
        percent = delimited[len(delimited)-1]
        del delimited[len(delimited)-1]
        
        jobs[''.join(delimited)] = float(percent)
    else:
        delimited = line.split(",")
        jobs[delimited[0]] = float(delimited[1].strip())
        
jobs.pop("Total")
for job, percentage in jobs.items():
    print(job + " " + str(percentage))

def percent_chance(dict):
    while True:
      for key, value in dict.items():
          random_chance = random.random() * 99.8
          if random_chance <= value:
              return key

i=0
while i < 5:
    print("RGO: " + percent_chance((jobs)))
    i+=1
