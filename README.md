# polish companies bankruptcy

## Concept

This challenge is about the bankruptcy prediction. A classification study with unbalanced classes.
The 5 initial arff files are converted to 5 csv files in order to conceive the dataframe.
It includes 64 features, adding to this the target and one feature about the year that I have added.
The target, named "class", is a numeric feature. 0 means no bankruptcy while 1 means the bankruptcy.
Due to the unbalanced target classes, the choice of the metrics is mainly based on the recall (the true positive) and the auc.

## Building the API
I have implemented the flask API by using the decision tree classifier model with the most important features resulting of a seven feature model.
