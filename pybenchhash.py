import time
import hashlib
import matplotlib.pyplot as plot
from passlib.hash import b
import random 
import argon 


# Random salt generation 
def ransalt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    chars = []

    for i in range(16):
        chars.append(random.choice(ALPHABET))

    return "".join(chars)


# Variables
string = input('Enter the benchmarking string: ')

key = b + input('Please specify a key between 4 and 56 bytes: ')

algo = ['MD5', 'SHA-1', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512', 'Scrpyt', 'Bcrypt', 'Argon2']
colors = ['b', 'c', 'y', 'm', 'r', 'k', 'l', 'm', 'f']
results = {}

# Getting iterations and step
iterations = int(raw_input("Iterations: "))
while iterations < 1 or iterations > 1000000:
    iterations = int(raw_input("Please enter a valid value for the number of iterations (1-1000000): "))

step = int(raw_input("Step: "))
while step < 1 or step > 1000000:
    step = int(raw_input("Please enter a valid value for the step (1-1000000): "))

print("\nbenchmarking...\n")

# MD5
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.md5(string)
    results[0,(i+1)*step] = (time.time() - Start)
print("\nMD5 benchmark done.\n")

# SHA-1
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha1(string)
    results[1, (i+1)*step] = (time.time() - Start)
print("\nSHA-1 benchmark done.\n")

# SHA-224
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha224(string)
    results[2, (i+1)*step] = (time.time() - Start)
print("\nSHA-224 benchmark done.\n")

# SHA-256
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha256(string)
    results[3, (i+1)*step] = (time.time() - Start)
print("\nSHA-256 benchmark done.\n")

# SHA-384
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha384(string)
    results[4, (i+1)*step] = (time.time() - Start)
print("\nSHA-384 benchmark done.\n")

# SHA-512
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha512(string)
    results[5, (i+1)*step] = (time.time() - Start)
print("\nSHA-512 benchmark done.\n")

# Bcrypt  
Start = time.time() 
tString = b + string 

for i in range (iterations):
    for j in range ((i+1)*step): 
        bcrypt.hashpw(tString, bcrypt.gensalt()) #random salt  
    results[6, (i+1)*step] = (time.time() - Start) 
print("\nBcrypt benchmark done.\n")

# Scrypt 
Start = time.time() 
tString = b + string #redundant but for exhibition purposes 

for i in range (iterations): 
    for j in range ((i+1)*step): 
        hashlib.scrypt(key, ransalt())
    results[7, (i+1)*step] = (time.time() - Start)
print("\nScrypy benchmark done.\n")

# Argon2 
Start = time.time() 

for i in range (iterations): 
    for j in range ((i+1)*step): 
        argon2.argon2_hash(string, ransalt()) 
    results[8, (i+1)*step] = (time.time() - Start) 
print("\nArgon2 benchmark done.\n")

# Generate plot and print results
print "\n---------- Report ----------\n"
for i in range(9):
    print algo[i]
    for j in range (iterations):
        print (j+1)*step, 'iterations in', results[i,(j+1)*step]*pow(10,3), 'ms'
        plot.plot((j+1)*step, results[i,(j+1)*step]*pow(10,3),colors[i]+'o', label=str(algo[i]) if j == 0 else "")
    print '\n'
plot.xlabel('Iterations')
plot.ylabel('Execution time in milliseconds')
plot.title('PyBenchHash', fontsize=40, color='white')
plot.legend(loc=2)
plot.grid(True)
plot.show()