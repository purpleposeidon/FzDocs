Parasieves
==========
The parasieve is used to proxy and filter the contents of an inventory.
It is placed against the side of an inventory, and it will provide extended access to that inventory.

Parasieves have 4 slots for filtering items, and additional 4 slots for specifying a range of items.
If two items are provided with the same ID and damage value, but one has an NBT tag (like enchants)
and the other does not, then NBT tags will be ignored.
If the item has the same ID and differing damage value, then items within the range of damage value
will be accepted.
This can be used to filter ranges of wool and damaged swords.
If the two items are from the same mod (not neglecting sub-mods), then all items from those mods
will be accepted.
Otherwise the results are undefined, tho they may still be useful.
Applying a redstone signal to the parasieve will invert the filter.

Parasieves can be chained up to 6 times.
They also support comparators; they can be used to measure the ratio of items in an inventory.



