# math_inspired
code that is inspired by math which i consider to be neat.

# euclidean algorithm

Just by looking at the code for this, it might not be too obvious what's going on here. It's finding the greatest common divisor between two numbers a and b. Here's an of the algorithm

(assuming a > b)
1. we set r = a % b.
1. r == 0 and a > 0 that means a is a multiple of b which makes gcd(a,b) = b.we're done.
2. if r != 0 Since a % b == r % b we can say that (a - r) % b == 0, or b evenly divides a - r.
3. Now we can have bx + r = a or bx - a = r (where x is some integer). If an integer d divides r and b evenly, then it must also divide a evenly.
   i.e d(i*x + j) = a  -> i*x + j = (a/d) where i and j are integers.


