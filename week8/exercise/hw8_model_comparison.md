# Week 8 (E): Model Comparison

The goal of this task is to compare preformance of multiclass classification models covered in our classes so far on the [Letter Recognition Data Set](https://archive.ics.uci.edu/ml/datasets/Letter+Recognition), which we already used in the last homework. You need to:

- Implement **one-vs-rest SVM classification model** as described in the exercise class. 
- Load **multiclass models** implemented in previous exercise classes and homework assignments: one-vs-rest linear (least squares) classification, one-vs-rest logistic regression, softmax regression.
- Train all the models on the training subset of the data. Pay attention to the choice of hyperparameters for every model. 
- Compare the performance of all the four models. Print final train and test accuracies. Which model performs the best? 
- (Optional) You can also compare the models using cross-validation (CV). However, it may be time consuming to train every model on multiple CV folds.

**Note**: 
- **Hyperparameters:** For all the models implemented earlier, you only need to choose the learning rate (small enough for the loss to decrease monotonically but large enough for the training speed to be reasonable). In case of SVM, you also have a hyperparameter $C$ (equivalent to the inverted regularization hyperparameter in Ridge regression). You may compare (by test performance or cross-validation) several SVM models with different choices of C and choose the best one. Note that you may need to use different learning rates for SVM depending on the choice of C.
- **Training:** Try to ensure that all the models that you compare are well-trained, i.e. the loss does not decrease much in the end of training. Note that all the models considered in this task have convex loss functions. Therefore, it is possible to get a solution close to the global minimum using GD.



---
© [Mariia Seleznova](https://www.ai.math.uni-muenchen.de/members/phd_students/seleznova/index.html) 2022

https://github.com/mselezniova/MSML22

Distributed under the [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/)

