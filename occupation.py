csv = open("occupations.csv","r")
list_of_lines = csv.readlines()

del list_of_lines[0]

# print(list_of_lines)

jobs = {}

for line in list_of_lines:
    # print(line)
    if line[0] == '"':
        delimited = line.split('",')
        
        print(delimited)
        
        delimited[0] = delimited[0][1::]
        
        percent = delimited[len(delimited)-1]
        del delimited[len(delimited)-1]
        
        jobs[''.join(delimited)] = float(percent)
    else:
        delimited = line.split(",")
        jobs[delimited[0]] = float(delimited[1].strip())
        
        
print()
for job, percentage in jobs.items():
    print(job + " " + str(percentage))