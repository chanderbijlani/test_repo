# taking email from the user and removing spaces
email=input("What is the email address:").strip()
#using index function for getting user and domain name
user = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "Your email is {} and your username is {} and domain is {}".format(email,user,domain)
print(output)
