import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv

df=pd.read_csv("sample_2.csv")
reading_time = df["reading_time"].tolist()
fig = ff.create_distplot([reading_time],["reading_time"], show_hist=False)
fig.show()

mean = statistics.mean(reading_time)
print("The mean of the reading time is: ", mean)

def random_set_of_means(counter):
    dataset= []
    for i in range(0,counter):
        random_index= random.randint(0, len(reading_time))
        value= reading_time[random_index]
        dataset.append(value)
    mean= statistics.mean(dataset)
    return mean

meanList= []
def setup():
    for i in range(0,1000):
        set = random_set_of_means(100)
        meanList.append(set)

setup()
random_set_of_means()

fig = ff.create_distplot([meanList],["Reading Time"], show_hist=False)
fig.show()

mean_2 = statistics.mean(meanList)
std_dev = statistics.stdev(meanList)

print("The mean of the sampling distribution score is: ", mean_2, "And the standard deviation is", std_dev)

