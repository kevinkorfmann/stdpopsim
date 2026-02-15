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

**Azathoth** (the Blind Idiot God) is the supreme deity of the Cthulhu Mythos,
dwelling at the center of ultimate chaos. It is a boundless, amorphous entity
of colossal size, described as a "nuclear chaos" surrounded by a retinue of
mindless dancers and the thin monotonous piping of a demonic flute. Azathoth is
effectively the ruler of the Outer Gods, yet is blind and idiotic, unaware of
its own existence or the cosmos it spawned. All of reality is said to be merely
Azathoth's dream. First appearing in Lovecraft's fiction in 1922, Azathoth
embodies the ultimate horror of a universe governed by mindless, purposeless
forces.

AzaPri — Azathoth primordia
---------------------------

.. speciescatalog:: AzaPri

**Great Cthulhu** is perhaps the most iconic entity of the Mythos, a cosmic
being of immense power who lies "dead but dreaming" in the sunken city of
R'lyeh, deep beneath the Pacific Ocean. Described as a gigantic creature with
an octopoid head, dragon-like wings, and a massive humanoid body, Cthulhu
stands hundreds of meters tall. It communicates telepathically, sending dreams
and visions to sensitive minds across the globe. Cthulhu is worshipped by
hidden cults worldwide who chant *"Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl
fhtagn"* -- "In his house at R'lyeh, dead Cthulhu waits dreaming." First
appeared in "The Call of Cthulhu" (1928).

CthGre — Great Cthulhu
----------------------

.. speciescatalog:: CthGre

**Chaugnar Faugn** (the Feeder) is a Great Old One resembling a vampiric
elephant-like humanoid horror. Created by Frank Belknap Long in *The Horror
from the Hills*, the entity has a proboscidean trunk ending in a horrible
lamprey-like mouth used to drain victims of blood and life essence. Though
often illustrated as an anthropomorphic elephant, it is actually described as
reptilian in nature, bearing only superficial resemblance to an elephant. It
stands roughly eight feet tall with webbed, tentacled ears and enormous
translucent tusks. When hungry, Chaugnar moves with surprising speed. Its
servitors, the Miri Nigri, are the progenitors of the Tcho-Tcho people through
hybridization with humans.

ChaFau — Chaugnar Faugn
-----------------------

.. speciescatalog:: ChaFau

**Father Dagon** is an immensely large and powerful Deep One, worshipped as a
deity by both the Deep Ones and certain coastal human cults. Together with
Mother Hydra, Dagon rules over the Deep One civilization from the depths of the
ocean. Described as a colossal fish-frog hybrid towering over even the largest
Deep Ones, Dagon is ancient beyond human reckoning. Lovecraft introduced Dagon
in his 1917 short story "Dagon," one of his earliest tales, in which a
shipwrecked sailor encounters the titanic creature on a newly risen island of
black, slimy mud.

DagGod — Father Dagon
---------------------

.. speciescatalog:: DagGod

**Hastur** (the King in Yellow) is an enigmatic Great Old One associated with
entropy, decay, and madness. The entity is connected to the mysterious play
*The King in Yellow*, a forbidden text that drives readers to insanity. Hastur
dwells near the star Aldebaran, close to the dark city of Carcosa by the shores
of the Lake of Hali. Those who speak Hastur's name risk drawing its attention.
Originally created by Ambrose Bierce and developed by Robert W. Chambers,
Hastur was later incorporated into the Cthulhu Mythos by Lovecraft and
especially August Derleth, who elevated Hastur to a Great Old One rivaling
Cthulhu.

HasKin — King in Yellow
-----------------------

.. speciescatalog:: HasKin

**Nyarlathotep** (the Crawling Chaos) is unique among the Outer Gods in that it
actively interacts with humanity, taking on a thousand different forms. Unlike
the other Outer Gods, Nyarlathotep appears to be fully sentient and even enjoys
spreading madness and destruction. Among its many avatars are the Black Pharaoh,
the Haunter of the Dark, and a tall, swarthy man who walks among mortals. It
serves as the messenger and soul of the Outer Gods, carrying out their will on
Earth. First mentioned by Lovecraft in a 1920 prose poem, Nyarlathotep appears
in numerous stories and is one of Lovecraft's most developed creations.

NyaAza — Crawling Chaos
------------------------

.. speciescatalog:: NyaAza

