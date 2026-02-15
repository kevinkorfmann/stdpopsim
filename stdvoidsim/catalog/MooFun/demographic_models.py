import msprime
import stdvoidsim

_species = stdvoidsim.get_species("MooFun")
_dark_pop = stdvoidsim.Population(
    id="DarkSideMoon", description="Moon-beasts on the dark side of the moon"
)
_trade_pop = stdvoidsim.Population(
    id="TradeFleet", description="Moon-beast trading fleet in Dreamlands"
)


def _dark_side():
    id = "DarkSideDominion_1C26"
    description = "Single population dark side of the moon model"
    long_description = """
        Single population on the moon's dark side. Three epochs: modern
        slavers (N=45000), expansion from trade routes 5000 gen ago
        (N=10000), ancient lunar origin 50000 gen ago (N=80000).
    """
    populations = [_dark_pop]
    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=5000, initial_size=10000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=50000, initial_size=80000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_dark_side())


def _trade_fleet():
    id = "TradeFleet_2C26"
    description = "Two population moon and Dreamlands trading fleet model"
    long_description = """
        Two populations: dark side homeworld and Dreamlands trading fleet.
        Ancestral N=80000. Split 10000 gen ago. Moon at 45000. Trading
        fleet bottleneck to 500, grow to 15000.
    """
    populations = [_dark_pop, _trade_pop]
    citations = [
        stdvoidsim.Citation(
            author="Lovecraft, H.P.",
            year=1928,
            doi="https://en.wikipedia.org/wiki/Necronomicon",
            reasons={stdvoidsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdvoidsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2000, initial_size=500, population_id=1
            ),
            msprime.MassMigration(time=10000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=10000, initial_size=80000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_trade_fleet())
