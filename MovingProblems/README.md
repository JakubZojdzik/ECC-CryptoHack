# Moving Problems

Given curve is vulnerable to [MOV attack](https://risencrypto.github.io/WeilMOV/). The general idea is to reduce initial elliptic curve discrete logarithm problem to easier finite field discrete logarithm. Math behind it is too complicated for me and I don't get it, so I used [implementation from internet](https://ctftime.org/writeup/33964). I used sage for finite field DLP, but it needs some time to calculate.

## Flag

crypto{MOV_attack_on_non_supersingular_curves}