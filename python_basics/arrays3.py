my_list = [2]
my_list.append(3)     # Append chucks at the end of the list.
my_list.insert(1, 9)  # Insert(a, b) pushes everything with index >= a to the right.
my_list[0] = 6        # Generic modification through indexing is ok too.
print(my_list)