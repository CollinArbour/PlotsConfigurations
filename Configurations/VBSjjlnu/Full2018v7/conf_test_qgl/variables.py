
res_cuts = [ c for c in cuts if 'res' in c]
boost_cuts = [ c for c in cuts if 'boost' in c]


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


variables['tree'] = {
    'tree': {
            'vbs_0_qgl_res':'vbs_0_qgl_res',
            'vbs_1_qgl_res':'vbs_1_qgl_res',
            'vjet_0_qgl_res':'vjet_0_qgl_res',
            'vjet_1_qgl_res':'vjet_1_qgl_res',
            'vbs_0_eta': 'vbs_0_eta',
            'vbs_1_eta': 'vbs_1_eta',
            'vjet_0_eta': 'vjet_0_eta',
            'vjet_1_eta': 'vjet_1_eta',
            'vbs_0_pt': 'vbs_0_pt',
            'vbs_1_pt': 'vbs_1_pt',
            'vjet_0_pt': 'vjet_0_pt',
            'vjet_1_pt': 'vjet_1_pt',
        },
}

variables['vbs_0_qgl_res'] = {  'name': 'vbs_0_qgl_res',
                        'range': (44,-0.1,1.),
                        'xaxis': 'Qgl VBS 0 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }

variables['vbs_1_qgl_res'] = {  'name': 'vbs_1_qgl_res',
                        'range': (44,-0.1,1.),
                        'xaxis': 'Qgl VBS 1 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }

variables['vjet_0_qgl_res'] = {  'name': 'vjet_0_qgl_res',
                        'range': (44,-0.1,1.),
                        'xaxis': 'Qgl Vjet 0 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }

variables['vjet_1_qgl_res'] = {  'name': 'vjet_1_qgl_res',
                        'range': (44,-0.1,1.),
                        'xaxis': 'Qgl Vjet 1 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }


variables['vbs_0_qgl_res_morebins'] = {  'name': 'vbs_0_qgl_res',
                        'range': (77,0.1,1.),
                        'xaxis': 'Qgl VBS 0 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }

variables['vbs_1_qgl_res_morebins'] = {  'name': 'vbs_1_qgl_res',
                        'range': (77,-0.1,1.),
                        'xaxis': 'Qgl VBS 1 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }

variables['vjet_0_qgl_res_morebins'] = {  'name': 'vjet_0_qgl_res',
                        'range': (77,-0.1,1.),
                        'xaxis': 'Qgl Vjet 0 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }

variables['vjet_1_qgl_res_morebins'] = {  'name': 'vjet_1_qgl_res',
                        'range': (77,-0.1,1.),
                        'xaxis': 'Qgl Vjet 1 jet',
                        'fold': 3,
                        'cuts': res_cuts
                }