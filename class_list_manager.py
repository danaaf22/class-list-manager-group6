# Class List Manager - Group 6
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
# ===== Each student adds her function BELOW this line =====
# Written by: Dana alfreeh (task 1)
def count_names(names):
    return len(names)
#Written by: Dana alzahrani (task 2) 
def search_name(names, name):
    for student in names:
        if student == name:
            return True
    return False
# Written by: Haifa (task 3)
def sort_names(names):
    return sorted(names)
# Written by: Haifa (task 4)
def longest_name(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest
# Written by: Tuleen Alnaim (task 6)
def to_upper(names):
    return [name.upper() for name in names]
# Written by: Tuleen Alnaim (task 8)
def remove_duplicates(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Search result:", search_name(names, "Sara"))
    print("Sorted names:", sort_names(names))
    print("Longest name:", longest_name(names))
    print("Uppercase names:", to_upper(names))
    print("Names without duplicates:", remove_duplicates(names))
# Each student calls her function here, for example:
# print("Number of names:", count_names(names))
main()

