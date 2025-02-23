"""
reference: https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData

pileupCalc.py ex.:
JSON="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt"
PUJSON="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt"
pileupCalc.py -i $JSON --inputLumiJSON $PUJSON  --calcMode true --minBiasXsec 69200 --maxPileupBin 100 --numPileupBins 100  --pileupHistName=PUpileupNominal pileupNominal.root

pileup bin starts from N TrueInteractions = 1 (1st bin content -> N TrueInteractions = 1)
"""
nomXsec = 69200.0
uncertainty = 0.05
#uncertainty = 0.046
nBins = 100
maxBin = 100

cal16=True
cal17=True
cal18=True

#from SimGeneral.MixingModule.mix_2016_PoissonOOTPU_HighPUTrains_Fill5412_cfi import mix as mc16
#from SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi import mix as mc16
from SimGeneral.MixingModule.mix_2016_25ns_Moriond17MC_PoissonOOTPU_cfi import mix as mc16
nMC16 = mc16.input.nbPileupEvents.probValue

from SimGeneral.MixingModule.mix_2017_25ns_WinterMC_PUScenarioV1_PoissonOOTPU_cfi import mix as mc17
#from SimGeneral.MixingModule.mix_2017_25ns_UltraLegacy_PoissonOOTPU_cfi import mix as mc17
nMC17 = mc17.input.nbPileupEvents.probValue

#from SimGeneral.MixingModule.mix_2018_25ns_JuneProjectionFull18_PoissonOOTPU_cfi import mix as mc18
#from SimGeneral.MixingModule.mix_2018_25ns_ProjectedPileup_PoissonOOTPU_cfi import mix as mc18
from SimGeneral.MixingModule.mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi import mix as mc18
nMC18 = mc18.input.nbPileupEvents.probValue

PUJSON16 = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt"
PUJSON17 = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PileUp/pileup_latest.txt"
PUJSON18 = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PileUp/pileup_latest.txt"
JSON16 =  "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt"
#JSON17 = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
JSON17 = "./Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt" #trim run2017A and run2017B
JSON18 = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
