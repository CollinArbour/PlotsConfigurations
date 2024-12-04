# This is is included to make the anomalous coupling configuration more modulare
# and to promote easier verification and editing.

import json

# Putting in XSec_Correction factors for the samples
nGen05 = 995000
nFilt05 = 333926 #v2

nGen57 = 999000
nFilt57 = 33065

nGen71 = 1500000
nFilt71 = 31759

nGen1I = 1500000
nFilt1I = 10415

cors = {}

cors['cor05'] = str(nGen05/(nGen05 - nFilt05))
cors['cor57'] = str(nGen57/(nGen57 - nFilt57))
cors['cor71'] = str(nGen71/(nGen71 - nFilt71))
cors['cor1I'] = str(nGen1I/(nGen1I - nFilt1I))

cors['MC_MG_Cor'] = '1.2249011'

with open('./Zcors.json','w') as fl:
    json.dump(cors,fl)
