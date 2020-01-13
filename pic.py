import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

COSMOS = pd.read_csv('match_COSMOS_99_with_err.csv')
COSMOS_rv=COSMOS[COSMOS['zspec']> 0]
#COSMOS_rv = COSMOS[-COSMOS.zspec.isin([-99])]
#print(COSMOS_rv)

COSMOS_rv = COSMOS_rv.replace({-99.9: None})
COSMOS_rv = COSMOS_rv.replace({-99: None})

'''
def MAG_pic(column,df=COSMOS_rv):
    #plt.hist(x=df[column].dropna().values, bins='auto' ,color='#0504aa',alpha=0.7, rwidth=0.85,histtype='stepfilled')
    plt.hist(x=df[column].dropna().values, bins='auto', histtype='step',label=column)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.savefig(column+".png",dpi=600,bbox_inches='tight')
    print("done"+column)
    

def REDSHIFT(column,df=COSMOS_rv):
    plt.hist(x=df[column].dropna().values, bins='auto', color='#607c8e', alpha=0.7, rwidth=0.85,histtype='stepfilled')
    plt.savefig(column+".png")

def compare_pic(column_MAG,column_REDSHIFT,df=COSMOS_rv):
    plt.hist(x=df[column_MAG].dropna().values, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85, histtype='stepfilled')
    plt.hist(x=df[column_REDSHIFT].dropna().values, bins='auto', color='#607c8e', alpha=0.7, rwidth=0.85, histtype='stepfilled')
    plt.savefig(column_MAG+"_"+column_REDSHIFT+".png")


MAG_pic("B_MAG_APER2")
MAG_pic("H_MAG_APER2")
MAG_pic("Hw_MAG_APER2")
MAG_pic("IA484_MAG_APER2")
MAG_pic("IA527_MAG_APER2")
MAG_pic("IA624_MAG_APER2")
MAG_pic("IA679_MAG_APER2")
MAG_pic("IA738_MAG_APER2")
MAG_pic("IA767_MAG_APER2")
MAG_pic("IB427_MAG_APER2")
MAG_pic("IB464_MAG_APER2")
MAG_pic("IB505_MAG_APER2")
MAG_pic("IB574_MAG_APER2")
MAG_pic("IB709_MAG_APER2")
MAG_pic("IB827_MAG_APER2")
MAG_pic("J_MAG_APER2")
MAG_pic("Ks_MAG_APER2")
MAG_pic("Ksw_MAG_APER2")
MAG_pic("NB711_MAG_APER2")
MAG_pic("NB816_MAG_APER2")
MAG_pic("SPLASH_1_MAG")
MAG_pic("SPLASH_2_MAG")
MAG_pic("SPLASH_3_MAG")
MAG_pic("SPLASH_4_MAG")
MAG_pic("V_MAG_APER2")
MAG_pic("Y_MAG_APER2")
MAG_pic("ip_MAG_APER2")
MAG_pic("r_MAG_APER2")
MAG_pic("yHSC_MAG_APER2")
MAG_pic("zpp_MAG_APER2")

'''

def plot_MAG(column,df=COSMOS_rv):
    plt.figure()
    plt.hist(x=df[column].dropna().values, bins='auto' , histtype='step',label=column,lw=3)
    #plt.hist(x=df[column].dropna().values, bins=50, label=column, )
    #plt.hist(x=df[column], bins='auto', histtype='step', label=column)
    #plt.figure(figsize=(10, 10))
    plt.title(column)
    plt.legend()
    plt.xlim(15, 30)
    #plt.ylim(0, 1000)
    plt.savefig(column)
    #plt.show()
    print("done"+column)



label_list=["B_MAG_APER2","H_MAG_APER2","Hw_MAG_APER2","IA484_MAG_APER2","IA527_MAG_APER2","IA624_MAG_APER2",
            "IA679_MAG_APER2","IA738_MAG_APER2","IA767_MAG_APER2","IB427_MAG_APER2","IB464_MAG_APER2","IB505_MAG_APER2",
            "IB574_MAG_APER2","IB709_MAG_APER2","IB827_MAG_APER2","J_MAG_APER2","Ks_MAG_APER2","Ksw_MAG_APER2",
            "NB711_MAG_APER2","NB816_MAG_APER2","SPLASH_1_MAG","SPLASH_2_MAG","SPLASH_3_MAG","SPLASH_4_MAG","V_MAG_APER2",
            "Y_MAG_APER2","ip_MAG_APER2","r_MAG_APER2","yHSC_MAG_APER2","zpp_MAG_APER2"]

for column in label_list:
    plot_MAG(column)

print("all done")
#print(pd.value_counts(COSMOS_rv["B_MAG_APER2"],sort=False))

'''
plt.subplots(15, 1,figsize=(80.0*15, 60.0*1))
plt.hist(COSMOS_rv["B_MAG_APER2"].dropna().values, bins='auto' ,color='#607c8e',alpha=0.7, rwidth=0.85,histtype='stepfilled',label="B_MAG_APER2")
plt.hist(COSMOS_rv["H_MAG_APER2"].dropna().values, bins='auto' ,color='#607c8e',alpha=0.7, rwidth=0.85,histtype='stepfilled',label="H_MAG_APER2")
plt.legend()


plt.show()

plt.figure("PER2")
plt.hist(COSMOS_rv["B_MAG_APER2"].dropna().values, bins='auto' ,color='#607c8e',alpha=0.7, rwidth=0.85,histtype='stepfilled')
plt.show()
'''
