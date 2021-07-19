#Importing numpy module needed to create arrays and matplotlib needed to plot graphs
import numpy as np
import matplotlib.pyplot as plt
g = []
t = ""
l = []
f = input("Please enter the name of dataset: ")

#Creating a function which allows us to read and process datasets.
def read(f):
    """
    This function opens, reads, and transforms a ".txt" file into a list of lists
    :param f: is a string, which value is entered by user
    t - a string, which contains numbers from a ".txt" file
    l - a list containing numbers from a string "t"
    g - a list of lists, produced from "l"
    :return: returns list of lists, containing integer numbers
    """
    d = open(f, "r")
    t = ""
    for line in d:
        t += line
    l = t.split("\n")
    for i in l:
        g.append(i.rsplit(","))
    for i in g:
        if i == ['']:
            g.remove(i)
    for j in g:
        for i in range(0,len(j)):
            j[i] = int(j[i])
    return g

#Creating a 2D array, containing integer values
y = np.array(read(f))

#Stating main variables
s = 4
m = y.shape[0]
n = y.shape[1]
n_iter = 100
centroids = np.array([]).reshape(n,0)

#Randomizing first centroids
for i in range(s):
    rand = np.random.randint(0,m-1)
    centroids=np.c_[centroids,y[rand]]

#Creating a dictionaty that will serve as a cluster
clusters = {}

#Calculating Eucledean distance from centroids to every dot from dataset and storing it,
#then finding the minimum distance and storing its index to C
euc_dis = np.array([]).reshape(m,0)
for k in range(s):
       tempDist=np.sum((y-centroids[:,k])**2,axis=1)
       euc_dis = np.c_[euc_dis,tempDist]
C=np.argmin(euc_dis,axis=1)+1

#Creating a temp dictionary, which will contain the regrouped data point based on C
dict = {}
for k in range(s):
    dict[k + 1] = np.array([]).reshape(2, 0)
for i in range(m):
    dict[C[i]] = np.c_[dict[C[i]], y[i]]
for k in range(s):
    dict[k + 1] = dict[k + 1].T
for k in range(s):
    centroids[:, k] = np.mean(dict[k + 1], axis=0)
for i in range(n_iter):
    euc_dis = np.array([]).reshape(m, 0)
    for k in range(s):
        tempDist = np.sum((y - centroids[:, k]) ** 2, axis=1)
        euc_dis = np.c_[euc_dis, tempDist]
    C = np.argmin(euc_dis, axis=1) + 1
    dict = {}
    for k in range(s):
        dict[k + 1] = np.array([]).reshape(2, 0)
    for i in range(m):
        dict[C[i]] = np.c_[dict[C[i]], y[i]]
    for k in range(s):
        dict[k + 1] = dict[k + 1].T
    for k in range(s):
        centroids[:, k] = np.mean(dict[k + 1], axis=0)
    clusters = dict

#Plotting and graphing
color=['red','blue','green','cyan','magenta']
labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
for k in range(s):
    plt.scatter(clusters[k+1][:,0],clusters[k+1][:,1],c=color[k],label=labels[k])
plt.scatter(centroids[0,:],centroids[1,:],s=10,c="black",label='Centroids')
plt.xlabel('Vitamin C levels')
plt.ylabel('GLA levels')
plt.legend()
plt.show()





