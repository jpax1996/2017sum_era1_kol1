#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/2017sum_era1_kol1
#
#Delete these comments before commit!
#Good luck.



def add_matrix (mat1,mat2):
	int i = 0
	result = [
         [0,0,0],
         [0,0,0]]
	for i in range(len(2)):
   		# iterate through columns
   		for j in range(len(2)):
       			result[i][j] = X[i][j] + Y[i][j]
	return result
	
def mult_matrix (mat1,mat2):
	int i = 0
	result = [
         [0,0,0],
         [0,0,0]]
	for i in range(len(2)):
   		# iterate through columns
   		for j in range(len(2)):
       			result[i][j] = X[i][j] * Y[i][j]
	return result
	
