students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

pets = [("Cat", 4), ("Dog", 10), ("Snake", 4)]
sorted_pets = sorted(pets, key=lambda x: x[1])
for name, age in sorted_pets:
    print(f"{name} — {age} years", end="|")

print(" ")
year = [("Persen1", 4), ("Persen2", 10), ("Persen3", 20), ("Persen4", 60), ("Persen5", 114)]
sorted_year = sorted(year, key=lambda x: x[1])
for name, age in sorted_year:
    print(f"{name} — {age} years", end="|")

print(" ")
year = [("Persen1", 4), ("Persen2", 10), ("Persen3", 20), ("Persen4", 60), ("Persen5", 114)]
sorted_year = sorted(year, key=lambda x: x[1], reverse = True)
for name, age in sorted_year:
    print(f"{name} — {age} years", end="|")



