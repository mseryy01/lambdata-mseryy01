"""
utility functions for working with DataFrames
"""

import pandas
TEST_DF = pandas.DataFrame([1,2,3,4,5,6,7,8,9,10])

### Train Test Split function
def train_val_test_split(X,y, train_size = 0.7, val_size=0.1, test_size=0.2,
    random_state=None, shuffle=True):
# Make sure after split data does not exceed 100%
    assert train_size + val_size + test_size==1
# First Split to val
    X_train_val, X_test, y_train_val, y_test = train_test_split(X,y,
    test_size=test_size, random_state=random_state, shuffle=shuffle)
# Second split to test
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val,
    test_size=val_size/(train_size+val_size), random_state=random_state,
    shuffle=shuffle)

return X_train, X_val, X_test, y_train, y_val, y_test

### Specific for my ongoing projrct. Get the ingredients column from the df data and create the list of all existing ingredients
ingredients = df.ingredients
rawlist=[item for sublist in ingredients.ravel() for item in sublist] #convert the ingredients list of lists into a list
ingredients=list(set(rawlist)) #remove duplicates

for ing in ingredients:
    vector=[]
    # loop for df data
    for recipe in df.ingredients:
        if ing in recipe:
            vector.append(1)
        else:
            vector.append(0)
    df[ing]=pd.Series(vector,index=df.index) # Adds column containing 0 and 1's for this ingredient
