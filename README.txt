In the file RSA_UnifyID I created an RSA key pair using Random.org.
To do this I sent and recieved json dictionaries that had random numbers
from these numbers I grabbed two large primes and created a public and a
private key by choosing a prime number greater than 2 and less than the 
euler's quotient (p - 1) * (q - 1) to be the public key and taking the inverse of the public 
key and modding it by the euler's quotient to get the private key. The one 
caveat is that the program is not necessarily guaranteed to get two prime 
numbers p and q but the odds are in our favor and the program has not failed
in finding two large primes p and q out of the many times I ran it. I also 
used a function to check for primality I found on stackoverflow only because 
of the time crunch.