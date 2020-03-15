formatter = "%r %r %r %r"
#Prints numbers
print(formatter % (1, 2, 3, 4))
#prints strings
print(formatter %("one","two","test","okay"))
#prints true/false
print(formatter %(True, False, True, False))
#prints formatter string as literal string.
print(formatter %(formatter,formatter, formatter, formatter))
#prints several sentence strings.
print(formatter %(
    "testing string",
    "testing2nd line",
    "testing 3rd line",
    "testing 4th line"
))
