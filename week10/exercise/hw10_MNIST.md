# Week 10 (E): MNIST

The [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset consists of 28x28 pixel images of handwritten digits. This dataset is considered "easy" for modern machine learning algorithms and is commonly used as the first test for image recognition algorithms, including neural networks. The goal of this task is to apply our multilayer perceptron (MLP) model to MNIST. You need to complete the following steps:

- Load the MNIST dataset (this part is already done in the provided Jupyter Notebook; instead of loading [the original dataset](http://yann.lecun.com/exdb/mnist/), which needs a bit of work to parse and convert to numpy arrays, we load a ready preproccessed version using ```sklearn```).
- Split the dataset into train and test (implement a train-test split function for numpy arrays instead of the function we used for pandas dataframes in previous classes).
- Modify method ```train``` of the ```MLP``` class, implemented in the exercise class, so that it performs **mini-batch SGD** training instead of full-batch GD.
- In addition to the ReLU activation function and L2 loss, implemented in the exercise class, implement **sigmoid** (logistic) activation and **cross-entropy loss**.
- Train several MLP models with different choices of **architecture** (number and width of hidden layers) **activation functions**, **loss** and **batch size**. Observe the training behaviour and test performance (accuracy) of your models. Which networks work better? What is the effect of the choice of activation and loss? How does the batch size affect the training speed and the final performance? 
- Even with very simple neural networks, it is possible to reach accuracy of **94-95%** on MNIST. Include at least one model that reaches this performance level in your submission.
- Display some examples of images misclassified by your best network. Count the number of misclassification for each class separately. Which digits are misclassified most often?




---
© [Mariia Seleznova](https://www.ai.math.uni-muenchen.de/members/phd_students/seleznova/index.html) 2022

https://github.com/mselezniova/MSML22

Distributed under the [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/)

