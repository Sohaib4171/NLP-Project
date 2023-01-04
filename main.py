import pandas as pd
from model import xgb, test_df

def submission(model, test_sentences):
    # test1 = pd.read_csv('dataset/test.csv')
    test1 = pd.read_csv('predictionData/predict.csv')
    print("TEST Sentence")
    print(test_sentences)
    preds = model.predict(test_sentences)
    prediction = pd.DataFrame(preds, columns = ['Match Percentage'])
    sub_df = pd.concat([test1, prediction], axis = 1)
    return sub_df

print("TEST DF")
print(test_df)
sub = submission(xgb, test_df)
sub.to_csv('results/predictions.csv')
print(sub.head())