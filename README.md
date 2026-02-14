# stdvoidsim

A community-maintained library of population genetic simulation models for
**Lovecraftian entities and eldritch horrors**.

Built on the [stdpopsim](https://github.com/popsim-consortium/stdpopsim) framework,
`stdvoidsim` provides fictional but population-genetically plausible demographic models
for creatures from H.P. Lovecraft's Cthulhu Mythos. All models use realistic population
genetic parameters and are fully simulatable with `msprime` and `SLiM`.

## Available Species

| ID | Species | Common Name | Pop Size | Gen Time |
|--------|-------------------------------|--------------------------|----------|----------|
| CthGre | *Cthulhu greatoldone* | Great Cthulhu | 500 | 10,000 yr |
| NyaAza | *Nyarlathotep azathothspawn* | Crawling Chaos | 1,000 | 1 yr |
| ShoNig | *Shoggoth nigrumplasma* | Shoggoth | 100,000 | 0.5 yr |
| YogSot | *Yogsothoth dimensionalis* | The Key and the Gate | 10 | 100,000 yr |
| DagHyd | *Dagonus hydridae* | Deep One | 50,000 | 100 yr |
| MiGFun | *Migo fungoides* | Fungi from Yuggoth | 500,000 | 5 yr |
| HasKin | *Hastur carcosensis* | King in Yellow | 2,000 | 50 yr |
| EldThi | *Elderium antarcticae* | Elder Thing | 10,000 | 1,000 yr |
| GhoFee | *Ghoulish necrophagus* | Ghoul | 30,000 | 20 yr |
| BybWor | *Byakhee voidwing* | Byakhee | 200,000 | 10 yr |

## Quick Start

```python
import stdpopsim

# Get the Deep Ones species
species = stdpopsim.get_species("DagHyd")

# Use the Innsmouth Decline demographic model
model = species.get_demographic_model("InnsmouthDecline_1M27")

# Set up a contig (chromosome 1, 10Mb chunk)
contig = species.get_contig("1", length=10_000_000)

# Simulate with msprime
engine = stdpopsim.get_engine("msprime")
ts = engine.simulate(model, contig, {"DeepOnes": 50})
```

## Installation

```bash
pip install stdvoidsim
```

Or for development:

```bash
git clone https://github.com/your-org/stdvoidsim.git
cd stdvoidsim
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
