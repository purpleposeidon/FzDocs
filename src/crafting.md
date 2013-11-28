Crafting Machines
=================
There are three basic crafting machines, and the much more complex [Compression Crafter](compact.html).

The Stamper
-----------
The stamper takes a single item and crafts it by itself.
It outputs a redstone signal when it does this.

The Packager
------------
The packager takes 9 or 4 items, and crafts them in a 3x3 or 2x2 grid.
It first tries the 3x3, and then falls back to the 2x2.

The Mixer
---------
The mixer runs shapeless crafting recipes.
Unlike vanilla shapeless crafting, the mixer will ignore over-large stacks.
For example, mushroom stew can be crafted even if there are wooden bowls in two slots.
If this could result in an ambiguity, the mixer will go for the larger recipe.
The mixer will accelerate its crafting speed if it does not run out of materials.


