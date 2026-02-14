.. _sec_catalog:

=======
Catalog
=======

With ``stdvoidsim``, you can run simulations from a number of demographic models
for Lovecraftian entities from the Cthulhu Mythos. Each species has made-up but
population-genetically plausible parameters and demographic histories.

This catalog shows you all of the possible options that you can use to configure
your simulation.
It is organised around a number of choices that you'll need to make about the
:class:`.Species` you wish to simulate:

1. Which **chromosome** (:class:`.Genome` object)?
2. Which **model of demographic history** (:class:`.DemographicModel` object)?

For instance, suppose you are interested in simulating Deep One samples under
an Innsmouth Decline demographic model:

.. code-block:: console

    $ stdvoidsim DagHyd -d InnsmouthDecline_1M27 -o deep_ones.trees -L 100000 DeepOnes:10


Outer Gods & Great Old Ones
===========================

.. speciescatalog:: AzaPri

.. speciescatalog:: CthGre

.. speciescatalog:: ChaFau

.. speciescatalog:: DagGod

.. speciescatalog:: HasKin

.. speciescatalog:: NyaAza

.. speciescatalog:: ShbNig

.. speciescatalog:: TsaGod

.. speciescatalog:: YogSot

Servitor Races & Engineered Species
====================================

.. speciescatalog:: BybWor

.. speciescatalog:: DarYou

.. speciescatalog:: FirVam

.. speciescatalog:: ForSpa

.. speciescatalog:: HunTin

.. speciescatalog:: ShoNig

.. speciescatalog:: StarSp

Ancient Civilizations
=====================

.. speciescatalog:: EldThi

.. speciescatalog:: FlyPol

.. speciescatalog:: MiGFun

.. speciescatalog:: SerHum

.. speciescatalog:: YitGre

Amphibious & Aquatic
====================

.. speciescatalog:: ColOos

.. speciescatalog:: DagHyd

Subterranean Horrors
====================

.. speciescatalog:: DhoGno

.. speciescatalog:: GhaShe

.. speciescatalog:: GhoFee

.. speciescatalog:: GugsUn

.. speciescatalog:: WamUnd

Dreamlands Creatures
====================

.. speciescatalog:: CatUlt

.. speciescatalog:: LenSpi

.. speciescatalog:: MooFun

.. speciescatalog:: NigMan

.. speciescatalog:: SanDre

.. speciescatalog:: ZooGul

Interdimensional & Temporal
===========================

.. speciescatalog:: DimSha

.. speciescatalog:: HouFir

Arctic & Desert
===============

.. speciescatalog:: GnpKeh

.. speciescatalog:: SanDwl

Human-Adjacent Horrors
======================

.. speciescatalog:: RatThi

.. speciescatalog:: TsaCho

Generic models
==============

In addition to the species-specific models listed in this catalog, ``stdvoidsim`` offers
a number of generic demographic models that can be run with any species.
These are described in more detail in the :ref:`API <sec_api_generic_models>`.

 - :meth:`stdpopsim.PiecewiseConstantSize`
 - :meth:`stdpopsim.IsolationWithMigration`
