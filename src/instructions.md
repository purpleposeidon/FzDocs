Instructions Reference
======================

Motion
------
![Instruction](textures/blocks/servo/entry_require.png)
![Instruction](textures/blocks/servo/entry_forbid.png)
__Entry Control__: Servos are attracted to the green check, and repelled by the red x.

![Instruction](textures/blocks/servo/set_direction_side_E.png)
(![Instruction](textures/blocks/servo/set_direction_back.png)
![Instruction](textures/blocks/servo/set_direction_front.png))
__Set Direction__: Makes the servo move in the specified direction.
This can make the servo reverse direction. 
If it points the servo in a direction it can not go (because there is no servo rail),
it will move in that direction at the next possible opportunity (Pacman-style).

![Instruction](textures/blocks/servo/set_facing_side_E.png)
(![Instruction](textures/blocks/servo/set_facing_back.png)
![Instruction](textures/blocks/servo/set_facing_front.png))
__Point Top__: Sets the top of the servo.
It does not make sense to point the top parallel to the direction of motion

![Instruction](textures/blocks/servo/speed1.png)
![Instruction](textures/blocks/servo/speed2.png)
![Instruction](textures/blocks/servo/speed3.png)
![Instruction](textures/blocks/servo/speed4.png)
![Instruction](textures/blocks/servo/speed5.png)
__Set Speed__: Sets the servo speed.
Speed 3 is the default speed.

![Instruction](textures/blocks/servo/spin_ccc.png)
![Instruction](textures/blocks/servo/spin_cc.png)
__Spin__: Spin clockwise or counter-clockwise.
If a servo passes over one, and then reverses direction and passes over it again,
it will be facing in the original direction.

![Instruction](textures/blocks/servo/trap.png)
__Trap__: Stops the servo motor.
It will resume motion when given a redstone signal.
Sockets will continue to operate.

Socket
------
__Socket Control__: Controls the redstone signal sent to the socket.

* ![Instruction](textures/blocks/servo/socket_on.png) Turns on a steady redstone signal.

* ![Instruction](textures/blocks/servo/socket_off.png) Turns off a steady redstone signal.

* ![Instruction](textures/blocks/servo/socket_pulse.png) Pulses the signal. If the signal is steady on, it will flicker instead.

__Item Shifter Control__: Changes settings in the Item Shifter;
this allows control of the same settings that are in [the GUI](sockets.html#shifter).


* ![Instruction](textures/blocks/servo/ctrl/shift_export.png) Export Mode

* ![Instruction](textures/blocks/servo/ctrl/shift_import.png) Import Mode

* ![Instruction](textures/blocks/servo/ctrl/shift_pulse_exact.png) Pulse Exact

* ![Instruction](textures/blocks/servo/ctrl/shift_pulse_some.png) Pulse Some

* ![Instruction](textures/blocks/servo/ctrl/shift_stream.png) Stream

* ![Instruction](textures/blocks/servo/ctrl/shift_target_slot.png) Target Slot; set with an integer popped from the stack.

* ![Instruction](textures/blocks/servo/ctrl/shift_transfer_limit.png) Transfer Limit; set with an integer popped from the stack.

Math and Logic
--------------
![Instruction](textures/blocks/servo/cmp_eq.png)
![Instruction](textures/blocks/servo/cmp_ge.png)
![Instruction](textures/blocks/servo/cmp_gt.png)
![Instruction](textures/blocks/servo/cmp_le.png)
![Instruction](textures/blocks/servo/cmp_lt.png)
![Instruction](textures/blocks/servo/cmp_ne.png)
__Compare__: Pops two integers from the stack and compares them.
(The cyan underline indicates the bottom of the icon.)

![Instruction](textures/blocks/servo/true.png)
![Instruction](textures/blocks/servo/false.png)
__Boolean Value__: Pushes `true` or `false`.

![Instruction](textures/blocks/servo/one.png)
![Instruction](textures/blocks/servo/zero.png)
![Instruction](textures/blocks/servo/number.png)
__Integer Value__: Pushes `1` or `0`. (The # is presently not available.)

![Instruction](textures/blocks/servo/sum.png)
__Sum__: Sum two integers popped from the stack, and push the value onto the stack.

![Instruction](textures/blocks/servo/product.png)
__Product__: Multiply two integers popped from the stack, and push the value onto the stack.

Stack
-----
![Instruction](textures/blocks/servo/drop.png)
__Drop__: Pop a value from the stack, and do nothing with it.

![Instruction](textures/blocks/servo/dup.png)
__Dup__: Duplicates the top value of the stack.

Other
-----
![Instruction](textures/blocks/servo/pulse.png)
__Redstone Pulse__: Emits a redstone pulse from the rail.

__Jump__: 

* ![Instruction](textures/blocks/servo/jmp_instruction.png)
Pop a boolean from the stack.
If it is true, then the next found instruction is jumped over.

* ![Instruction](textures/blocks/servo/jmp_tile.png)
Unconditionally skip the instruction on the next (adjacent) servo rail.
If the next servo rail is empty, then there will be no effect.

