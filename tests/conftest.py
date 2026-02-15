"""
Pytest configuration for stdvoidsim.
"""

import pathlib

# Species IDs in the stdvoidsim catalog (Lovecraftian only)
CATALOG_SPECIES = {
    "AzaPri",
    "BybWor",
    "CatUlt",
    "ChaFau",
    "ColOos",
    "CthGre",
    "DarYou",
    "DagGod",
    "DagHyd",
    "DhoGno",
    "DimSha",
    "EldThi",
    "FirVam",
    "FlyPol",
    "ForSpa",
    "GhaShe",
    "GhoFee",
    "GnpKeh",
    "GugsUn",
    "HasKin",
    "HouFir",
    "HunTin",
    "LenSpi",
    "MiGFun",
    "MooFun",
    "NigMan",
    "NyaAza",
    "RatThi",
    "SanDre",
    "SanDwl",
    "SerHum",
    "ShoNig",
    "ShbNig",
    "StarSp",
    "TsaCho",
    "TsaGod",
    "WamUnd",
    "YitGre",
    "YogSot",
    "ZooGul",
}

# Test modules that target species not in the catalog (from stdpopsim); skip them.
SKIP_SPECIES_TEST_MODULES = {
    "test_AraTha",
    "test_BosTau",
    "test_DroMel",
    "test_DroSec",
    "test_EscCol",
    "test_HomSap",
    "test_PanTro",
    "test_RatNor",
    "test_StrAga",
    "test_SusScr",
}


def _catalog_has_species():
    """Species IDs that must be in catalog for test_cli / test_slim_engine."""
    import stdvoidsim

    return {s.id for s in stdvoidsim.all_species()}


def pytest_ignore_collect(collection_path, config):
    """Skip test modules for species not in the catalog (e.g. test_HomSap.py)."""
    path = pathlib.Path(collection_path)
    if path.suffix == ".py" and path.name.startswith("test_"):
        stem = path.stem
        if stem in SKIP_SPECIES_TEST_MODULES:
            return True
        # These modules require HomSap (and EscCol for cli/slim_engine)
        if stem in ("test_cli", "test_slim_engine"):
            catalog_ids = _catalog_has_species()
            if "HomSap" not in catalog_ids or "EscCol" not in catalog_ids:
                return True
        if stem in ("test_genomes", "test_genetic_maps", "test_annotations"):
            catalog_ids = _catalog_has_species()
            if "HomSap" not in catalog_ids:
                return True
        if stem in ("test_maintenance", "test_dfes"):
            return False
        # test_SpeciesId.py -> SpeciesId (dynamic species tests)
        if len(stem) > 5:
            maybe_species = stem[5:]
            if maybe_species not in CATALOG_SPECIES and maybe_species[0].isupper():
                return True
    return False
