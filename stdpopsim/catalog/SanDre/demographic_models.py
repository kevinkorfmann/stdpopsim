import msprime
import stdpopsim

_species = stdpopsim.get_species("SanDre")
_kadath_pop = stdpopsim.Population(id="KadathPeaks", description="Shantaks nesting on Kadath peaks")
_plateau_pop = stdpopsim.Population(id="LengPlateau", description="Shantaks of the Plateau of Leng")

def _kadath_nesting():
    id = "KadathNesting_1C26"
    description = "Single population Kadath nesting colony model"
    long_description = """
        Single population on Kadath peaks. Three epochs: modern flock
        (N=60000), taming by moon-beasts 3000 gen ago (N=20000),
        wild ancestral flock 30000 gen ago (N=150000).
    """
    populations = [_kadath_pop]
    citations = [stdpopsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.shantak.dem1",
        reasons={stdpopsim.CiteReason.DEM_MODEL})]
    return stdpopsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=60000, metadata=populations[0].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=3000, initial_size=20000, population_id=0),
            msprime.PopulationParametersChange(time=30000, initial_size=150000, population_id=0)])

_species.add_demographic_model(_kadath_nesting())

def _leng_split():
    id = "LengSplit_2C26"
    description = "Two population Kadath and Leng shantak model"
    long_description = """
        Two populations: Kadath peaks and Leng plateau. Ancestral N=150000.
        Split 10000 gen ago. Kadath at 60000. Leng bottleneck to 300,
        grow to 25000.
    """
    populations = [_kadath_pop, _plateau_pop]
    citations = [stdpopsim.Citation(author="Carter et al.", year=1926,
        doi="https://doi.org/10.1666/void.shantak.dem2",
        reasons={stdpopsim.CiteReason.DEM_MODEL})]
    return stdpopsim.DemographicModel(
        id=id, description=description, long_description=long_description,
        populations=populations, citations=citations,
        generation_time=_species.generation_time, mutation_rate=1.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(initial_size=60000, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(initial_size=25000, metadata=populations[1].asdict())],
        demographic_events=[
            msprime.PopulationParametersChange(time=2000, initial_size=300, population_id=1),
            msprime.MassMigration(time=10000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(time=10000, initial_size=150000, population_id=0)])

_species.add_demographic_model(_leng_split())
