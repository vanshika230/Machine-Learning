<h1 align="center"> 👩‍⚕️ Diabetes Classification </h1>

 # ✅ Objective of this project
- The objective of this project is to classify whether someone has diabetes or not. We have to use the Independent Variables data to train the model to predict the dependent variable(outcome). 
- The independent variables in this data set are :-'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'
- The outcome variable value is either 1 or 0 indicating whether a person has diabetes(1) or not(0).

# 🔥 Implements the following Algorithm :- 
### ✔ K-nearest neighbor
K-nearest neighbor, also known as the KNN algorithm, is a non-parametric algorithm that classifies data points based on their proximity and association to other available data. This algorithm assumes that similar data points can be found near each other. As a result, it seeks to calculate the distance between data points, usually through Euclidean distance, and then it assigns a category based on the most frequent category or average.KNN is typically used for recommendation engines and image recognition.

### Data Set used :- https://www.kaggle.com/c/diabetes-classification/data

## 💯 Procedure followed :- 

1️⃣ Data Preparation

2️⃣ Implementation of KNN

3️⃣ Predictions on Test Data

### 🙌 Applying KNN from Scratch 
```
  def knn(X,Y,queryPoint,k=5):
    
    vals = []#saves people info as tuples
    m = X.shape[0] #no. of people
    
    for i in range(m):
        d = dist(queryPoint,X[i])#calculating euclidian distance
        vals.append((d,Y[i])) #appending distance and label
        
    
    vals = sorted(vals) #sorting distances
    # Nearest/First K points
    vals = vals[:k] #until mentioned K points
    
    vals = np.array(vals) #converting to numpy array
    
    #print(vals)
    
    new_vals = np.unique(vals[:,1],return_counts=True) #counting no. of unique labels
    #print(new_vals)
    
    index = new_vals[1].argmax()#max count label
    pred = new_vals[0][index] #returning label of max count
    
    return pred
    
```
