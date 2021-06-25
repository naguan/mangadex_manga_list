# mangadex_manga_reading_list
Calls mangadex api so that you can create a csv of your read list or update read status of manga

To use:

In terminal, enter 'python3 main.py'

Login with your MD credentials and follow prompts.

When updating manga read status, make sure you use enter the name of the manga as accuarately as possible

There is a secret input 3 that allows for the input of a dict of manga names and thier wanted 'read' statuses.
        -Most just the beginning infrastructure for using an input file
        -needs special to_add.py with the dicts in file
        -creates a csv with the manga that could not have its read status updated due to not being able to find its uuid in the mangadex database

TODO list that will grow eventually:

be able to create list with wanted read status, instead of all

front end component -> flask project?
