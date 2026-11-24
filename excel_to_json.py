import pandas as pd
import json

excel_file = "Calendrier_Avent_72_Messages_Complet.xlsx"

json_file = "calendrier_avent.json"

df = pd.read_excel(excel_file)

result = []

for _, row in df.iterrows():

    result.append({

        "jour": int(row["Jour"]),

        "coeur": str(row["CoeurMessage"]),
        "coeurImage": "images/" + str(row["CoeurImage"]),

        "hot": str(row["HotMessage"]),
        "hotImage": "images/" + str(row["HotImage"]),

        "ouch": str(row["OuchMessage"]),
        "ouchImage": "images/" + str(row["OuchImage"]),

        "sms": str(row["SMS"])

    })

with open(
    json_file,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=2
    )

print("JSON généré")