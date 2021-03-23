
import random
import plotly.figure_factory as ff
import plotly.express as ps
import csv
import pandas as spb
import statistics

df = spb.read_csv("medium_data.csv")
data = (df["reading_time"].tolist())


def random_data(datapoint):
    dataset = []
    for i in range(0, datapoint):
        random_number = random.randint(0, (len(data)-1))
        value = data[random_number]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return (mean)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("Population Mean:- ", population_mean)

def showMean():
    mean_list = []
    for i in range(0, 1000):
        a = random_data(100)
        mean_list.append(a)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )
showMean()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        a= random_data(100)
        mean_list.append(a)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()