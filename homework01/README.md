# Practicing python with numbers

In this file we brush up on python by using it to generate primes with Eratosthenes Sieve and figuring out how to determine if numbers are odd or even with python.

## Description
1.
The first python script OddEven.py takes a random list of ten numbers, n. If n%2 == 0, the number is even 
and it prints out "n is even". Otherwise it prints, "n is odd".


2.
The second python script takes each number from i = (3,100) and attempts to divide it by each of the numbers lower
than it in n = (2,100). If it finds a number lower than i that can divide it without a remainder, it is not prime,
so the loop breaks. If n>=i the loop also breaks because we dont want to check numbers greater than i.  
Then if each of the numbers has a remainder it prints the number as it is prime. 


### Dependencies

* Running these files requires: python3
### Installing

* To install python3 with homebrew type:
```
brew install python3
```
in the commandline (requires homebrew)
otherwise go to the python website

### Executing program

* To run this file, pull each of the files from github and call them in the commandline

ex:
```
    python3 OddEven.py
```
will result in the file OddEven.py running