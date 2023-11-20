# Week 2 (E): Covid-19 time series data

The goal of this task is to visualize the [Covid-19 data provided by WHO](https://covid19.who.int/data).  You need to:

* Download the dataset of daily confirmed Covid-19 cases and deaths reported to WHO (this part is already done in the provided Jupyter Notebook).
* Produce a bar plot of **daily new cases** over the whole time period covered in the dataset for **two countries of your choice**. 
* Since daily reported cases fluctuate strongly and depend on the day of the week, you should also plot a line with a rolling average over 7 days on top of the bar plot. 
* Produce a similar bar plot with the rolling average line for **daily reported deaths**.
* Produce a bar plot with **cumulative confirmed cases** of Covid-19 over the whole time period. You can also add a rolling average here.
 * Produce a similar plot with **cumulative confirmed deaths** of Covid-19 over the whole time period. 

To see the relationship between the curves of confirmed cases and deaths, you can plot the two graphs in the same figure. In this case, you can add a new Y-axis by ```ax.twinx()``` command to have two different value ranges of the Y-axis in the same figure. You may need this because the number of reported deaths is normally much smaller than the number of reported cases.

Alternatively, you can plot the two curves in two different subplots, one under another, using subplots.

Summing up, you should choose two countries present in the dataset and produce two figures for each country: one with daily cases and deaths, another one with cumulative cases and deaths. You need to submit a Jupyter Notebook, in which you generate your graphs, as a solution.

Below you can see the examples of the two figures. Of course, your graphs can look different as long as they provide the same information.

![](https://raw.githubusercontent.com/mselezniova/MSML22/media/week2/images/fig1.svg)
![](https://raw.githubusercontent.com/mselezniova/MSML22/media/week2/images/fig2.svg)