**Shub-Niggurath** (the Black Goat of the Woods with a Thousand Young) is an
Outer God associated with fertility, growth, and hideous fecundity. Though
never directly described by Lovecraft, Shub-Niggurath is referenced frequently
in incantations and rituals. It is a perverse fertility deity, spawning vast
numbers of monstrous offspring known as the Dark Young. The entity exists in a
cloudy, forested dimension and is worshipped by cults that invoke it with the
chant *"Ia! Shub-Niggurath!"* Lovecraft first mentioned Shub-Niggurath in
"The Last Test" (1928) and referenced it in several subsequent stories.

ShbNig — Black Goat of the Woods
---------------------------------

.. speciescatalog:: ShbNig

**Tsathoggua** is a Great Old One originally created by Clark Ashton Smith,
later adopted into the Cthulhu Mythos by Lovecraft. Described as a furry,
toad-like entity with sleepy eyes and a bat-like visage, Tsathoggua dwells in
lightless caverns beneath Mount Voormithadreth in Hyperborea (and later
beneath North America). It is notably lazy and slothful, preferring to lie in
torpor and wait for sacrifices to be brought to it. Despite its apparent
lethargy, it is immensely powerful. Its worship predates humanity, having been
venerated by the Voormis and other prehuman races. First appeared in Smith's
"The Tale of Satampra Zeiros" (1931).

TsaGod — Tsathoggua
-------------------

.. speciescatalog:: TsaGod

**Yog-Sothoth** (the Key and the Gate) is an Outer God that exists
simultaneously in all of time and space, coterminous with all things. It
appears as a conglomeration of iridescent, ever-shifting spheres or globes. As
the "Key and the Gate," Yog-Sothoth is the guardian of the threshold between
dimensions, and those who seek to open the way between worlds must deal with it.
It knows all and sees all, past, present, and future. Unlike Azathoth, it is
fully cognizant. In "The Dunwich Horror" (1929), it is revealed as the father
of the monstrous Wilbur Whateley and his invisible twin. Yog-Sothoth is one of
the most powerful entities in the Mythos.

YogSot — Yog-Sothoth
--------------------

.. speciescatalog:: YogSot

Servitor Races & Engineered Species
====================================

**Byakhee** are interstellar servitor creatures associated with Hastur and the
King in Yellow. They can fly through space and between dimensions, carrying
riders through the void. Described as a composite creature with bat-like wings,
insectoid features, and a vaguely avian body, the Byakhee are not native to
Earth. They possess an organ containing a substance called "space-mead" that
allows them to survive the vacuum and cold of interstellar space. They can be
summoned on certain nights using particular rituals. First described by August
Derleth, the Byakhee serve as steeds for those traveling to Carcosa or other
far-flung cosmic destinations.

BybWor — Byakhee
-----------------

.. speciescatalog:: BybWor

**Dark Young of Shub-Niggurath** are monstrous tree-like entities spawned by
the Outer God Shub-Niggurath. They appear as enormous, black, ropy, tentacled
masses with multiple goat-like hooves at their bases, resembling a nightmarish
fusion of tree and animal. They stand roughly 20 feet tall. Despite their
plant-like appearance, they are intelligent and serve as intermediaries between
Shub-Niggurath and her worshippers. Dark Young inhabit dark forests and
woodlands, and are summoned during rituals to the Black Goat. They emit a
sickly sweet smell and crush victims beneath their hooves or grasp them with
their tentacles.

DarYou — Dark Young
--------------------

.. speciescatalog:: DarYou

**Fire Vampires** are living extensions of the cosmic entity Fthaggua, created
by Donald Wandrei for "The Fire Vampires" and later incorporated into the
Cthulhu Mythos. They appear as reddish electrical discharges resembling
lightning, traveling the cosmos aboard the interstellar comet Ktynga. Fire
Vampires feast upon the life energy and memories of sentient creatures, causing
their victims to burst into flames during the feeding process. Their leader,
Fthaggua, appears as a great flickering ball of cold blue flame and serves as
high priest of Cthugha. The knowledge accumulated from slain beings allows
Fthaggua to better locate and hunt intelligent civilizations across the cosmos.

FirVam — Fire Vampire
----------------------

.. speciescatalog:: FirVam

