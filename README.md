# stdvoidsim

A community-maintained library of population genetic simulation models for
**Lovecraftian entities and eldritch horrors**.

Built on the [stdpopsim](https://github.com/popsim-consortium/stdpopsim) framework,
`stdvoidsim` provides fictional but population-genetically plausible demographic models
for creatures from H.P. Lovecraft's Cthulhu Mythos. All models use realistic population
genetic parameters and are fully simulatable with `msprime` and `SLiM`.

**40 species, 80 demographic models.**

## Available Species

### Outer Gods & Great Old Ones

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| AzaPri | *Azathoth primordia* | Blind Idiot God | 1 | 1M yr | 2 |
| CthGre | *Cthulhu greatoldone* | Great Cthulhu | 500 | 10K yr | 4 |
| DagGod | *Dagonus maximus* | Father Dagon | 50 | 50K yr | 4 |
| HasKin | *Hastur carcosensis* | King in Yellow | 2,000 | 50 yr | 2 |
| NyaAza | *Nyarlathotep azathothspawn* | Crawling Chaos | 1,000 | 1 yr | 2 |
| ShbNig | *Shubniggurath fertilitas* | Black Goat of the Woods | 100,000 | 25 yr | 2 |
| TsaGod | *Tsathoggua somnolentis* | Tsathoggua | 100 | 50K yr | 2 |
| YogSot | *Yogsothoth dimensionalis* | The Key and the Gate | 10 | 100K yr | 2 |
| ChaFau | *Chaugnarus faugnis* | Chaugnar Faugn | 200 | 10K yr | 2 |

### Servitor Races & Engineered Species

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| ShoNig | *Shoggoth nigrumplasma* | Shoggoth | 100,000 | 0.5 yr | 6 |
| StarSp | *Starspawn cthulhidae* | Star-Spawn of Cthulhu | 10,000 | 5K yr | 4 |
| DarYou | *Obscurus silvanus* | Dark Young | 35,000 | 50 yr | 3 |
| ForSpa | *Informis generatus* | Formless Spawn | 25,000 | 10 yr | 2 |
| HunTin | *Venator obscurus* | Hunting Horror | 15,000 | 20 yr | 2 |
| FirVam | *Igneus vampirus* | Fire Vampire | 1M | 0.01 yr | 1 |
| BybWor | *Byakhee voidwing* | Byakhee | 200,000 | 10 yr | 2 |

### Ancient Civilizations

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| EldThi | *Elderium antarcticae* | Elder Thing | 10,000 | 1K yr | 2 |
| YitGre | *Yithianus temporalis* | Great Race of Yith | 50,000 | 500 yr | 2 |
| FlyPol | *Polypus volantis* | Flying Polyp | 20,000 | 2K yr | 2 |
| SerHum | *Serpentis valusiensis* | Serpent Person | 40,000 | 50 yr | 2 |
| MiGFun | *Migo fungoides* | Fungi from Yuggoth | 500,000 | 5 yr | 2 |

### Amphibious & Aquatic

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| DagHyd | *Dagonus hydridae* | Deep One | 50,000 | 100 yr | 2 |
| ColOos | *Chromatis extraspatiala* | Colour Out of Space | 10,000 | 0.1 yr | 1 |

### Subterranean Horrors

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| GhoFee | *Ghoulish necrophagus* | Ghoul | 30,000 | 20 yr | 2 |
| GugsUn | *Gugus underworldis* | Gug | 25,000 | 30 yr | 2 |
| GhaShe | *Ghastus cavernicola* | Ghast | 80,000 | 3 yr | 2 |
| DhoGno | *Dholos subterraneus* | Dhole | 15,000 | 200 yr | 2 |
| WamUnd | *Degeneratus subterraneus* | Wamp | 20,000 | 10 yr | 2 |

### Dreamlands Creatures

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| NigMan | *Nightgauntus mantaformis* | Nightgaunt | 75,000 | 5 yr | 2 |
| SanDre | *Shantakus dreamlandis* | Shantak | 60,000 | 15 yr | 2 |
| MooFun | *Lunaris bestialis* | Moon-Beast | 45,000 | 8 yr | 2 |
| ZooGul | *Zoogus sylvaticus* | Zoog | 500,000 | 2 yr | 2 |
| CatUlt | *Felis ultharensis* | Cat of Ulthar | 100,000 | 5 yr | 2 |
| LenSpi | *Araneus lengensis* | Leng Spider | 20,000 | 10 yr | 2 |

### Interdimensional & Temporal

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| HouFir | *Houndus tindalosi* | Hound of Tindalos | 5,000 | 500 yr | 2 |
| DimSha | *Dimensius shambleris* | Dimensional Shambler | 3,000 | 100 yr | 2 |

### Arctic & Desert

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| GnpKeh | *Gnophkehus arcticus* | Gnoph-Keh | 12,000 | 40 yr | 2 |
| SanDwl | *Arenicola abyssalis* | Sand Dweller | 40,000 | 15 yr | 2 |

### Human-Adjacent Horrors

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| TsaCho | *Tsathoggua choriensis* | Tcho-Tcho | 70,000 | 25 yr | 2 |
| RatThi | *Rattus magicus* | Rat-Thing | 50,000 | 1 yr | 2 |

## Quick Start

```python
import stdpopsim

# Get the Shoggoth species (hexaploid engineered servitors)
species = stdpopsim.get_species("ShoNig")

# Use the Antarctic Revolt demographic model
model = species.get_demographic_model("AntarcticRevolt_1D31")

# Set up a generic contig of 100kb
contig = species.get_contig(length=100_000)

# Simulate with msprime
engine = stdpopsim.get_engine("msprime")
ts = engine.simulate(model, contig, samples={"Antarctic": 20}, seed=42)

print(f"Trees: {ts.num_trees}, Mutations: {ts.num_mutations}")
```

## CLI Usage

```bash
# List all available species
stdvoidsim --help

# Simulate 10 Deep One samples under the Innsmouth Decline model
stdvoidsim DagHyd -d InnsmouthDecline_1M27 -o deep_ones.trees -L 100000 DeepOnes:10

# Simulate Shoggoth rebellion scenario
stdvoidsim ShoNig -d AntarcticRevolt_1D31 -o shoggoths.trees -L 50000 Antarctic:20
```

## Installation

```bash
pip install -e .
```

## Design Philosophy

Each species has:
- **Made-up but internally consistent genome**: chromosome counts, lengths, ploidy,
  mutation rates, and recombination rates chosen to reflect the creature's biology
- **Demographic models**: population size changes, bottlenecks, splits, and migrations
  that tell a story consistent with the Mythos lore
- **Simulatable parameters**: all values are chosen so that simulations complete in
  reasonable time and produce meaningful coalescent trees

The models are designed to be useful for testing population genetic inference methods
on non-standard demographic scenarios (extreme bottlenecks, very small populations,
polyploidy, highly asymmetric migration, etc.).

## Citation

This project is a fork of [stdpopsim](https://github.com/popsim-consortium/stdpopsim).
If you use the simulation framework, please cite:

* [Adrion, et al. (2020)](https://doi.org/10.7554/eLife.54967)
* [Lauterbur, et al. (2023)](https://doi.org/10.7554/eLife.84874)

*"Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn."*
