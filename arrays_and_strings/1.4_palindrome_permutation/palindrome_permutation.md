## Palindrome Permutation

This solution builds a list of permutations using the recursive function referenced in 1.3.  
It then checks if any of the permutations are a palindrome. It does this by reversing the character array and checking if it is equal to the original array.  

Building the list of permutations takes n! where n is the number of characters in the input string. Checking for a palindrome takes n time to build the backwards array and n time to check if the arrays are equal, 2n time in total.  
The algorithim takes 2n for every n! permutation, 2n * n! which simplifies to O(n!)

An alternate way of checking if a string is a palindrome is to set a pointer at the start and the finish of the string and move them towards the 'center' checking for equality as you go. The complexity of this is n/2 where n is the number of characters in the potential palindrome.