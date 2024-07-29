# ask for user name
name = input("Whats Your Name? ")

# Remove White Space from String, if user put exra space while entering input their name excidentaly it will clear space before first word
name = name.strip()
#Capitalize First latter of all words input by user
name = name.title()

# Say Hello to User
print("Hello," + name)
