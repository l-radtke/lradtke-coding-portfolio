# import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# read in data
df = pd.read_csv("25_Pc_Full_Query-result.csv")

]:
# make lists for G, J, and distance to use in making the CMD
G = df["phot_g_mean_mag"]
J = df["j_m"]
distance = 1 / (df["parallax"]/ 1000)


# define the absolute magnitude using the formula(list)
abs_mag = G - 5 * np.log10(distance) + 5

# define cm as our color map
# cm = plt.cm.get_cmap("RdYlBu_r")

# create a scatter plot using G-J as the x values and the absolute magnitude as the y values
plt.scatter(G-J,abs_mag)

# add a title and labels to our axes
plt.title("Color Magnitude Diagram- Gaia Stars and Stuff")
plt.xlabel("Color(G-J)")
plt.ylabel("Absolute G")

# invert the y axis
plt.gca().invert_yaxis()

# plot
plt.show()
 
df.columns[-100:]

i = df["i_mag"]
print(max(G-i))
print(min(G-i))

# create a plot that shows the star distrubution divided in 47 "bins"
list1 = G - i
plt.hist(list1, bins = 47)
plt.title("Gaia star distribution")
plt.show()

# define the function that makes a histogram of star distribution
def histogram(fileName,name):
    
    # read in the file
    file = pd.read_csv(fileName)
    
    # define g and i
    g = file["g_mag"]
    i = file["i_mag"]
    
    # make and clean the list 
    list1 = g - i
    mask = np.isfinite(list1)
    cleaned_list = list1[mask]
    
    plt.figure(figsize = [8,5])
    
    # define the parameters of the histogram
    y, x, _ = plt.hist(cleaned_list, bins = np.arange(min(cleaned_list), 
            max(cleaned_list), 0.5), color = "#4aaf42")
    # add a line to represent the Sun
    plt.axvline(x=0.6, color = "black", linestyle = 'dashed')
    # add redder and bluer labels
    plt.text(max(x)- 0.6 * max(x), max(y) - 0.1 * max(y),
             "REDDER", color = "r", size = 20, **gsfont)
    plt.text(min(x)+ 0.2* max(x), max(y) - 0.1 * max(y),
             "BLUER", color = "b", size = 20, **gsfont)
    # add the labels and title
    plt.xlabel("g - i")
    plt.ylabel("nb of stars")
    plt.title("Gaia star distribution within {}".format(name))
    # save the histogram
    plt.savefig("hist_{}.png".format(name))
    
# run the function on the data at different distances
histogram("25_Pc_Query-result.csv","25_Pc")
histogram("50_Pc_Query-result.csv","50_Pc")
histogram("100_Pc_Query-result.csv","100_Pc")
histogram("200_Pc_Query-result.csv","200_Pc")
