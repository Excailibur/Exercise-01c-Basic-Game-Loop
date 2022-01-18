world = {
    "story":"Zork",
    "startnode":"1",
    "passages": [{
        "name":"West of House",
        "pid":"1",
        "links": [{
            "label": "NORTH",
            "newPassage": "North of House",
            "pid": "2",
            "selection": "1"
        }],
        "cleanText":"This is an open field west of a white house, with a boarded front door."
    },
     {
        "name":
        "North of House",
        "pid":
        "2",
        "links": [{
            "label": "WEST",
            "newPassage": "West of House",
            "pid": "1",
            "selection": "1"
        }],
        "cleanText":
        "You are facing the north side of a white house. There is no door here, and all the windows are barred."
    }]
}

current = world["startnode"]
response = ""
current_location = {}
while True:
    if response == "quit":
        break
    # Find passage (update)
    if "links" in current_location:
      for link in current_location ["links"]:
        if link ["selection"]==response:
          current = link["pid"]
    for passage in world["passages"]:
      if current == passage["pid"]:
        current_location = passage
    # Display passage (render the world)
    if "name" in current_location:
      print(current_location["name"])
      print(current_location["cleanText"])
      print("select one of the following:")
    for link in current_location["links"]:
      print("({}) {}".format(link["selection"],link["label"]))
    response = input("What do you want to do? (type [quit] to exit)")