**Formless Spawn** are the amorphous servitors of Tsathoggua, dwelling in the
lightless caverns beneath Mount Voormithadreth and other subterranean locations.
They are black, protoplasmic entities that can assume virtually any shape, from
tentacled horrors to serpentine forms. In their natural state, they appear as
pools of living blackness. Unlike shoggoths, they are naturally occurring beings
rather than engineered creatures. Formless Spawn guard the sleeping form of
Tsathoggua and attack anything that approaches their master without proper
obeisance. They were first described by Clark Ashton Smith in "The Tale of
Satampra Zeiros" (1931).

ForSpa — Formless Spawn
------------------------

.. speciescatalog:: ForSpa

**Hunting Horrors** are nightmarish serpentine creatures that serve
Nyarlathotep. They resemble enormous, jet-black serpents or worms with bat-like
wings, and their forms seem to shift and writhe in a way that defies clear
perception. They pursue their prey relentlessly through the skies and even
through the void between worlds. Hunting Horrors are vulnerable to light,
particularly sunlight, which can destroy them. They are most commonly
encountered in the Dreamlands, where they hunt on behalf of the Crawling Chaos.
Lovecraft referenced these creatures in *The Dream-Quest of Unknown Kadath*
(1927), where protagonist Randolph Carter encounters them in the skies.

HunTin — Hunting Horror
------------------------

.. speciescatalog:: HunTin

**Shoggoths** are massive amoeba-like creatures originally bioengineered by the
Elder Things as versatile construction workers and servants. Described as
protoplasmic, iridescent black masses roughly 15 feet across, shoggoths can
form any organ, limb, or sensory apparatus at will. Multiple luminous green
eyes float on their surfaces. Originally mindless, the shoggoths gradually
developed intelligence over millions of years and eventually revolted against
their Elder Thing masters -- a catastrophic rebellion that contributed to the
decline of Elder Thing civilization. Their cry of *"Tekeli-li!"* is one of the
most chilling sounds in the Mythos. First described in *At the Mountains of
Madness* (1936).

ShoNig — Shoggoth
------------------

.. speciescatalog:: ShoNig

**Star-Spawn of Cthulhu** are gigantic octopoid beings that closely resemble
Great Cthulhu himself, though smaller in stature. They accompanied Cthulhu when
he descended from the stars to Earth, and helped build the cyclopean city of
R'lyeh. When R'lyeh sank beneath the Pacific, most Star-Spawn were trapped
alongside Cthulhu in his deathless slumber. However, some are believed to still
roam the deepest ocean trenches, tended by the Deep Ones. They possess
considerable telepathic abilities and are nearly as resilient as their master.
Lovecraft described them in *At the Mountains of Madness* as the enemies of the
Elder Things in ancient wars for dominion of the Earth.

StarSp — Star-Spawn of Cthulhu
-------------------------------

.. speciescatalog:: StarSp

Ancient Civilizations
=====================

**Elder Things** (also known as the Old Ones or Elder Ones) are the first
extraterrestrial species to have colonized Earth, arriving approximately one
billion years ago. They stand roughly eight feet tall with an oval, barrel-
shaped body exhibiting five-fold radial symmetry. The top appendage is a head
adorned with five eyes, five eating tubes, and a set of cilia for perceiving
without light. The bottom appendage has five limbs used for locomotion. Five
leathery, fan-like retractable wings and five sets of branching tentacles
sprout from their torsos. Their blood is dark green, and their metabolism is
based on carbon dioxide rather than oxygen.

The Elder Things can withstand the pressures of the deepest ocean, survive
interstellar travel, and hibernate for vast epochs. They are amphibious and
reproduce via spores. On Earth they built enormous cities both underwater and
on land, and their civilization was extraordinarily advanced -- they are credited
with creating eukaryotic cells and thus all complex life on Earth. Most
significantly, they bioengineered the shoggoths as construction servants, a
decision that ultimately led to catastrophic revolts. Their society had no
families (since they reproduce via spores) and their architecture reflects their
five-pointed anatomy. First appeared in *At the Mountains of Madness* (1936).

EldThi — Elder Thing
--------------------

.. speciescatalog:: EldThi

**Flying Polyps** are a terrifying race of partially material beings that came
to Earth from space approximately 750 million years ago. They are largely
invisible, betrayed only by the great winds they generate and their five-pointed
footprints. When partially visible, they appear as enormous, semi-transparent,
tentacled horrors with multiple temporary eyes. Flying Polyps wield power over
wind and can generate devastating aerial attacks. They were driven underground
by the Great Race of Yith, who imprisoned them in vast subterranean caverns.
However, the Polyps eventually rose up and destroyed the Great Race's
terrestrial civilization. Lovecraft described them in "The Shadow Out of Time"
(1936).

