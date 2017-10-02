days = int(raw_input ("How many days are you looking for?"))

two_days = [21205, 23060, 22732]
three_days = [21102, 21285, 19943, 20694, 21482, 22802, 21403]
four_days = [21839, 21938, 22536]
six_days = [21614]

if days == 2:
  print ("These trailers have been here for 2 days:" + " " + str(sorted(two_days)))
elif days == 3:
  print ("These trailers have been here for 3 days:" + " " + str(sorted(three_days)))
elif days == 4:
  print ("These trailers have been here for 4 days" + " " + str(sorted(four_days)))
elif days >= 5:
  print "These trailers have been here for over 5 days" + " "+ str(sorted(six_days))
else:
  print ("Sorry, I can't help you.")

print days
