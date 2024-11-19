#!/usr/bin/pthon

import json

# aC sample info generator                                                                                                                                                           
#op_nms = ['cHDD','cHWB','cHq1','cHl3','cW','cHl1','cll1','cHq3']
op_nms = ['cW', 'cHDD', 'cHWB', 'cHl1','cHl3','cHq1', 'cHq3', 'cll1']
mxd = [17, 24, 30, 35, 39, 42, 44]

ops = {}

sm_wt = 'LHEReweightingWeight[0]'
ops['sm'] = {'sm': sm_wt}

for i in range(len(op_nms)):
    wt_idx = i+1 
    lin_wt = '(LHEReweightingWeight[{}]-LHEReweightingWeight[{}])/2'.format(wt_idx,wt_idx+8)
    quad_wt = '(LHEReweightingWeight[{}]+LHEReweightingWeight[{}]-2*{})/2'.format(wt_idx,wt_idx+8,sm_wt)
    slq_wt = '({}+{}+{})'.format(sm_wt, lin_wt, quad_wt)


    ops[op_nms[i]] = { 'lin_{}'.format(op_nms[i]): lin_wt,
        'quad_{}'.format(op_nms[i]): quad_wt,
        'sm_lin_quad_{}'.format(op_nms[i]): slq_wt
        }

for i in range(len(op_nms)-1):
    iwt_idx = i+1
    op1 = op_nms[i]
    for j in range(i+1,len(op_nms)):
        jwt_idx = j+1
        op2 = op_nms[j]

        print('mixed_{}_{}'.format(op1,op2))
        
        mxd_wt_idx = mxd[i] + j-iwt_idx
        mxd_wt = 'LHEReweightingWeight[{}]'.format(mxd_wt_idx)
        # [sm_lin_quad_A] + [sm_lin_quad_B] - sm (to get rid of duplicate sm) + 2*[mixed]
        slqlq2m_wt = '{}+{}-{}+2*{}'.format(ops[op1]['sm_lin_quad_{}'.format(op1)],ops[op2]['sm_lin_quad_{}'.format(op2)],sm_wt,mxd_wt)

        ops['{}_{}'.format(op1,op2)] = { 'mixed_{}_{}'.format(op1,op2): mxd_wt,
                'sm_lin_quad_mixed_{}_{}'.format(op1,op2): slqlq2m_wt
            }


with open('aC_wts.json','w') as fl:
    json.dump(ops,fl)
