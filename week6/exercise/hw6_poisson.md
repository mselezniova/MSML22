# Week 6 (E): Poisson regression 

The goal of this task is to implement Poission regression and apply it to [Seoul Bike Sharing Demand Data Set](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand). The dataset contains the number of rented bikes per day, together with parameters describing the day (weather, season, day of week, etc.). You need to predict the count of rented bikes based on all the other data columns. Below are the steps to complete the task:

- Load the data (already done in the provided Jupyter Notebook).
- The dataset contains **categorical variables**, which take only a limited number of non-ordered values (e.g. columns ```Seasons``` or ```Holiday```). These variables cannot be treated as numerical variables, since their value is not meaningful. Thus, it is important to transform categorical variables to meaningful numerical variables during data preprocessing. In this task, we use **one-hot-encoding** for this purpose, which creates a separate data column with values 0 and 1, corresponding to each possible value of the categorical variable. E.g. the column ```Seasons``` is transformed into 4 columns (```Seasons_Autumn, Seasons_Spring, Seasons_Summer	, Seasons_Winter```), only one of which contains value 1 in each data row. This preprocessing step is already done in the provided Jupyter Notebook using the following line:
```pd.get_dummies(df, columns=['Hour','Seasons','Holiday','Functioning Day'])```
- Carry out **min-max normalization** of the data columns to avoid numerical problems.
- Implement a **Poission regression** model as a child class of the ```LinearRegression``` class. The output function of this model is given by: $$h(x) = e^{\langle w, x\rangle + b},$$ i.e. Poisson regression uses **exponential activation function** $\alpha(t)=e^t$. And the loss function is given by the so-called **Poisson loss**: $$\mathcal{R}(y,\hat{y})=\hat y- y \log \hat y,$$ where $y$ is the true answer and $\hat{y}$ is the model's prediction.
- Train the Poission regression model on the data. Plot the learning curve. 
- Add ```mean_abs_error``` method to ```LinearRegression``` class. The method should compute mean absolute deviation of the model's predictions from the true answers: $$E(X,Y) = \dfrac{1}{n} \sum_{i=1}^n |h(x_i)-y_i| $$
- Compute mean absolute error of your trained Poisson regression model on train and test.
- Train a linear regression model on the same data. Compute train and test mean absolute error. How does the performance compare to the Poisson regression model?
