## Check Permutation
*Given two strings write a method to decide if one is a permutation of the other.*

This solution builds a list of permutations using the helper function compute_permutation.  
It then iterates through the first list and for every permutation checks if it matches any permutation in the second list.  
If any matches are found, one string is a permutation of the other string.

The complexity of checking if any items of the list match is a*b, where a is the size of the first list and b is the size of the second. Computing the list of permutations is n! where n is the number of characters in the longest input string.