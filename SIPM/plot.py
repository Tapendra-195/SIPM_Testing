import pandas as pd
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]#"9_10_11_12.csv"
directory = sys.argv[2]
print("loading ",filename, " from ", directory)


#for chan in chans:
#    dfs.append( pd.read_csv('test_ch'+str(chan)+'.csv',skipinitialspace=True) )
            
#dfs[1].keys()

df =  pd.read_csv(directory+filename,skipinitialspace=True) 

name, extension = filename.split('.')
ch_a,ch_b,ch_c,ch_d  = name.split('_')
chans = [ch_a,ch_b,ch_c,ch_d]
print(df)
print(df['HV_set (V)'])

print(df['HV_set (V)'].to_numpy())


plt.figure( figsize=(3,3), dpi=100)
plt.plot( df['HV_set (V)'].to_numpy(), df['HV_rdb (V)'].to_numpy(), '.', label='CH'+str(name))
plt.ylabel('HV_rdb (V)')
plt.xlabel('HV_set (V)')
plt.legend()
plt.tight_layout()
plt.savefig(directory+'HVset-rdb-ch'+name+'.png',facecolor='w')

plt.figure( figsize=(3,3), dpi=100)
plt.plot( df['HV_set (V)'].to_numpy(), df['HV_err (V)'].to_numpy(), '.', label='CH'+str(name))
plt.ylabel('HV_err (V)')
plt.xlabel('HV_set (V)')
plt.legend()
plt.tight_layout()
plt.savefig(directory+'HVerr-ch'+name+'.png',facecolor='w')

# 'VsCH_2 (V)', 'IsCH_2 (A)'
plt.figure( figsize=(3,3), dpi=100)
for i,chan in enumerate(chans):
    plt.plot( df['VsCH_'+str(chan)+' (V)'].to_numpy(), df['IsCH_'+str(chan)+' (A)'].to_numpy(),  '.', label='CH'+str(chan) )
plt.xlabel('Vs (V)')
plt.ylabel('Is (A)')
plt.legend()
plt.tight_layout()
plt.savefig(directory+'IV-curve-ch'+name+'.png',facecolor='w')