FlyPol — Flying Polyp
---------------------

.. speciescatalog:: FlyPol

**Mi-Go** (Fungi from Yuggoth) are an extraterrestrial species resembling
crustacean-fungoid hybrids. About five feet long, they have multiple pairs of
limbs, large membranous wings, and a head covered in antennae that constantly
shift color to communicate. Despite their wings, they fly through space using
means unknown. The Mi-Go have established colonies on Pluto (which they call
Yuggoth) and mine rare minerals from Earth's mountains, particularly in Vermont
and the Himalayas. They are scientifically advanced, capable of removing human
brains and placing them in metal cylinders for transport across space. Unlike
most Mythos creatures, Mi-Go are composed of matter not native to our part of
space and cannot be photographed. First appeared in "The Whisperer in Darkness"
(1931).

MiGFun — Fungi from Yuggoth
----------------------------

.. speciescatalog:: MiGFun

**Serpent People** (of Valusia) are an ancient reptilian race that predates
humanity by millions of years. Once the dominant civilization on Earth during
the Paleozoic and Mesozoic eras, they built great cities and mastered powerful
sorcery. Serpent People are shape-shifters capable of assuming human form, and
they have infiltrated human societies throughout history. Their original empire
of Valusia was overthrown by the barbarian king Kull. Despite their decline,
small enclaves persist in hidden subterranean cities. They worship the serpent
god Yig and possess advanced knowledge of alchemy and dark magic. Originally
created by Robert E. Howard in his Kull stories, they were later incorporated
into the Cthulhu Mythos.

SerHum — Serpent Person
------------------------

.. speciescatalog:: SerHum

**Great Race of Yith** are one of the most remarkable species in the Mythos --
not for their physical forms, but for their mastery of time. The Yithians are
minds, not bodies: they project their consciousnesses across time and space,
swapping minds with other beings to inhabit their bodies. On Earth, they
occupied the cone-shaped bodies of a species that lived roughly 250 million
years ago, building a vast library-city in what is now Australia. Their great
library contained knowledge gathered from all eras of history, as visiting
Yithian minds recorded everything they learned. They were eventually destroyed
by the Flying Polyps they had imprisoned underground. The surviving Yithian
minds then projected themselves far into the future, into the bodies of a
beetle-like species. First appeared in "The Shadow Out of Time" (1936).

YitGre — Great Race of Yith
----------------------------

.. speciescatalog:: YitGre

Amphibious & Aquatic
====================

**Colour Out of Space** is an extraterrestrial entity or force of unknowable
nature that arrived on Earth via meteorite. The Colour exists on a part of the
electromagnetic spectrum imperceptible to humans, appearing as an indescribable
hue. After impact, it seeps into soil and water, corrupting the surrounding
environment. Vegetation grows lush but bitter and unwholesome; animals are born
deformed and driven mad; and humans exposed to it slowly wither, their skin
graying and cracking as their life force is drained. The Colour's life cycle
involves germinating, leeching energy from a local ecosystem, and eventually
departing the planet for space. It is perhaps Lovecraft's most alien creation --
a being with no physical form, no clear intelligence, and motives entirely
beyond human comprehension. First appeared in "The Colour Out of Space" (1927).

ColOos — Colour Out of Space
-----------------------------

.. speciescatalog:: ColOos

**Deep Ones** are an amphibious humanoid species that dwell in vast underwater
cities deep in the Earth's oceans. They have a generally humanoid shape but with
fish-like and frog-like features: bulging eyes, wide mouths, gills, scaly skin,
and webbed hands and feet. Deep Ones are effectively immortal, growing larger
and more powerful with age, and only dying through violence or accident. They
worship Father Dagon, Mother Hydra, and Great Cthulhu. Most infamously, Deep
Ones can interbreed with humans, producing hybrid offspring that initially
appear human but gradually undergo a transformation (the "Innsmouth Look") as
they age, eventually becoming fully aquatic. The coastal town of Innsmouth,
Massachusetts was the site of extensive Deep One--human hybridization. First
appeared in "The Shadow Over Innsmouth" (1936).

