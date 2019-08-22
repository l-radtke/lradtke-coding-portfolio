#importing packages
import csv
import numpy as np
import matplotlib.pyplot as plt

#clears the screen
plt.clf()
        
#opens the file and creates a reader
csvFile = open("experimentDataMusicMath.csv")
csvReader = csv.reader(csvFile, delimiter = ",")

#creates two empty lists for the values
classical = []
deathMetal = []

#skips the first line
next(csvReader)

#gets the values from the files and puts them into the lists
for row in csvReader:
    classical.append(float(row[0]))
    deathMetal.append(float(row[1]))
 
#calculates the t value
t = (np.mean(classical)-np.mean(deathMetal))/(np.var(classical)/len(classical)+ np.var(deathMetal)/len(deathMetal))**0.5
print("t value = ",t)

#calculates the degrees of freedom
DoF = len(classical) + len(deathMetal) - 2
print("Degrees of freedom = ",DoF)

#imports more stuff
from scipy import stats

#defines a function that calculates the p value
def p_value(DoF, t):
    print("p value = ",stats.t.sf(np.abs(t), DoF)*2)

#calls the function
p_value(DoF, t)

#calculates the mean of each list using numpy
classicalAvg = np.mean(classical)
deathMetalAvg = np.mean(deathMetal)

#calculates the standard deviation of each list using numpy
classicalStdDev = np.std(classical)
deathMetalStdDev = np.std(deathMetal)

#defines two lists to hold our values
meanList = [classicalAvg,deathMetalAvg]
yerrs = [classicalStdDev,deathMetalStdDev]

#creates a variable that plots a bar graph
barList  = plt.bar([0,1], meanList, yerr = yerrs, capsize = 5)

#sets the colors
barList[0].set_color('r')
barList[1].set_color('b')

#psets title, label, and adds error bars
plt.title("Classical v. death metal math problems averages")
plt.ylabel("problems solved")
plt.xticks([0,1],["classical music","death metal"])

#displays the plot
plt.show()