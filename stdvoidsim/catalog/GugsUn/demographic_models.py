import msprime
import stdvoidsim

_species = stdvoidsim.get_species("GugsUn")
_vault_pop = stdvoidsim.Population(id="VaultDwellers", description="Gugs in the vaults of Zin")
_tower_pop = stdvoidsim.Population(id="TowerGugs", description="Gugs near the Tower of Koth")

def _vault_exile():
    id = "VaultExile_1C26"
    description = "Single population Gug vault exile model"
    long_description = """
        Single population of exiled Gugs. Three epochs: modern vault
        (N=25000), post-banishment bottleneck 3000 gen ago (N=2000),
        surface era before exile 30000 gen ago (N=200000).
    """
    populations = [_vault_pop]
    citations = [stdvoidsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.gug.dem1",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=5e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=25000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=3000, initial_size=2000, population_id=0),
            msprime.PopulationParametersChange(time=30000, initial_size=200000, population_id=0)])

_species.add_demographic_model(_vault_exile())

def _tower_split():
    id = "TowerSplit_2C26"
    description = "Two population vault and Tower of Koth model"
    long_description = """
        Two populations: vault dwellers and Tower of Koth gugs. Ancestral
        N=200000. Split 10000 gen ago. Vault at 25000. Tower bottleneck
        to 500, grow to 10000.
    """
    populations = [_vault_pop, _tower_pop]
    citations = [stdvoidsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.gug.dem2",
        reasons={stdvoidsim.CiteReason.DEM_MODEL})]
    return stdvoidsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=5e-9,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=25000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=10000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=2000, initial_size=500, population_id=1),
            msprime.MassMigration(time=10000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=10000, initial_size=200000, population_id=0)])

_species.add_demographic_model(_tower_split())
