# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#Body

t = ['apple', ['bear'], 'cherries', ['giraffe']]

def capitalize_nested(t):
    cap = []
    for s in t:
        if type(s) == list:
            cap.append(capitalize_nested(s))
        else:
            cap.append(s.capitalize())
    return cap
    print cap


##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()
