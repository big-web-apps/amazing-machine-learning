import pandas as pd
from joblib import load


def predict(estate_params=[2, 64.56, 18, 126100]):
    # param:
    #   [room number,
    #   square,
    #   floor,
    #   current price]

    test_series = pd.Series(estate_params)
    forecaster = load("forecaster.py")

    predictions = forecaster.predict(steps=50, last_window=test_series)
    # return float value
    predicted_coefficent = predictions.median() / test_series[3]

    return predicted_coefficent

# def train_and_save_model():
#     df = pd.read_csv("data.csv")

#     df2501 = df.drop(["Цена на 11.06.2022", "Цена на 15.02.2023"], axis=1)
#     df2501 = df2501.assign(date="25.01.2022")
#     df2501.rename(
#         {
#             "Цена на 25.01.2022": "price",
#         },
#         inplace=True,
#         axis=1,
#     )

#     df1106 = df.drop(["Цена на 25.01.2022", "Цена на 15.02.2023"], axis=1)
#     df1106 = df1106.assign(date="11.06.2022")
#     df1106.rename(
#         {
#             "Цена на 11.06.2022": "price",
#         },
#         inplace=True,
#         axis=1,
#     )

#     df1502 = df.drop(["Цена на 11.06.2022", "Цена на 25.01.2022"], axis=1)
#     df1502 = df1502.assign(date="15.02.2023")
#     df1502.rename(
#         {
#             "Цена на 15.02.2023": "price",
#         },
#         inplace=True,
#         axis=1,
#     )

#     df2501 = df2501.append(df1106)
#     df2501 = df2501.append(df1502)

#     df2501.rename(
#         {
#             "Цена на 25.01.2022": "price",
#         },
#         inplace=True,
#         axis=1,
#     )

#     # df = pd.get_dummies(df, columns=('Name complex'))
#     df = df.drop(["date", "Name complex"], axis=1)
#     steps = 50
#     data_train = df[:-steps]
#     # data_test = df[-steps:]

#     forecaster = ForecasterAutoreg.ForecasterAutoreg(
#         regressor=RandomForestRegressor(random_state=123), lags=4
#     )

#     forecaster.fit(y=data_train["price"])
#     # Save model
#     dump(forecaster, filename="forecaster.py")
