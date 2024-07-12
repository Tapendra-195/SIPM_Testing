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
print(name)
print(extension)
ch_a,ch_b,ch_c,ch_d,fc  = name.split('_')
chans = [ch_a,ch_b,ch_c,ch_d]

'''
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
'''

f = open(directory + "mean_sd_"+ch_a+"_"+ch_b+"_"+ch_c+"_"+ch_d+".txt", "w")
f.write("Ch \t mean(nA) \t sd(nA) \n")


for i,chan in enumerate(chans):
    mean = df['IsCH_'+str(chan)+' (A)'].mean()*1000000000;
    sd = df['IsCH_'+str(chan)+' (A)'].std()*1000000000;
    f.write(str(chan) + "\t"+ str(mean) + "\t" + str(sd) + "\n")
    print( chan, " mean ", mean)
    print( chan, " std ", sd)

f.close()
