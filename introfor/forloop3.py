#!/usr/bin/env python3

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


    for x in farms:
        print(x.get("name"),end= ":\n")
    
        for i in x.get("agriculture"):
           print(" - ", i)

main()
