import re
# Write a Python program to check that a string contains only a certain set of characters 
# (in this case a-z, A-Z and 0-9).

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

# print(is_allowed_specific_char("Welcome to RegExr \\\\,v2.1 by gskinner.com, proudly hosted by Media Temple! Edit the Expression & Text to see matches. Roll over matches or the expression for details. Undo mistakes with ctrl-z. Save Favorites & Share expressions with friends or the Community. Explore your results with Tools\\\\, A full Reference & Hel\\\\p is available in the Library, or watch the video Tutorial. Sample text for testing: abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 _+-.\\,!@#$%^&*();\\/|<>\"\'12345 -98.7 3.141 .6180 9\\,000 +42555.123.4567	+1-(800)-555-2468 foo@demo.net	bar.ba@test.co.uk\\,,,www.demo.com	http://foo.co.uk/ http://\\\\regexr.com/foo.html?q=bar\\\\,\\ https://mediatemple.net\\,'
# ")) 
print(is_allowed_specific_char("*&%@#!}{"))
