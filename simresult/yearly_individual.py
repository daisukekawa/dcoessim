import numpy as np
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

#path = r"C:\Users\0000112098\Documents\Open Energy System\32_Simulation\DCOES performance\result\Enefarm simulation\20170323\20170323_145006_DCOES"
#csv = pd.read_csv(path + r"\result_summary.csv")

### Data alinement

os.chdir("data")
#csv1 = pd.read_csv("standalone_summary.csv")
csv2 = pd.read_csv("dcoes_summary.csv")

#df_sta = csv1[2:]
df = csv2[1:]
#df = pd.concat([df_sta, df_oes])
#df.index = ["Standalone", "DCOES"]
con = df["CONSUMPTION"] / 1000
self = con * df["SELF_SUFFICIENT"] / 100
buy = con - self
sur = df["SURPLUS"] / 1000
chg = df["EXCHANGE_CHARGE"] / 1000
dchg = df["EXCHANGE_DISCHARGE"] / 1000

labels0 = ["Buy", "Self", "Surplus"]
labels1 = ["Charge", "Discharge"]

df_plt0 = pd.concat([buy, self, sur], axis=1)
df_plt1 = pd.concat([chg, dchg], axis=1)
df_plt0.columns = labels0
house = []
for i in range(len(df_plt0)):
    house.append("house" + str(i+1))

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
xvals = np.arange(len(df_plt0))
xvals1 = np.arange(len(df_plt1))
width = 0.7
colors = ["orange", "blue", "brown"]
colors1 = ["black", "gray"]
bottom = np.zeros(df_plt0.shape[0])

for i in range(df_plt0.shape[1]):
    ax0.bar(xvals, 
            df_plt0.iloc[:,i], 
            width, 
            bottom, 
            color=colors[i],
            label=labels0[i] 
            )
    #for j in range(len(df_plt)):
        #ann = ax.annotate("{:,d}".format(int(df_plt.iloc[j,i])), xy=(xvals[j]+width*1.7, bottom[j]+df_plt.iloc[j,i]*0.45),fontsize=12, color="white")
    
    bottom += df_plt0.iloc[:,i]

for i in range(df_plt1.shape[1]):
    ax1.bar(xvals1, 
            df_plt1.iloc[:,i], 
            width, 
            #bottom, 
            color=colors1[i],
            label=labels1[i] 
        )
    
### Draw diagram

commaform = mpl.ticker.FuncFormatter(lambda x,p: format(int(x), ','))
ax0.get_yaxis().set_major_formatter(commaform)
ax1.get_yaxis().set_major_formatter(commaform)

handles0, labels0 = ax0.get_legend_handles_labels()
ax0.legend(handles0[::-1], labels0[::-1], bbox_to_anchor=(0.9, 1.1), fontsize=9)
handles1, labels1 = ax1.get_legend_handles_labels()
ax1.legend(handles1[::-1], labels1[::-1], bbox_to_anchor=(0.9, 0.45), fontsize=9)
ax0.axhline(y=0, lw=1, color="black")
ax1.axhline(y=0, lw=1, color="black")
ax0.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='on')
ax0.spines['right'].set_color('none')
ax0.spines['top'].set_color('none')
ax1.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='on')
ax1.spines['right'].set_color('none')
ax1.spines['bottom'].set_color('none')
ax1.spines['top'].set_color('none')

ax1.set_xticks(xvals)
ax1.set_xticklabels(house, rotation=90)
fig.subplots_adjust(left=0.12, bottom=0.17, right=0.9, top=0.9, wspace=0.15, hspace=0.15)
ax0.tick_params(labelsize=9)
ax1.tick_params(labelsize=9)

plt.show()



