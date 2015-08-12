# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#Body

t = [1, 2, 3, [4, 5], 6]

def nested_sum(t):
    total = 0
    for i in t: #i is each element in list t
        if type(i) == list: #if the type of element is a list
            total = total + nested_sum(i) # adds elements within list to total
        else:
            total += i
    return total


##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()