DagHyd — Deep One
------------------

.. speciescatalog:: DagHyd

Subterranean Horrors
====================

**Dholes** are colossal burrowing worm-like entities of immense size that
inhabit the underworld of the Dreamlands, particularly the Vale of Pnath. They
are so enormous that they can be mistaken for geographical features -- their
bodies stretch for miles through the earth. Dholes are slimy, pale, and
virtually featureless, with gaping maws. They burrow through both the
Dreamlands and the waking world, and their passage leaves great tunnels and
caverns. Little is known about their intelligence or motivations. They are among
the most dangerous creatures in the Dreamlands, and even other Mythos entities
give them a wide berth. Lovecraft mentioned them in *The Dream-Quest of Unknown
Kadath* (1927).

DhoGno — Dhole
---------------

.. speciescatalog:: DhoGno

**Ghasts** are large, kangaroo-like humanoid creatures that inhabit the
underworld caverns of the Dreamlands, particularly the Vaults of Zin. They are
roughly human-sized but with bestial features, including elongated limbs and a
vaguely canine face. Ghasts are savage predators that hunt in packs and will
devour anything they can catch, including ghouls. Their one great weakness is
light -- they cannot endure even the faintest illumination and flee from it in
terror. Ghasts hop rather than walk, using their powerful hind legs. Despite
their ferocity, they are preyed upon by the even more terrible gugs. Lovecraft
described them in *The Dream-Quest of Unknown Kadath* (1927).

GhaShe — Ghast
---------------

.. speciescatalog:: GhaShe

**Ghouls** are humanoid creatures that feed on the flesh of the dead. In
Lovecraft's Mythos, ghouls are not undead but a distinct species -- rubbery,
loathsome beings with canine features, hooved feet, and mold-caked skin. They
dwell in vast warrens of tunnels beneath cemeteries and in the underworld of
the Dreamlands. Remarkably, some ghouls were once human: certain individuals
who develop a taste for human flesh gradually transform over time into ghouls.
Despite their horrific diet and appearance, ghouls possess intelligence and even
a crude society. In *The Dream-Quest of Unknown Kadath*, they prove to be
valuable allies. Richard Upton Pickman, the artist from "Pickman's Model"
(1927), eventually completed his transformation into a ghoul.

GhoFee — Ghoul
---------------

.. speciescatalog:: GhoFee

**Gugs** are gigantic, hairy, barrel-shaped creatures that inhabit the
Dreamlands underworld. They stand roughly 20 feet tall, with enormous arms
ending in paws that have vertical mouths running from wrist to elbow. Their
heads bear a single pair of pink eyes and a wide, fanged mouth. Gugs were
banished from the surface of the Dreamlands to the underworld for committing
some unnamed blasphemy against the Great Ones. A massive stone trapdoor in the
Enchanted Wood marks the boundary they are forbidden to cross. Despite their
fearsome appearance and strength, gugs possess a crude civilization and worship
dark gods. They prey on ghasts and anything else they can catch. First described
in *The Dream-Quest of Unknown Kadath* (1927).

GugsUn — Gug
-------------

.. speciescatalog:: GugsUn

**Wamps** are subterranean creatures from the Mythos, dwelling in deep cave
systems and underground passages. These lesser-known entities are predatory
and adapted to a lightless existence, hunting by sound and vibration in the
eternal darkness of the deep earth. They are generally hostile to surface
dwellers and other subterranean races alike, defending their territory with
ferocity.

WamUnd — Wamp
--------------

.. speciescatalog:: WamUnd

Dreamlands Creatures
====================

**Cats of Ulthar** are the felines of the Dreamlands city of Ulthar, where by
ancient law no man may kill a cat. This law was established after an old couple
who delighted in killing cats made the mistake of taking in a kitten belonging
to a traveling orphan boy. The boy prayed to the mysterious gods of the
Dreamlands, and that night all the cats of Ulthar gathered and descended upon
the couple. In the morning, nothing remained of the pair but two cleanly picked
skeletons. The cats of Ulthar are intelligent, organized, and capable of
collective action. They can leap to the moon and travel throughout the
Dreamlands. First appeared in "The Cats of Ulthar" (1920).

CatUlt — Cat of Ulthar
-----------------------

.. speciescatalog:: CatUlt

