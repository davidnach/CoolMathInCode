# math_inspired
code that is inspired by math which i consider to be neat.

# euclidean algorithm

Just by looking at the code for this, it might not be too obvious what's going on here. However, what this code is doing is actually
really simple. It's finding the greatest common divisor between two numbers a and b. Here's an explanation for why this works:

(assuming a > b)
1. we set r = a % b.
1. r == 0 and a > 0 that means a is a multiple of b which makes gcd(a,b) = b.we're done.
2. if r != 0 Since a % b == r % b we can say that (a - r) % b == 0, or b evenly divides a - r.
3. Now we can have bx + r = a or bx - a = r (where x is some integer). if d divides a and b, then it also divides r and b, and if
it divides r and b, then it also divides a and b. Therefore gcd(a,b) == gcd(r,b).

