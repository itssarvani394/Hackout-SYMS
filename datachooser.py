import urllib.request
import io
import pandas as pd
import csv

def givestringio(url):
    req = urllib.request.urlopen(url)
    data = req.read()
    data = io.StringIO(str(data)[2:-1])
    return data


data1 = givestringio("https://services.swpc.noaa.gov/json/rtsw/rtsw_mag_1m.json")
data2 = givestringio("https://services.swpc.noaa.gov/json/rtsw/rtsw_wind_1m.json")
data3 = givestringio("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json")
data4 = givestringio("https://services.swpc.noaa.gov/json/dscovr/dscovr_mag_1s.json")
data5 = givestringio("https://services.swpc.noaa.gov/json/rtsw/rtsw_wind_1m.json")

df1 = pd.read_json(data1)
df1 = df1[df1['source'] == "DSCOVR"]
df1.to_csv("rtsw_mag_1m.csv", index = False)

df2 = pd.read_json(data2)
df2 = df2[df2['source'] == "DSCOVR"]
df2[["proton_speed", "proton_density"]].to_csv("rtsw_wind_1m.csv", index = False)

df3 = pd.read_json(data3)
df3[["time_tag", "kp_index", "estimated_kp"]].to_csv("planetary_k_index_1m.csv", index = False)

df4 = pd.read_json(data4)
df4.to_csv("dscovr_mag_1s.csv", index = False)

dfa = pd.read_json(data5)
dfa[["proton_vx_gse", "proton_vy_gse", "proton_vz_gse", "proton_vx_gsm", "proton_vy_gsm", "proton_vz_gsm"]].to_csv("rtsw_wind_1m-vxvyvzgsegsm.csv", index = False)



def enumeratefirstcol(s):    
    with open(s, "r") as f:
        obj = csv.reader(f)
        rows = []
        for row in obj:
            rows.append(row)


    for i in range(1, len(rows)):
        rows[i][0] = i


    with open(s, "w", newline = "") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(rows)



enumeratefirstcol("dscovr_mag_1s.csv")
enumeratefirstcol("planetary_k_index_1m.csv")
enumeratefirstcol("rtsw_mag_1m.csv")
enumeratefirstcol("rtsw_wind_1m-vxvyvzgsegsm.csv")
enumeratefirstcol("rtsw_wind_1m.csv")