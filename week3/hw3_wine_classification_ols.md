# Week 3 (E): Wine classification

The goal of this task is to classify wine based on the chemical analysis data using **ordinary least squares (OLS)** method. To complete the task, you need to do the following:

- Load the [**wine dataset**](https://archive.ics.uci.edu/ml/datasets/Wine) from the UCI Machine Learning Repository. You can find the description of the dataset under the link. If you load the dataset as a Pandas DataFrame, you can use the following line to specify the column names:
``column_names = ['Class','Alcohol', 'Malic acid','Ash', 'Alcalinity of ash', 'Magnesium',
               'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 
                'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']``
                
- The dataset contains three classes of wine. In this task, we want to work with **binary classification**. Therefore, you should to **discard class "3" from your data and only work with classes "1" and "2"**.
- Shuffle the data and separate it into train and test subsets. The train set should constitute 80% of the data.
- Choose a reasonable **two-dimensional projection** of the data (e.g. columns "Alcohol" and "Proline") and plot the data. The difference between the two classes should be visible in your projection. You should plot test and train data using different markers. 
- Implement a OLS classifier **with intercept** (e.g. the bias $b$ value may be non-zero) and run it on your two-dimensional train data. To do so, implement a method called ```OLS()``` in the ```LinearBinaryClassification``` class defined in the exercise class.  The method has to change the parameters of the class to the OLS solution.
- Plot the **decision regions** of the classifier as in the exercise class.
- Count the number of errors that  your classifier makes on train and test.
- Train an OLS classifier on **all the 13 variables** of the wine dataset and count the number of errors. Is the dataset linearly separable? Answer this question explicitly in your notebook. 

Submit your solution as a Jupyter Notebook.