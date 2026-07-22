capitals = {"USA": "Washington D.C",
            "INDIA": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",}
#if (capitals.get("USA")):
 #   print("That capital exists")
#else: 
 #   print("That capital doesn't exist")    

#capitals.update({"Germany": "Berlin"})
#capitals.pop("China")
#keys = capitals.keys()
#for key in capitals.keys():
 #   print(key)

#values = capitals.values()
#print(values)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

                                