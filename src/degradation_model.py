
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class DegradationModel:
    def __init__(self):
        self.poly = PolynomialFeatures(degree=2, include_bias=False)
        self.model = LinearRegression()

    def fit(self, df):
        X = df[["lap", "tyre_temp"]]
        X_poly = self.poly.fit_transform(X)
        y = df["lap_time"]
        self.model.fit(X_poly, y)

    def predict(self, lap, tyre_temp):
        X = pd.DataFrame({"lap": [lap], "tyre_temp": [tyre_temp]})
        X_poly = self.poly.transform(X)
        return float(self.model.predict(X_poly)[0])









