"""
calculate sum of 5 subjects and find percentage
"""

sub1 = float(input("Enter sub1 marks : "))
sub2 = float(input("Enter sub2 marks : "))
sub3 = float(input("Enter sub3 marks : "))
sub4 = float(input("Enter sub4 marks : "))
sub5 = float(input("Enter sub5 marks : "))


sum = (sub1 + sub2 + sub3 + sub4 + sub5) / 500
print(f"Percentage : {sum*100}")
