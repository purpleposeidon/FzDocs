Compression Crafter
===================
(Picture of a CompACT system goes here...)

The Compression Crafter (CompACT) is a crafting system that uses blocks, in the world, rather than items in an inventory.
It is a mutli-block structure.
The crafting grid size can range from 1x1 (using 4 CompACT blocks) to 3x3 (using 12 CompACT blocks).

The CompACT blocks must be placed around the desired crafting area, with the blue grids facing inwards.
To activate crafting, a redstone signal must be applied to a CompACT block,
and that block must be adjacent to an inventory to output the crafting results.

It can convert blocks into items in a few different ways:

0. If it is a barrel, it'll use the barrel's contents
0. It will try to use the block exactly as it is (not unlike silk touch)
0. It will use the broken form of the block (eg, smooth stone used as cobblestone)
0. It will break the block, and use the output of crafting it by itself (eg, wood log used as wooden planks)

If crafting with barrels, it can pull up to 32 items at once for one craft.
The crafted form of a block can also be used to craft multiple items at once;
9 being typical for metal storage blocks.

If crafting fails, it may be because the CompACT is looking at the crafting grid at a different angle.


