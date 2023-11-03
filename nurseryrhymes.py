def nurseryStories():
    girls_name_nr = input("Enter a Girl's Name: ")
    animal_nr = input("Enter an Animal: ")
    color_nr = input("Enter a Color: ")
    place_nr = input("Enter a Place: ")
    verb_nr = input("Enter a Verb: ")

    nursery_story = (
        girls_name_nr + " had a little " + animal_nr + " little " + animal_nr + " little " + animal_nr + ". \n" +
        girls_name_nr + " had a little " + animal_nr + ", its fleece was " + color_nr + " as snow.\nIt followed her to " + place_nr + " one day, " + place_nr + " one day, " + place_nr + " one day,\n" +
        "it made the children " + verb_nr + " and play to see " + animal_nr + " at " + place_nr + "."
    )
    print(nursery_story)

if __name__ == '__main__':
    nurseryStories()
