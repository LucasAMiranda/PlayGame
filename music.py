def musicStories():
    animal_music = input("Enter an Animal: ")
    verb_ing_music = input("Enter a Verb ending in 'ING': ")
    noun1_music = input("Enter a Noun: ")
    verb_music = input("Enter a Verb: ")
    occupation_music = input("Enter an Occupation: ")
    adjective_music = input("Enter an Adjective: ")
    animal1_music = input("Enter an Animal: ")
    noun2_music = input("Enter a Noun: ")
    noun_plural_music = input("Enter a Noun (plural): ")
    relationship_music = input("Enter a Relationship: ")
    body_part_music = input("Enter a Body part (plural): ")

    smelly_music = (
        "Smelly " + animal_music + ".\n"
        "Smelly " + animal_music + ", smelly " + animal_music + ".\n"
        "What are they " + verb_ing_music + " you?\n"
        "Smelly " + animal_music + ", smelly " + animal_music + ".\n"
        "It's not your " + noun1_music + ".\n"
        "...\n"
        "They won't " + verb_music + " you to the " + occupation_music + ".\n"
        "You're obviously not their " + adjective_music + " " + animal1_music + ".\n"
        "You may not be a " + noun2_music + " of " + noun_plural_music + ",\n"
        "And you are no " + relationship_music + " to those with " + body_part_music + ".\n"
        "...\n"
        "Smelly " + animal_music + ".\n"
        "Smelly " + animal_music + ", smelly " + animal_music + ".\n"
        "What are they " + verb_ing_music + " you?\n"
        "Smelly " + animal_music + ", smelly " + animal_music + ".\n"
        "It's not your " + noun1_music + "."
    )
    print(smelly_music)

if __name__ == '__main__':
    musicStories()