import numpy as np
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

#path = r"C:\Users\0000112098\Documents\Open Energy System\32_Simulation\DCOES performance\result\Enefarm simulation\20170323\20170323_145006_DCOES"
#csv = pd.read_csv(path + r"\result_summary.csv")

### Data alinement

os.chdir("data")
csv1 = pd.read_csv("standalone_summary.csv")
csv2 = pd.read_csv("dcoes_summary.csv")

df_sta = csv1[:1]
df_oes = csv2[:1]
df = pd.concat([df_sta, df_oes])
df.index = ["Standalone", "DCOES"]
df["SELF"] = df["CONSUMPTION"] * df["SELF_SUFFICIENT"] / 100
df["BUY"] = df["CONSUMPTION"] - df["SELF"]
df.iloc[:,1:] /= 1000

"""
con = np.array([df.loc["Standalone","CONSUMPTION"], 0, 0])
buy = np.array([0, df.loc["Standalone","BUY"], df.loc["DCOES","BUY"]])
self = np.array([0, df.loc["Standalone","SELF"], df.loc["DCOES","SELF"]])
sur = np.array([0, df.loc["Standalone","SURPLUS"], df.loc["DCOES","SURPLUS"]])
"""

con = df.loc["Standalone","CONSUMPTION"]
buy = pd.DataFrame([df.loc["Standalone","BUY"], df.loc["DCOES","BUY"]])
self =pd.DataFrame([df.loc["Standalone","SELF"], df.loc["DCOES","SELF"]])
sur = pd.DataFrame([df.loc["Standalone","SURPLUS"], df.loc["DCOES","SURPLUS"]])

labels = ["Consumption", "Buy", "Self", "Surplus"]
#df_plt = pd.concat([con, buy, self, sur], axis=1)
df_plt = pd.concat([buy, self, sur], axis=1)

fig, ax = plt.subplots()
xvals = np.arange(len(df_plt))
xvals2 = np.arange(len(df_plt)+1)
width = 0.5
colors = ["gray", "orange", "blue", "brown"]
bottom = np.zeros(df_plt.shape[0])

plt.bar(0, con, width, color=colors[0])
ann = ax.annotate("{:,d}".format(int(con)), xy=(-width*0.3, bottom[0]+con*0.45),fontsize=12, color="white")

for i in range(df_plt.shape[1]):
    plt.bar(xvals+1, 
            df_plt.iloc[:,i], 
            width, 
            bottom, 
            color=colors[i+1],
            label=labels[i+1] 
            )
    
    for j in range(len(df_plt)):
        #ann = ax.annotate(str(df_plt.iloc[j,i]), xy=(xvals[j]-width/4, bottom[j]+df_plt.iloc[j,i]*0.45),fontsize=12)
        ann = ax.annotate("{:,d}".format(int(df_plt.iloc[j,i])), xy=(xvals[j]+width*1.7, bottom[j]+df_plt.iloc[j,i]*0.45),fontsize=12, color="white")
    
    bottom += df_plt.iloc[:,i]


### Draw diagram

"""
fig = plt.figure()

plt.bar(xvals, con, width, color="gray")
plt.text(xvals, con, con)
plt.bar(xvals, buy, width, color="orange")
plt.bar(xvals, self, bottom=buy, width = 0.5, color="blue")
plt.bar(xvals, sur, bottom=buy+self, width = 0.5, color="brown")
"""
plt.xticks(xvals2, ["Consumption", "Standalone", "DCOES"])
commaform = mpl.ticker.FuncFormatter(lambda x,p: format(int(x), ','))
ax.get_yaxis().set_major_formatter(commaform)
plt.ylabel("[kWh]")
plt.title("Yearly data")
plt.legend(["Consumption", "Buy", "Self", "Surplus"])


plt.grid(False)

plt.show()


#print(xvals)

