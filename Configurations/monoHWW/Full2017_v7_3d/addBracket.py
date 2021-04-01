import os
import shutil
import argparse

import subprocess

#python addBracket.py --inputDir datacards_2016

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Receive the parameters")
    parser.add_argument('--inputDir', action = 'store', type = str, dest = 'inputDir', help = 'Define the inputDir path')
    args = parser.parse_args()

    mhs = ['160','180','200','250','300','350','400']
    mDM = ['100','150','200','300']
    mZp = ['200','300','400','500','600','700','800','900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200','2300','2400','2500']
    
    for hs in mhs:
        for DM in mDM:
            for Zp in mZp:
                with open(args.inputDir + '/datacard_DH_mhs_' + hs + '_mx_' + DM + '_mZp_' + Zp + '_combined.txt', 'r') as input_file, open(args.inputDir + '/datacard_DH_mhs_' + hs + '_mx_' + DM + '_mZp_' + Zp + '_combined_corr.txt', 'w') as output_file:
                    for line in input_file:
                        if 'rateParam' in line.strip():
                            output_file.write(line.replace('1.0000', '1.0000  [0.1,10]'))
                        else:
                            output_file.write(line)


    # mDM = ['150','200']
    # mhs = ['300','400']
    # mZp = ['400','500','800','1000','1200','1500']

    # for DM in mDM:
    #     for hs in mhs:
    #         if DM == '150' and hs == '400':
    #             continue
    #         for Zp in mZp:
    #             if DM == '200' and Zp == '400':
    #                 continue
    #             if DM == '200' and hs == '400' and int(Zp) > 1000:
    #                 continue
    #             with open(args.inputDir + '/datacard_DH_mhs_' + hs + '_mx_' + DM + '_mZp_' + Zp + '_combined.txt', 'r') as input_file, open(args.inputDir + '/datacard_DH_mhs_' + hs + '_mx_' + DM + '_mZp_' + Zp + '_combined_corr.txt', 'w') as output_file:
    #                 for line in input_file:
    #                     if 'rateParam' in line.strip():
    #                         output_file.write(line.replace('1.0000', '1.0000  [0.1,10]'))
    #                     else:
    #                         output_file.write(line)



    # mDM = ['300']
    # mhs = ['160','180','200','300']
    # mZp = ['800','1000','1200','1500','2000','2500']


    # for DM in mDM:
    #     for hs in mhs:
    #         for Zp in mZp:
    #             if hs == '300' and int(Zp) > 1200:
    #                 continue
    #             with open(args.inputDir + '/datacard_DH_mhs_' + hs + '_mx_' + DM + '_mZp_' + Zp + '_combined.txt', 'r') as input_file, open(args.inputDir + '/datacard_DH_mhs_' + hs + '_mx_' + DM + '_mZp_' + Zp + '_combined_corr.txt', 'w') as output_file:
    #                 for line in input_file:
    #                     if 'rateParam' in line.strip():
    #                         output_file.write(line.replace('1.0000', '1.0000  [0.1,10]'))
    #                     else:
    #                         output_file.write(line)

    # mA = ['200', '400', '500', '600']
    # for A in mA:

    #     with open(args.inputDir + '/datacard_2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_' + A +'_ma_150_combined.txt', 'r') as input_file, open(args.inputDir + '/datacard_2HMDa__gg_sinp_0p35_tanb_1p0_mXd_10_MA_' + A +'_ma_150_combined_corr.txt', 'w') as output_file:
    #         for line in input_file:
    #             if 'rateParam' in line.strip():
    #                 output_file.write(line.replace('1.0000', '1.0000  [0.1,10]'))
    #             else:
    #                 output_file.write(line)




    # sintheta = ['0p35', '0p7']
    # tanbeta = ['0p5', '1p0', '1p5', '2p0', '4p0', '8p0']

    # for theta in sintheta:
    #     for beta in tanbeta:
    #         with open(args.inputDir + '/datacard_2HMDa__gg_sinp_' + theta  + '_tanb_' + beta  + '_mXd_10_MA_300_ma_150_combined.txt', 'r') as input_file, open(args.inputDir + '/datacard_2HMDa__gg_sinp_' + theta  + '_tanb_' + beta  + '_mXd_10_MA_300_ma_150_combined_corr.txt', 'w') as output_file:
    #             for line in input_file:
    #                 if 'rateParam' in line.strip():
    #                     output_file.write(line.replace('1.0000', '1.0000  [0.1,10]'))
    #                 else:
    #                     output_file.write(line)