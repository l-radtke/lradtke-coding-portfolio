# import the packages we need to create our CMD
import numpy as np
import matplotlib.pyplot as plt

# defines CMD function
def CMD(loc):
    
    # read data using pandas
    df = pd.read_csv("oh_table.csv")
    
    # defining distance, G, and J using the group id
    distance = df["distance"].loc[df["group_id"] == loc]
    G = df["G"].loc[df["group_id"] == loc]
    J = df["J"].loc[df["group_id"] == loc]
    
    # define the absolute magnitude using formula
    abs_mag = G - 5 * np.log10(distance) + 5
    
    # define cm as the color map
    cm = plt.cm.get_cmap("seismic")
    
    # create a scatter plot using G-J as the x values and the absolute 
    # magnitude as the y values
    plt.scatter(G-J,abs_mag, c=abs_mag, s=35, cmap=cm)
    
    # create another scatter plot adding the sun
    plt.scatter(5.12-3.64,5.12, c='lime', s=200, marker='*')
    
    # add a title and labels to our axes
    plt.title("Color Magnitude Diagram- Coma Bere Star Cluster")
    plt.xlabel("Color(G-J)")
    plt.ylabel("Absolute Magnitude(G)")
    
    # invert the y axis
    plt.gca().invert_yaxis()
    
    # save our graph to our computer
    plt.savefig("CMD.png")

# call our function
CMD(8)