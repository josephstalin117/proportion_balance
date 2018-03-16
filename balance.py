# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:13:55 2018

@author: joseph
"""

        
def input_balance(req_list,init_list,init_total):
    
    if len(req_list)!=len(init_list):
        print('unequal length of list')
        return 0
    
    req_pro=[x/sum(req_list) for x in req_list]
    init_pro=[x/sum(init_list) for x in init_list]
    diff_pro=[req_pro[i]-init_pro[i] for i in range(0,len(req_pro))]
    
    if max(diff_pro)>0 and min(diff_pro)<0:
        t_index=diff_pro.index(min(diff_pro))
        t_pro=init_list[t_index]/req_list[t_index]
        x_delta=[req_list[x]*t_pro-init_list[x] if x!=t_index else 0 for x in range(0,len(req_pro))]
    
    return [init_total*x/sum(init_list) for x in x_delta]
    
    
    

if __name__ == '__main__':
    req_list=[31.5,0.5,0.5,0.5,7]
    init_list=[33,0.5,0.5,0.5,5.5]
    
    output=input_balance(req_list,init_list,140)
    print(output)
    
        


