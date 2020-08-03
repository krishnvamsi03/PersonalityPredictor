import numpy as np
import pandas as pd
import joblib

classes = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
       'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

def preprocess(input_df):
    processing_obj = joblib.load("Preprocessing.pkl")
    platform = processing_obj['LabelEncoderMostUsedPlatform']
    frequent_user = processing_obj['LabelEncoderFrequentUser']
    frequent_posted = processing_obj['LabelEncoderFrequentlyPostAnything']
    most_liked_about = processing_obj['LabelEncoderMostPostLikedAbout']
    one_hot_most_used_platform = processing_obj['OneHotMostUsedPlatform']
    one_hot_most_liked_about = processing_obj['OneHotMostPostLikedAbout']
    sc = processing_obj['StandardScaler']

    input_df.iloc[:, 0] = platform.transform(input_df.iloc[:, 0].values.reshape(-1, 1))
    input_df.iloc[:, 3] = frequent_user.transform(input_df.iloc[:, 3].values.reshape(-1, 1))
    input_df.iloc[:, 4] = frequent_posted.transform(input_df.iloc[:, 4].values.reshape(-1, 1))
    input_df.iloc[:, 7] = most_liked_about.transform(input_df.iloc[:, 7].values.reshape(-1, 1))

    test_X = input_df.values
    print(test_X)
    test_X = np.append(test_X, one_hot_most_used_platform.transform(test_X[:, 0].reshape(-1, 1)).toarray(), axis = 1)
    test_X = np.append(test_X, one_hot_most_liked_about.transform(test_X[:, 7].reshape(-1, 1)).toarray(), axis = 1)
    test_X = np.delete(test_X, 0, 1)
    test_X = np.delete(test_X, 7, 1)
    return test_X.astype(float)

def predict(input_df):
    model = joblib.load("PersonalityClassifier.pkl")
    processed_input = preprocess(input_df)
    print(processed_input.shape)
    processed_input = np.append(processed_input, np.random.randint(0, 2, 4).reshape(1, -1), axis = 1)
    y_hat = model.predict(processed_input)
    return classes[int(y_hat)]