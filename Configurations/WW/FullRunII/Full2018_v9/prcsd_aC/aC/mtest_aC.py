#!/usr/bin/env python3

import json

# aC sample info generator                                                                                                                                                           
#op_nms = ['cHDD','cHWB','cHq1','cHl3','cW','cHl1','cll1','cHq3']
op_nms = ['cW', 'cHDD', 'cHWB', 'cHl1','cHl3','cHq1', 'cHq3', 'cll1']
mxd = [17, 24, 30, 35, 39, 42, 44]

ops = {}

sm_wt = 'LHEReweightingWeight[0]'
ops['sm'] = {'sm': sm_wt}

log = open('./log_of_aC_wts.txt','w')
log.write('Recording assembly of WC weights in human readable form:\n')

for i,op in enumerate(op_nms):
    wtp1_idx = i+1
    wtm1_idx = wtp1_idx + 8

    slq_wt = f'LHEReweightingWeight[{wtp1_idx}]'
    quad_wt = f'0.5(LHEReweightingWeight[{wtp1_idx}]+LHEReweightingWeight[{wtm1_idx}]-2*LHEReweightingWeight[0])'
    lin_wt = f'0.5*(LHEReweightingWeight[{wtp1_idx}]-LHEReweightingWeight[{wtm1_idx}])'

    #  Logging weights ---------------------------------------------
    log.write(f'\nWilson Coefficient: {op} ----'+'\n')
    log.write(f'\t\t\t WC+1 \t WC-1'+'\n')
    log.write(f'\tindex \t  {wtp1_idx} \t  {wtm1_idx}'+'\n')

    log.write(f'\tsm_lin_quad_{op}: {slq_wt}'+'\n')
    log.write(f'\tlin_{op}: {lin_wt}'+'\n')
    log.write(f'\tquad_{op}: {quad_wt}'+'\n')
    # --------------------------------------------------------------

    # Storing weights in dictionary for sample production
    ops[op] = {f'sm_lin_quad_{op}':slq_wt,
            f'quad_{op}':quad_wt,
            f'quad_{op}':lin_wt
        }

    # Now acquiring the mixed weights

    if i != len(op_nms)-1:
        log.write('\n\n')
        log.write('\tAcquiring mixed term interference terms:'+'\n')

    for j in range(i+1,len(op_nms)):
        op2 = op_nms[j]

        op2_wtp1_idx = j+1
        op2_wtm1_idx = op2_wtp1_idx + 8
        mxd_wt_idx = mxd[i] + j-wtp1_idx

        mxd_wt = f'LHEReweightingWeight[{mxd_wt_idx}]'

        log.write(f'\t\t\t Ops:\t {op} & {op2} (WC+1: {op2_wtp1_idx}, WC-1: {op2_wtm1_idx})'+'\n')
        log.write(f'\t\t Indices:\t {mxd[i]} + {j-wtp1_idx} = {mxd_wt_idx}'+'\n')
        log.write(f'\t\t\t\tmixed_{op}_{op2}: {mxd_wt}'+ '\n')

        ops[f'{op}_{op2}'] = {f'mixed_{op}_{op2}':mxd_wt}

#for i in range(len(op_nms)):
#    wt_idx = i+1 
#    lin_wt = '(LHEReweightingWeight[{}]-LHEReweightingWeight[{}])/2'.format(wt_idx,wt_idx+8)
#    quad_wt = '(LHEReweightingWeight[{}]+LHEReweightingWeight[{}]-2*{})/2'.format(wt_idx,wt_idx+8,sm_wt)
#    slq_wt = '({}+{}+{})'.format(sm_wt, lin_wt, quad_wt)
#
#
#    ops[op_nms[i]] = { 'lin_{}'.format(op_nms[i]): lin_wt,
#        'quad_{}'.format(op_nms[i]): quad_wt,
#        'sm_lin_quad_{}'.format(op_nms[i]): slq_wt
#        }
##
##for i in range(len(op_nms)-1):
##    iwt_idx = i+1
##    op1 = op_nms[i]
##    for j in range(i+1,len(op_nms)):
##        jwt_idx = j+1
##        op2 = op_nms[j]
##
##        print('mixed_{}_{}'.format(op1,op2))
##        
##        mxd_wt_idx = mxd[i] + j-iwt_idx
##        mxd_wt = 'LHEReweightingWeight[{}]'.format(mxd_wt_idx)
##        # [sm_lin_quad_A] + [sm_lin_quad_B] - sm (to get rid of duplicate sm) + 2*[mixed]
##        slqlq2m_wt = '{}+{}-{}+2*{}'.format(ops[op1]['sm_lin_quad_{}'.format(op1)],ops[op2]['sm_lin_quad_{}'.format(op2)],sm_wt,mxd_wt)
##
##        ops['{}_{}'.format(op1,op2)] = { 'mixed_{}_{}'.format(op1,op2): mxd_wt,
##                'sm_lin_quad_mixed_{}_{}'.format(op1,op2): slqlq2m_wt
##            }


with open('test_aC_wts.json','w') as fl:
    json.dump(ops,fl)

log.close()
