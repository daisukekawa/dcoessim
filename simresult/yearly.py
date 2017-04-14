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
df.iloc[:,1:3] /= 1000
df.iloc[:,4:10] /= 1000
df.iloc[:,11:] /= 1000

con = df.loc["Standalone","CONSUMPTION"]
buy = pd.DataFrame([df.loc["Standalone","BUY"], df.loc["DCOES","BUY"]])
self =pd.DataFrame([df.loc["Standalone","SELF"], df.loc["DCOES","SELF"]])
sur = pd.DataFrame([df.loc["Standalone","SURPLUS"], df.loc["DCOES","SURPLUS"]])
exc = pd.DataFrame([df.loc["Standalone","EXCHANGE_CHARGE"], df.loc["DCOES","EXCHANGE_CHARGE"]])

labels = ["Consumption", "Buy", "Self", "Surplus"]
df_plt = pd.concat([buy, self, sur], axis=1)

fig, ax = plt.subplots()
xvals = np.arange(len(df_plt)) ## delete -1 to include exchange
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

plt.xticks(xvals2, ["Consumption", "Standalone", "DCOES"])
commaform = mpl.ticker.FuncFormatter(lambda x,p: format(int(x), ','))
ax.get_yaxis().set_major_formatter(commaform)
plt.title("Yearly data [kWh]")
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1, 1.06), fontsize=9)
fig.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.9, wspace=0.15, hspace=0.15)
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
for spine in plt.gca().spines.values():
    spine.set_visible(False)


plt.show()


