import numpy as np

#There are two words we take: Source and target
source_word = input("Please enter the source word:\n")
target_word = input("Please enter the target word:\n")

#For creating a matrix, we are adding +1 to both row and column, then we are creating matrix with zeros.
source_length = len(source_word) + 1
target_length = len(target_word) + 1
levensthein_matrix = np.zeros((target_length, source_length))

#We are adding each words' indexes
for i in range(0,target_length):
    levensthein_matrix[i][0] = i

for j in range(0, source_length):
    levensthein_matrix[0][j] = j


#We are looking every letter. If letter of the words are the same, cost will be 0. Else it will be 1.
for i in range(1, target_length):
    for j in range(1, source_length):
        if source_word[j - 1] == target_word[i - 1]:
            cost = 0
        else:
            cost = 1
        levensthein_matrix[i][j] = min(levensthein_matrix[i - 1][j] + 1,levensthein_matrix[i][j - 1] + 1,levensthein_matrix[i - 1][j - 1] + cost)
#Parameters in min function represents insert, delete, replace respectively.

print("Levenshtein matrix:\n",levensthein_matrix)
#Last element of the matrix is distance
print("Distance:",levensthein_matrix[-1][-1])

