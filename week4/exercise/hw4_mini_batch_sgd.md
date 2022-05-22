# Week 4 (E): Mini-batch SGD

The goal of this task is to implement  and test **Mini-batch Stochastic Gradient Descent** (SGD).  Below is the pseudocode of the algorithm:

0. Choose **hyperparameters**: learning rate $\eta\in\mathbb{R}$, number of epochs $K\in\mathbb{N}$, batch size $B\in\mathbb{N}$.
1. **Initialize** trainable parameters $w = w^{(0)}$. Set $k=0$. 
2. **While** epoch $k < K$: 
    - **While** $i < \lceil |X| / B\rceil$:
         - Sample batch $(X_i,Y_i)$ of size $B$ from $(X,Y)$ randomly without replacement.
         - Run a GD update on the batch:
$$w \leftarrow w - \eta \nabla_w  R (w,X_i,Y_i)$$
         - Update $i$: $i=i+1$

         
   - Update epoch number $k$: $$k = k+1$$
3. **Return** $w$.

**Note:**

- Batches are sampled without replacement within an epoch, i.e. $\{X_i\}_{i=1,\dots,\lceil |X| / B\rceil}$ are disjoint.
- In every epoch, batches should be resampled independently, i.e. you should not use the same choice of batches over many epochs.

**You need to:**

- Modify the train() method of LinearBinaryClassification class so that it performs Mini-batch SGD instead of ordinary (full-batch) GD. The implementation needs to accept **arbitrary batch size**, i.e. you should include batch size as an argument of the training function.
- Load the Iris dataset and separate it into two classes, as done in the exercise class. Unlike in the previous classes, use **all the four variables** of the dataset to form feature matrix $X$.
- Train  your classification model multiple times using different values of the batch size, e.g. [1,5,10,20,50,150 (full-batch)]. Plot the learning curves (which include **every update**, not just every epoch ) for all the batch sizes. What behaviour do you observe in mini-batch SGD in comparison to full-batch GD? How do the curves corresponding to different batch sizes compare?