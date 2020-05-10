# AMR11E - Distinct Primes
# #math #number-theory
# Arithmancy is Draco Malfoy's favorite subject, but what spoils it for him is that Hermione Granger is in his class, and she is better than him at it. 
# Prime numbers are of mystical importance in Arithmancy, and Lucky Numbers even more so. Lucky Numbers are those positive integers that have at least three distinct prime factors; 
# 30 and 42 are the first two. Malfoy's teacher has given them a positive integer n, and has asked them to find the n-th lucky number. Malfoy would like to beat Hermione at this exercise, 
# so although he is an evil git, please help him, just this once. After all, the know-it-all Hermione does need a lesson.

# Input
# The first line contains the number of test cases T. Each of the next T lines contains one integer n.

# Output
# Output T lines, containing the corresponding lucky number for that test case.

# Constraints
# 1 <= T <= 20
# 1 <= n <= 1000

# Sample Input:
# 2
# 1
# 2

# Sample Output:
# 30
# 42


def sieve(n):
	number_range = 100000
	result = []
	number_list = [0] * number_range
	
	for i in range(2,number_range):
		if number_list[i] == 0:
			number_list[i] = 1
			
			for j in range(2*i,number_range,i):
				number_list[j] -= 1
				if number_list[j] == -3:
					result.append(j)
	result.sort()
	return result[n-1]

iter_num = int(input())
for i in range(iter_num):
	num = int(input())
	print(sieve(num))
	