**Leng Spiders** are gigantic arachnids that inhabit the cold, desolate Plateau
of Leng in the Dreamlands. They are bloated, purple-bodied spiders of
extraordinary size -- smaller specimens are the size of ponies, while the
largest can tower over elephants and weigh many tons, as Leng Spiders never stop
growing. They are highly intelligent, spinning webs of incredible strength with
strategic cunning rather than instinct. Leng Spiders are solitary predators that
will even prey on their own kind. Their venom induces deep sleep, after which
victims are dragged to the spider's lair to be consumed or used as hosts for
eggs. They are thought to be the children of Atlach-Nacha, the spider god.
Once rulers of the Leng plains, they were driven to gorges and caves by the
people of Leng. First appeared in *The Dream-Quest of Unknown Kadath* (1927).

LenSpi — Leng Spider
---------------------

.. speciescatalog:: LenSpi

**Moon-Beasts** are the bloated, toad-like creatures that inhabit the dark side
of the Dreamlands' moon. They are pale, amorphous, almost faceless beings with
small red tentacles or feelers where a face should be. Moon-Beasts are cruel
slavers who sail black galleys crewed by their servants, the Men of Leng, and
trade in slaves captured from the Dreamlands' ports and cities. They serve
Nyarlathotep and maintain a trade network that extends across the Dreamlands.
Their galleys are distinctive and feared. Moon-Beasts are physically soft and
relatively weak individually, but dangerous in groups. First described by
Lovecraft in *The Dream-Quest of Unknown Kadath* (1927).

MooFun — Moon-Beast
--------------------

.. speciescatalog:: MooFun

**Nightgaunts** are faceless, black, rubbery, winged humanoid creatures that
inhabit the Dreamlands. They are lean and slippery, with bat-like wings, horned
tails, and inward-curving horns on their heads. Their most distinctive and
unsettling feature is their complete lack of a face -- where features should be,
there is only smooth, blank darkness. Nightgaunts attack by tickling their
victims into helplessness, then carrying them off through the air. Despite their
terrifying appearance, nightgaunts are not inherently evil and can sometimes be
allied with. They guard the slopes of the Dreamlands' highest peaks and serve
Nodens, Lord of the Great Abyss. Lovecraft dreamed of nightgaunts as a child,
and they appeared in *The Dream-Quest of Unknown Kadath* (1927).

NigMan — Nightgaunt
--------------------

.. speciescatalog:: NigMan

**Shantaks** are enormous bird-like creatures from the Dreamlands, larger than
elephants, with the body of a horse and the head of a horse combined with
bat-like wings. Their skin is described as slippery and scaly rather than
feathered. Shantaks serve as aerial mounts in the Dreamlands and are used by
various beings for transportation across vast distances. Despite their great
size and power, shantaks are terrified of nightgaunts, who can easily
overpower them. They nest on the peaks of the tallest mountains in the
Dreamlands and are sometimes tamed by inhabitants of the Plateau of Leng.
First described in *The Dream-Quest of Unknown Kadath* (1927).

SanDre — Shantak
-----------------

.. speciescatalog:: SanDre

**Zoogs** are small, brown, mouse-like creatures that inhabit the Enchanted
Wood of the Dreamlands. They are furtive, secretive beings roughly the size of
a rat, with sharp teeth and a taste for mischief. Though individually
insignificant, zoogs are numerous and organized into a loose tribal society led
by elders. They are omnivorous and have been known to attack travelers in large
groups. Zoogs are cunning negotiators and possess considerable knowledge of the
Dreamlands, making them useful (if unreliable) sources of information. They
maintain an uneasy truce with the cats of Ulthar, who are their natural
enemies. First appeared in *The Dream-Quest of Unknown Kadath* (1927).

ZooGul — Zoog
--------------

.. speciescatalog:: ZooGul

Interdimensional & Temporal
===========================

**Dimensional Shamblers** are interdimensional predators that move between
planes of existence. They appear as roughly humanoid but deeply wrong -- with
coarse, wrinkled skin, long arms ending in enormous crab-like claws, and a
hunched, ape-like posture. Their heads are featureless except for a mass of
short, writhing tentacles where the face should be. Dimensional Shamblers can
step between dimensions at will, appearing and disappearing without warning.
They seize their prey and drag them into other dimensions from which there is
no return. They were first described in "The Horror in the Museum" (1933),
a story ghost-written by Lovecraft for Hazel Heald.

DimSha — Dimensional Shambler
------------------------------

