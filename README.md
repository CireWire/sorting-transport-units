## Welcome to my code

This was something I wanted to use personally to sort out some of the trailers I had to go through at work. This saved me a lot of hassle when I had to send a response to my **boss**.

##Code
```
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
```


### Support or Contact

This is a very easy program to use and edit, but if you need any help feel free to contact me!
