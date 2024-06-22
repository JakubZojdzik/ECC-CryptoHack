# Montgomery's Ladder

In this challenge, Montgomery form of curve was provided, so new addition and multiplication formulas were needed. This time, we had to multiply generator point by `0x1337c0decafe`, but firstly, we had to find Y coordinate of `G`. It is easy to get square of it by just passing it's x to the curve formula, but then it would be necessary to find it's root what is more difficult. One could either implement an algorithm for finding it or use a ready function from sage math and get whole point `G` with one function `lift_x`.

## Flag

crypto{49231350462786016064336756977412654793383964726771892982507420921563002378152}