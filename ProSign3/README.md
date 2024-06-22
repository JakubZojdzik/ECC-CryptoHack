# ProSign 3

Here, we have to sign `unlock` message with ECDSA without provided private key, but with possibility to sign some restricted messages. In ECDSA signing should be performed with cryptographically secure random integer `k` less than `n`, which is integer order of `G`. In provided algorithm, `n` variable is assigned to number of second in current time, which is between 0 and 59, so used `k` will also be in this range. With the knowledge of value of `k`, we can calculate private key and sign every message we want. As there aren't many possible values of `k`, we can brute force it by assuming it is equal to 1 and check if further calculations will give flag.

## Flag

crypto{ECDSA_700_345y_70_5cr3wup}