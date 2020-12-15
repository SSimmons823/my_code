#!/usr/bin/env python3

# create a list that we can sort
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

# print what we are testing
print("Currently the value of vendor:", vendors)

# print the results
print("\nThe results of sorted() function:", sorted(vendors))

# print to show the value does not change
print("\nBut the value of the list hasn't actually changed:", vendors)

# creat new (sorted) list
sortedvendors = sorted(vendors)

# display new (sorted) list
print('Our sorted vendor list looks like this: ' + str(sortedvendors))

# reverse the order
baksortvendors = sorted(vendors, reverse=True)

# display reversed order
print('Our sorted vendor list looks like this: ', baksortvendors)

# create new mixed list of lower and capitals
vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', \
'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

# display list
print('Our new vendordeux list looks like this: ', vendorsdeux)

# display (sorted) list
print('Our sorted vendor list looks like this: ', sorted(vendorsdeux))

