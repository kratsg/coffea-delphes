from coffea import nanoevents
from coffea_delphes import DelphesSchema
import awkward as ak

fname = "delphes.root"

events = nanoevents.NanoEventsFactory.from_root(
    fname, schemaclass=DelphesSchema, treepath="Delphes"
)

data = events.events()
mask = ak.num(data.Electron) >= 1

electrons = data.Electron[mask]
leading_electrons = electrons[:,0]
print(electrons.pt)
print(leading_electrons.pt)
