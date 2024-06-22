# Curveball

We have to find a pair `private_key` and `generator`, which product will be equal to public key assigned to `www.bing.com`. The easiest way would be to set `private_key=1`, but it isn't allowed. Natural next idea is to set `private_key=2` and try to find matching generator. I have found [this easy method](https://crypto.stackexchange.com/questions/55069/elliptic-curve-divide-by-2#answer-55109).

## Flag

crypto{Curveballing_Microsoft_CVE-2020-0601}