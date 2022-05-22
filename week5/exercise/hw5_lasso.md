# Week 5 (E): Lasso

In this task you will need to implement **Lasso** regression and study its behavior on the [**Boston housing** dataset](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html). 

- Load the Boston housing dataset from the following link: https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv
The task is to predict MEDV variable (median house price) using all the other variables in the dataset. You can see the description of the variables [here](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html).
- Implement a LinearRegression class. It should behave the same as LinearBinaryClassification class but return the value of $\langle w, x \rangle + b$ instead of 1 or -1 through method h(). The training method should be GD. 
- Implement LassoRegression class. You can assume that $\partial_w |w| = sign(w)$ everywhere.
- Train your Lasso regression with a variety of values of hyperparameter $\lambda$, e.g. [1e-5,1e-4,1e-3,1e-2,2e-2,5e-2,1e-1,0.2,0.5,1.,2,5,10].
- Plot the behaviour of the final train MSE, test MSE and the coefficients norm as a function of $\lambda$ (as we did for Ridge in the exercise class). Observe what values of $\lambda$ allow to decrease the norm of $w$ without significantly worsening the regression performance.
- Plot the behaviour of each coefficient in $w$ as a function of $\lambda$ to see which coefficients are zeroed out as we increase the regularization hyperparameter. You graph can look as follows: 

![coefs](https://raw.githubusercontent.com/mselezniova/MSML22/main/week5/exercise/coefs.png)

Here the legend, which should show which variable corresponds to each line, is hidden. You should show the legend in your notebook.
- Find the last few (e.g. 4-6) variables that do not zero out as the regularization hyperparameter increases. Write what these variables mean in your notebook. 
- What $\lambda$ value is needed to obtain a model with only these variables not zeroed? Train such a model and plot/print coefficients corresponding to your "active" variables. Which variables affect the housing price positively and which affect it negatively? You can visualize the coefficients as follows:

![coefs](https://raw.githubusercontent.com/mselezniova/MSML22/main/week5/exercise/coef_vals.png)

Here the x ticks labels, which should show the names of the variables in the x axis, are hidden. Show them in your notebook.