.. speciescatalog:: DimSha

**Hounds of Tindalos** are extradimensional entities that inhabit the "angles"
of time, as opposed to the "curves" in which normal life exists. They are
lean, filthy creatures of alien geometry, described as having long, hollow
tongues through which they drain their victims. The Hounds can materialize
through any sufficiently sharp angle -- corners of rooms, edges of furniture --
anywhere that angles of 120 degrees or less exist. Once a Hound has the scent
of its prey (typically someone who has traveled through time or used certain
drugs), it will pursue relentlessly across any distance or dimension. The only
protection is to be in a room with no angles -- a perfectly curved space. They
are believed to be among the oldest entities in existence. First appeared in
Frank Belknap Long's "The Hounds of Tindalos" (1929).

HouFir — Hound of Tindalos
---------------------------

.. speciescatalog:: HouFir

Arctic & Desert
===============

**Gnoph-Keh** are fearsome arctic creatures resembling six-legged polar bears
with coarse, matted white hair and a single large narwhal-like horn. They
possess the ability to summon blizzards and drastically reduce temperatures in
their vicinity. Gnoph-Keh are territorial, solitary, and now extremely rare,
dwelling in Greenland and the Arctic Circle. In the earliest texts (such as the
Book of Eibon), the Gnoph-Keh were described as a race of vicious cannibals
driven from the land of Lomar by mankind and the Voormis. They are connected
with Rhan-Tegoth and possibly with Ithaqua, the Wind-Walker. Legend suggests
they are the remnants of a lost tribe that turned from earthly gods to serve
Ithaqua, becoming something other than human.

GnpKeh — Gnoph-Keh
-------------------

.. speciescatalog:: GnpKeh

**Sand Dwellers** are minor creatures from the Cthulhu Mythos, originating in
"The Gable Window" by August Derleth. They resemble thin, sand-encrusted humans
with unusually large eyes and ears, and faces that look somewhat like those of
koalas. Sand Dwellers dwell in caves during daylight and emerge at night in
groups to hunt. They are associated with at least one large tentacled creature
of unknown nature. In some interpretations they are literally made of sand and
can combine into larger forms, while in others they are psychic parasites that
grow inside the minds of their victims before manifesting physically.

SanDwl — Sand Dweller
----------------------

.. speciescatalog:: SanDwl

Human-Adjacent Horrors
======================

**Rat-Things** (such as the infamous Brown Jenkin) are hybrid creatures with the
body of a rat and a disturbing, miniature human-like face with sharp teeth.
Brown Jenkin, the most famous rat-thing, served the witch Keziah Mason and could
pass through dimensional barriers along angles that correspond to alien
geometries. Rat-Things are familiar spirits of witches, carrying out errands
between dimensions and assisting in dark rituals. They are disturbingly
intelligent, possessing human-level cunning in a rodent body. Their small size
makes them difficult to catch or kill, and their ability to move between
dimensions makes them impossible to trap by conventional means. First appeared
in "The Dreams in the Witch House" (1933).

RatThi — Rat-Thing
-------------------

.. speciescatalog:: RatThi

**Tcho-Tcho** are a species of near-human beings native to Asia, found in
Burma, Tibet, Malaysia, and the Andaman Islands. Created by August Derleth and
Mark Schorer, they are notably small (rarely exceeding four feet in height),
with dome-shaped heads, small deep-set eyes, and livid skin. Despite their
small stature, they are surprisingly strong. The Tcho-Tcho are believed to have
been spawned through the genetic manipulation of pre-human ancestors by the
Great Old Ones Zhar and Lloigor, with further connections to Chaugnar Faugn
through the Miri Nigri. They worship various Great Old Ones including Hastur,
Chaugnar Faugn, and Rhan-Tegoth. They are notorious for their cannibalistic
practices and hostility toward outsiders. Lovecraft referenced them in *The
Shadow Out of Time* (1936).

TsaCho — Tcho-Tcho
-------------------

.. speciescatalog:: TsaCho

Generic models
==============

In addition to the species-specific models listed in this catalog, ``stdvoidsim`` offers
a number of generic demographic models that can be run with any species.
These are described in more detail in the :ref:`API <sec_api_generic_models>`.

 - :meth:`stdvoidsim.PiecewiseConstantSize`
 - :meth:`stdvoidsim.IsolationWithMigration`
