## Training and Testing
- The only method to assess a model's performance is to subject it to fresh test cases. This may be accomplished by putting your model into production, but if your model is severely flawed, this might be hazardous.
- Another option is to divide your dataset into training and testing data sets. 
- The training dataset is used to train the model, while the testing dataset is used to evaluate the model. 
- The error we obtain when we test the model with the test set tells us how well the model works on unknown data.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=2)
 
- In the above code, we have used the train_test_split method from the sklearn module. 
- Parameters of train_test_split() : 
- X : features in dataset 
- y : labels in dataset 
- test_size : Splits the datasets into given ratio (eg test_size=0.3 splits data into 70:30) 
- random_state : random_state simply sets a seed to random generator so that splits are always deterministic.
-  But When evaluating different hyperparameters for complex algorithms like SVM, Decision Tree there is still a risk of overfitting on the test set because parameters can be twitched to perform optimally. 
 This can leak the knowledge about test cases into the model and can overfit. To solve this problem another part of the dataset can be created as a “ Validation set ”.
 Now training will be done on training data evaluation is done on validation data and for final evaluation testing data should be used.
 
 ## Training, Testing and Validating
X_train, X_rem, y_train, y_rem = train_test_split(X, y, test_size=0.3,random_state=33)  
 
X_val, X_test, y_val, y_test = train_test_split(X_rem, y_rem, test_size=0.6,random_state=33)
 
- In the above code, we first split the training data and from the remaining data, we created a testing and validation set. However, splitting data into three sets (Training set, Testing set, and validation set) reduces the quantity of data required to train the model.
- A solution to this problem is called “Cross-Validation
