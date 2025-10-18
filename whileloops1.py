a = 0
two_power_a = 1  # 2^0 = 1.
largest_value = int(input("What number? "))
print("Powers of 2 less than {l}:".format(l=largest_value))
while two_power_a < largest_value:
    # This indented block is repeated, and continually
    # modifies two_power_a until it exceeds largest_value.
    print("2^{a} = {x}".format(a=a, x=two_power_a))
    a += 1
    two_power_a = pow(2, a)