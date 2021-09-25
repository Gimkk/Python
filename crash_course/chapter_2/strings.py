first_name = "Albert"
last_name = "Einstein"
print(f"Hello {first_name.title()} {last_name.title()}, would you like to learn some python today? - title name")
print(f"Hello {first_name.upper()} {last_name.upper()}, would you like to learn some python today? - upper name")
print(f"Hello {first_name.lower()} {last_name.lower()}, would you like to learn some python today? - lower name")

print(f"{first_name} {last_name} once said,", end=" ") 
print('"A person who never made a mistake never tried anything new."')

str = "---geeksforgeeks---"
print(f"String after stipping all '-' is : {str.strip('-')}")
print(f"String after stipping all leading '-' is : {str.lstrip('-')}")
print(f"String after stipping all tailing '-' is : {str.rstrip('-')}")