# Read Delphes with Coffea!

Whooo! Yeah!

## Installing

Clone this repository, then `python -m pip install -r requirements.txt`. See `example.py` for how you use the NanoEvents schema.

## Running

`python example.py` gives current output like so (lots of warnings for things we haven't handled yet):

```
$ python example.py
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet/GenJet.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Track/Track.Particle as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Tower/Tower.Edges[4] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Tower/Tower.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping EFlowTrack/EFlowTrack.Particle as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping EFlowPhoton/EFlowPhoton.Edges[4] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping EFlowPhoton/EFlowPhoton.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping EFlowNeutralHadron/EFlowNeutralHadron.Edges[4] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping EFlowNeutralHadron/EFlowNeutralHadron.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Photon/Photon.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Electron/Electron.Particle as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Muon/Muon.Particle as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping Jet/Jet.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet02/GenJet02.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet04/GenJet04.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet08/GenJet08.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping GenJet15/GenJet15.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet02/ParticleFlowJet02.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet04/ParticleFlowJet04.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet08/ParticleFlowJet08.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping ParticleFlowJet15/ParticleFlowJet15.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet02/CaloJet02.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet04/CaloJet04.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet08/CaloJet08.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping CaloJet15/CaloJet15.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet02/TrackJet02.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet04/TrackJet04.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet08/TrackJet08.Area as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.FracPt[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.Tau[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.SoftDroppedJet as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.SoftDroppedSubJet1 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.SoftDroppedSubJet2 as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.TrimmedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.PrunedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.SoftDroppedP4[5] as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.Constituents as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.Particles as it is not interpretable by NanoEvents
  warnings.warn(
/Users/kratsg/.pyenv/versions/coffea-delphes/lib/python3.8/site-packages/coffea/nanoevents/mapping/uproot.py:89: UserWarning: Skipping TrackJet15/TrackJet15.Area as it is not interpretable by NanoEvents
  warnings.warn(
ParticleFlowJet02
Tower
TrackJet08
EFlowPhoton
WeightLHEF
ScalarHT
EventLHEF
EFlowTrack
Jet
ParticleFlowJet04
Muon
Photon
CaloJet04
MissingET
EFlowNeutralHadron
GenJet08
GenMissingET
Track
CaloJet02
TrackJet04
CaloJet15
CaloJet08
TrackJet15
GenJet02
Event
TrackJet02
GenJet15
ParticleFlowJet08
ParticleFlowJet15
Electron
Particle
GenJet04
GenJet
[[0.812], [0.771], [3.25], [98.1, 38.4]]
[0.812, 0.771, 3.25, 98.1]
```
