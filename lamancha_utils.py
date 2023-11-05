import pandas as pd
import re
from datetime import datetime


df = pd.read_csv("C:\\Users\\usuario\\Desktop\\ehu_python\\5_WikiData\\lamancha_project\\lamancha.csv")



def get_stats(df):
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")
    print(f"Name columns: {', '.join(df.columns)}")
    print("Gender:")
    gender_counts = df['genderLabel'].value_counts()
    for gender, count in gender_counts.items():
        print(f"{gender}: {count}", end=". ")

#df["birthDate"] = df["birthDate"].apply(lambda x: x.split("T")[0])
#df["birthDate"] = df["birthDate"].str.replace(r"\b0", "", regex=True)
#df["birthDate"] = df["birthDate"].apply(lambda x: x.split("-"))
#df["birthDate"] = df["birthDate"].apply(lambda x: x[::-1])


def get_zodiac_sign(date):
    day, month, year = date
    day = int(day)
    month = int(month)
    zodiac_signs = {
        
        (3, 21): "Aries",
        (4, 20): "Tauro",
        (5, 21): "Géminis",
        (6, 21): "Cáncer",
        (7, 23): "Leo",
        (8, 23): "Virgo",
        (9, 23): "Libra",
        (10, 23): "Escorpio",
        (11, 22): "Sagitario",
        (12, 22): "Capricornio",
        (1, 20): "Acuario",
        (2, 19): "Piscis",
        
    }

    for (start_month, start_day), sign in zodiac_signs.items():
        if month == 1 and day == 1:
            return "Desconocido"
        elif (month == start_month and day >= start_day) or (month == start_month % 12 + 1 and day <= start_day - 1):
            return sign

#df["signos"] = df["birthDate"].apply(lambda x: get_zodiac_sign(x))
#sing_counts = df.value_counts("signos")


#df["signos"] = df["birthDate"].apply(lambda x: get_zodiac_sign(x))
#sing_counts = df.value_counts("signos")





#gender_counts = lamancha.value_counts("genderLabel")


#fila_mujer_transgenero = lamancha.loc[lamancha['genderLabel'] == 'mujer transgénero']
