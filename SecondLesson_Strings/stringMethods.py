text = "   Python Programming   "

# Remove leading and trailing whitespace
cleaned_text = text.strip()
print("Strip:", cleaned_text)

# Convert to lowercase and uppercase
lower_text = text.lower()
print("lower:", lower_text)

upper_text = text.upper()
print("UPPER:", upper_text)

# Find and replace
replaced_text = text.replace("Programming", "Code")
print(replaced_text)