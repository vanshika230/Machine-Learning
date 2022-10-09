## Hyperparameter Optimization
- Hyperparameters are variables whose values influence the learning process and affect the model parameters that a learning algorithm learns. This Hyperparameter should be tuned so that the model produces a satisfactory score, although determining the optimum settings for certain datasets might be difficult. For configuring hyperparameters, there are frequently broad guidelines.
- A better method is to find a subset of hyperparameters that provide the best model objectively. This is known as Hyperparameter Optimization.

## GridSearchCV
- Grid Search calculates the performance for each combination of all the supplied hyperparameters and their values, and then chooses the optimum value for the hyperparameters. 
- Grid Search along with Cross-validation is known as GridSearchCV K-Fold cross-validation is the most often used cross-validation technique. 
- We divide datasets into k folds in this method. Each fold is then validated once, with the remaining k-1 folds being the training set. 
- As a result, evaluating the optimum parameters using GridSearch and cross-validation takes a lengthy time.

## RandomizeSearchCV
- When we have a big number of parameters and testing each one results in high training costs, Randomize Search is utilized. 
- Randomize Search will pick a combination of parameters at random to acquire the best results. 
- It's similar to GridSearch in that, rather than trying every combination, Randomize Search chooses a combination at random to find the optimal solution with the fewest iterations.
