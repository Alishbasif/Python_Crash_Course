# ==========================================
# Problem 1
# Find the Index of the Word "Python"
# ==========================================

sentence = input("Enter a Sentence: ")

index = sentence.find("Python")

if index != -1:
    print("'Python' is found at index:", index)
else:
    print("'Python' is not found.")

# ==========================================
# Problem 2
# Replace "Python" with "Java"
# ==========================================

sentence = input("Enter a Sentence: ")

new_sentence = sentence.replace("Python", "Java")

print("Updated Sentence:", new_sentence)   