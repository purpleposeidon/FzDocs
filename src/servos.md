Servos
======
![A sugar-cane harvesting servo](screen/servo.png)

Servos are entities that ride on Servo Rail.
They can be equiped with a socket tool, and provide a four-slot inventory.

Servo Rail
----------
Servo rail is the conductive wire that servos ride on. Charge is drawn from the servo rails to power the servo and its socket tool.
Instructions (and decorators) can be placed on servo rail.
Servos travel along the servo rail, and execute instructions as they pass over them.

Instructions
------------
Instructions can be placed infinitely on servo rails.
The Logic Matrix Programmer is used to modify and remove them.

Shift-right clicking with an LMP will remove it from the rail.
Right clicking an instruction will cycle it to a different version of it.
Clicking on an instruction empty-handed _may_ show a notification indicating its state.

For details on specific instructions, see the [Instructions](instructions.html) page.

Decorators
----------
Decorators are similar to instructions, except they are single-use.
Presently the only decorators are the three grates; their purposes is to plug up holes in the floor.

Servo Motion
------------
When confronted with a rail junction, the servo has a choice of which direction to go.

0. If there is an entry control ![Green Checkmark](textures/blocks/servo/entry_require.png) instruction, it will go that way.

0. If it has encountered a ![Set Direction](textures/blocks/servo/set_direction_side_E.png) that it could not execute, it will go in that direction.

0. It prefers to go straight.

0. It tries to go in the direction it was moving previously (this makes it zig-zag). For example, if it reaches a T intersection after a left turn, it will go right.

0. If it can not go straight, then it will try to go up (relative to the servo), or down.

0. Failing that, it will go right or left, at random.

0. It avoids going through a forbidding entry control ![Red x mark](textures/blocks/servo/entry_forbid.png); this is the second-to-last resort.

0. It won't go backwards unless it is at a dead-end.

<small><i>(Probably.)</i></small>

Computation
-----------
Not yet implemented.

Each servo has 16 seperate stacks, one for each wool color in Minecraft.
Each stack can hold 16 values.
Looking at a servo while holding an LMP will show the contents of the stacks.

At present only two stacks are used.
The yellow stack is used for values, and the black stack is used for error messages.

Examples
--------
[sorting system; sugar cane harvester...]
