#!/usr/bin/env python3
shows =[ 
    "The Crown", 
    "Succession",
    "Unbreakable Kimmy Schmidt",
    "The Great British Baking Soda"
]


times_watched = [0.5, 0, 2, 0, 15]

show_times={}
if len(shows) == len(times_watched):
    for i in range(len(shows)):
        show_times[shows[i]]=times_watched[i]
print(show_times)



#print(dict(zip(shows, times_watched)))
