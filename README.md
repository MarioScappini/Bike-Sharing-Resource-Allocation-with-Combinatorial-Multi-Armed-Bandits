# Bike Sharing Resource Allocation with Combinatorial Multi-Armed Bandits

---

Across the globe many cities are following the trend of implementing a form of bike sharing system. Taipei, Taiwan and Asuncion, Paraguay are no different. Each city had executed different systems of a bike sharing system with different degrees of success, while the first succeed in developing a solution to improve the mobility of the citizens across the city, the second miserably failed. In this project proposal we would explore the role of bike sharing resource allocation and the successfulness of a bike sharing system. In addition, we would implement a bike allocation model using a combinatorial multi-armed bandits algorithms and the open data of UBike system in Taipei, to demonstrate how resource allocation systems can greatly benefit the successfulness of such kind of systems.

### Problem Formulation

For implementing a resource allocation system for a bike sharing system we need to consider the following. 

When we allocate a number of bikes to a certain station we need to perform this action every t period of time. In addition, we need to consider that we have a limited amount of available bikes to allocate in the while system. Each station has an unknown distribution. Finally we need to consider incoming bicycles, such as users have space to park their bicycles they rented from other stations. Our goal is to accumulate the largest amount of rides over a t period of time.

### Resources

- We would be using the model presented in the paper "Combinatorial Multi-armed Bandits for Resource Allocation" [https://arxiv.org/pdf/2105.04373.pdf](https://arxiv.org/pdf/2105.04373.pdf)
- In addition to the UBike Taipei dataset [https://data.gov.tw/dataset/137993](https://data.gov.tw/dataset/137993)


### Objectives

- Collect and process from the UBike Taipei API over a period of a month, with an 20 minutes interval between each entry
- Implement the model presented in the paper "Combinatorial Multi-armed Bandits for Resource allocation"
- Feed the model with the collected data.
- Evaluate the impact of such model would imply in a bike sharing system

---
