import os
import pathlib
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings('ignore')

class Predict:
    def __init__(self) -> None:
        self.dataset = None

    def init(self):
        BASE_DIR = pathlib.Path(__file__).parent.resolve()
        self.dataset = pd.read_csv(os.path.join(BASE_DIR, "dataset/heart.csv"))

    def predict(self, info):
        Y = self.dataset['target']
        X = self.dataset.drop(['target'], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

        randomforest_classifier = RandomForestClassifier(n_estimators=10, min_samples_split=10)
        randomforest_classifier.fit(X_train, y_train)
        y_pred = randomforest_classifier.predict(X_test)
        score = cross_val_score(randomforest_classifier, X, Y, cv=10)

        result = randomforest_classifier.predict([info])
        result_proba = randomforest_classifier.predict_proba([info])

        self.dataset = self.dataset.append({'age':[info[0]], 'sex':[info[1]], 'cp':[info[2]], 'trestbps':[info[3]], \
                             'chol':[info[4]], 'fbs':[info[5]], 'restecg':[info[6]], 'thalach':[info[7]], \
                             'exang':[info[8]], 'oldpeak':[info[9]], 'slope':[info[10]], 'ca':[info[11]], \
                             'thal':[info[12]], 'target':[result]}, ignore_index=True)
        #  TODO: duplicate
        # print(result)
        # print(result_proba)
        # bool_series = self.dataset.duplicated(subset=['age', 'sex'])
        # print(bool_series)
        # [[0.97 0.03]]   0.97 probility of getting heart-disease
        return result_proba[0][1]


# def main():
#     predict = Predict()
#     predict.init()
#     # info = [71, 0, 0, 130, 149, 0, 1, 125, 0, 2.1, 1, 0, 2]
#     info = [50,0,0,110,254,0,0,159,0,0,2,0,2]
#     result = predict.predict(info)
#     print(result)

# main()