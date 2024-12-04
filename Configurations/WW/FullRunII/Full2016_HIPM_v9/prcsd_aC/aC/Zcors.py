# This is is included to make the anomalous coupling configuration more modulare
# and to promote easier verification and editing.

import json

# Putting in XSec_Correction factors for the samples

nGen05 = 498148    
nFilt05 = 168994

nGen57 = 500000
nFilt57 = 16551

nGen71 = 750000
nFilt71 = 16189

nGen1I = 736155
nFilt1I = 4967  

cors = {}

cors['cor05'] = str(nGen05/(nGen05 - nFilt05))
cors['cor57'] = str(nGen57/(nGen57 - nFilt57))
cors['cor71'] = str(nGen71/(nGen71 - nFilt71))
cors['cor1I'] = str(nGen1I/(nGen1I - nFilt1I))

cors['MC_MG_Cor'] = '1.2249011'

with open('./Zcors.json','w') as fl:
    json.dump(cors,fl)
