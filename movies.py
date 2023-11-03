def moviesStories():
    noun_movies = input("Enter a Noun: ")
    silly_word_movies = input("Enter a Silly Word: ")
    noun1_movies = input("Enter a Noun: ")
    noun2_movies = input("Enter a Noun: ")
    girls_name_movies = input("Enter a Girl's Name: ")
    noun3_movies = input("Enter a Noun: ")
    verb_ed_movies = input("Enter a Verb Ending with 'ED': ")
    noun4_movies = input("Enter a Noun: ")
    verb2_ed_movies = input("Enter a Verb Ending with 'ED': ")
    noun5_movies = input("Enter a Noun: ")
    noun6_movies = input("Enter a Noun: ")
    surname_movies = input("Enter a Surname: ")
    noun7_movies = input("Enter a Noun: ")
    verb_ing_movies = input("Enter a Verb Ending with 'ING': ")
    noun8_movies = input("Enter a Noun: ")
    verb_movies = input("Enter a Verb: ")
    verb_s_movies = input("Enter a Verb Ending with 'S': ")
    noun9_movies = input("Enter a Noun: ")
    adjective_movies = input("Enter an Adjective: ")

    moviesStories = {
            "noun_movies": noun_movies,
            "silly_word_movies": silly_word_movies,
            "noun1_movies": noun1_movies,
            "noun2_movies": noun2_movies,
            "girls_name_movies": girls_name_movies,
            "noun3_movies": noun3_movies,
            "verb_ed_movies": verb_ed_movies,
            "noun4_movies": noun4_movies,
            "verb2_ed_movies": verb2_ed_movies,
            "noun5_movies": noun5_movies,
            "noun6_movies": noun6_movies,
            "surname_movies": surname_movies,
            "noun7_movies": noun7_movies,
            "verb_ing_movies": verb_ing_movies,
            "noun8_movies": noun8_movies,
            "verb_movies": verb_movies,
            "verb_s_movies": verb_s_movies,
            "noun9_movies": noun9_movies,
            "adjective_movies": adjective_movies,
            "nightmare_on_elm_street": (
                "A " + noun_movies + " on " + silly_word_movies + " Street.\n...\nThe movie begins with a mysterious "
                + noun1_movies + " crafting a deadly glove with " + noun2_movies + " for fingers.\n" + girls_name_movies +
                " , a girl, has a terrifying " + noun_movies + "where she's attacked by the glove-" + noun2_movies + " man."
                "\nHer " + noun3_movies + " is mysteriously slashed during the dream.\n...\n" + girls_name_movies +
                " shares her " + noun_movies + "  with her friends, Nancy, Rod, and Glen.\nThey've all been having similar "
                + noun_movies + ". That night, " + girls_name_movies + " is " + verb_ed_movies + " in her dream, and her "
                + noun4_movies + " is mirrored in the real world.\nRod is " + verb2_ed_movies + " for her " + noun5_movies + "."
                "\n...\nNancy's mother reveals a dark: " + noun6_movies + "  a man named Freddy, " + surname_movies +
                " a child " + noun7_movies + " , was " + verb_ed_movies + " by parents.\nNow, he's " + verb_ing_movies +
                " their dreams seeking " + noun8_movies + ".\n...\nNancy tries to " + verb_movies + " her friends and face "
                "Freddy " + surname_movies + ".\nShe sets traps and succeeds in bringing him into the real world.\nShe "
                + verb_s_movies + " him, and her " + noun9_movies + " weakens him. Nancy defeats Freddy, and all seems well."
                "\nHowever, in the end, a " + adjective_movies + " twist suggests that Freddy's presence still lingers."
            )
        }


    print(moviesStories["nightmare_on_elm_street"])

if __name__ == '__main__':
    moviesStories()