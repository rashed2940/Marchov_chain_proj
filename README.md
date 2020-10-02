# Marchov_chain_proj


## Our team:
We are an international team of passionate data scientist, online participants, at Spiced Academy. We call ourselves team **rebels of Munich**, Germany. [Rashed](https://github.com/rashed2940), and [Diana](https://github.com/dian-ai)

## Goal:
By participating in this project, we hope to challenge ourselves and our learnings to provide a monte carlo marchov chain simulation of a supermarket.
Our aim is to provide an insights regarding the questions of how many people for how long can be in the supermarket at the same time wandering around different aisles. We plan to do EDA analysis on our dataset to gain knowledge about the business questions. Then with Object Oriented Programming and with the help of OpenCV library we tried to simulate the movement of customers inside the supermarket. 

## [Dataset description](http://krspiced.pythonanywhere.com/chapters/project_markov/data_analysis.html#explore-supermarket-data):
Our dataset is imaginary dataset of all DOODLE customers in 5 days of the week. It has information about time that  customer is present at each section of supermarket, date, sections that customer visits while shopping, and imaginary price of each product.

## Our answeres to business questions:
* Calculate the total number of customers in each section

<p align="center">
  <img src="/images/cust_at_sec.png"   title = "total customers in 5 days">
</p>


* Calculate the total number of customers in each section over time

<p align="center">
  <img src="/images/cust_time_sec.png"  title = "Customer over time at different locations">
  <img src="/images/cust_sub_days.png"  title = "Customers over time, per ech day">
</p>



* Calculate the total number of customers in the supermarket over time

<p align="center">
  <img src="/images/total_cust_times.png"  title = "Total customers over time in supermarket">
</p>


* Our business managers think that the first section customers visit follows a different pattern than the following ones.

 - fisrt visiting section distributions
<p align="center">
  <img src="/images/first_dist.png"  title = "distribution of first visiting sections">
</p>

- following visiting sections distributions

<p align="center">
<img src="/images/follow_dist.png"  title = "Cdistribution of following visiting sections">
</p>


* Estimate the total revenue for each product:
<p align="center">
<img src="/images/revenue.png"  title = "total revenue of each section">
</p>



* Calculate the time each customer spent in the market (part of table)

|  index| customer| day  | time_spent  | 
|---|---|---|---|
| 1 | 1000  |  friday |   00:01:00 | 
| 2 | 9 | monday  | 00:07:00  |  
| 3  | 102  |  thursday | 00:02:00|  





