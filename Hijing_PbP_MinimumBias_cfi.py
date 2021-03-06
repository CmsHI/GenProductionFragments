import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("HijingGeneratorFilter",
                         rotateEventPlane = cms.bool(True),
                         frame = cms.string('CMS     '),
                         targ = cms.string('A       '),
                         izp = cms.int32(1),
                         bMin = cms.double(0),
                         izt = cms.int32(82),
                         proj = cms.string('P       '),
                         comEnergy = cms.double(5023.0),
                         iat = cms.int32(208),
                         bMax = cms.double(15),
                         iap = cms.int32(1)
                         )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('HIJING generator'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/HI/Hijing_PbP_MinimumBias_cfi.py,v $')
    )

