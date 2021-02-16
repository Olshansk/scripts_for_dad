import glob

import re
import openpyxl
import pandas
import pandas as pd

columns = [
    "Set Sample name",
    "Confined pressure s3/Patm (1)",
    "Confined pressure s3/Patm (2)",
    "Confined pressure s3/Patm (3)",
    "# of samples",
    "phi",
    "c",
    "Rf",
    "E50_ref [Kpa]",
    "m",
    "Eur_ref [Kpa]",
    "dr (dilation)",
    "pr (Poisson)",
    "OCR",
    "Knc"
    ]

dat_keywords = ['dr_', 'pr_', 'OCR_', 'Knc_']

def get_num_from_string(s):
    result = re.findall(r'[\d]*[.][\d]*', s)
    if len(result) == 1:
        return float(result[0])
    return None

data = []
for txt_file in glob.glob("*.txt"):
    row = []
    with open(txt_file, 'r') as f:
        line = f.read().strip().split(',')
        row.append(line[0])
        row.extend(list(map(lambda x: float(x), line[1:])))

    dat_file = txt_file.replace('testing_', 'single_set').replace('.txt', '.dat')
    with open(dat_file, 'r') as f:
        for line in f.readlines():
            if any(keyword in line for keyword in dat_keywords):
                r = get_num_from_string(line)
                if r is not None: row.append(r)
    data.append(row)

df = pd.DataFrame(data, columns=columns)
df.to_excel("output.xlsx", index=False)
print(df)
