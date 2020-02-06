import random
import decimal
import string
line1="Are maybe you finished with school already?"
line2="Hi Mary maybe. I'm filling out a job application."
line1=line1.lower()
line2=line2.lower()
for x in line1:
    if x in string.punctuation:
        line1=line1.replace(x,"")

for x in line2:
    if x in string.punctuation:
        line2=line2.replace(x,"")

probabilityOfMarkersGeneral={}
probabilityOfMarkersLocal={}
inF= open("MarksAndExamples")
for line in inF:
    probabilityOfMarkersGeneral[tuple(line[line.index(" "):-1].split())]=float(decimal.Decimal(random.randrange(0, 5000)))/100000
    probabilityOfMarkersLocal[tuple(line[line.index(" "):-1].split())]=0
for word1 in line1.split(" "):
    if(word1 in line2.split(" ")):
       for tup in probabilityOfMarkersLocal.keys():
            if( word1 in tup):
                probabilityOfMarkersLocal[tup]+=1
                break
print(probabilityOfMarkersGeneral)
for tup in probabilityOfMarkersLocal:
    probabilityOfMarkersLocal[tup]=probabilityOfMarkersLocal[tup]/len(line2.split(" "))


aggregatePossibility={}

for tup in probabilityOfMarkersLocal:
    aggregatePossibility[tup]=probabilityOfMarkersLocal[tup]-probabilityOfMarkersGeneral[tup]

print(sum(aggregatePossibility.values()))
