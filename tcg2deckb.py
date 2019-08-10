#!/usr/bin/python

import sys
import pandas

if len(sys.argv) == 3:
    tcgList = pandas.read_csv(sys.argv[1])
    output = sys.argv[2]

    tcgList.rename(columns={
    "Quantity":"Count",
    "Set":"Edition",
    "Printing":"Foil"}, 
    errors="raise", inplace=True)

    tcgList = tcgList[[
    "Count",
    "Name",
    "Edition",
    "Language",
    "Foil"]]

    # This set replacement list is probably not complete
    tcgList["Edition"].replace(
        {"Magic 2015 (M15)":"Magic 2015 Core Set",
        "Magic 2014 (M14)":"Magic 2014 Core Set",
        "Magic 2013 (M13)":"Magic 2013",
        "Magic 2012 (M12)":"Magic 2012",
        "Magic 2011 (M11)":"Magic 2011",
        "Magic 2010 (M10)":"Magic 2010",
        "10th Edition":"Tenth Edition",
        "9th Edition":"Ninth Edition",
        "8th Edition":"Eighth Edition",
        "7th Edition":"Seventh Edition",
        "Modern Masters 2015":"Modern Masters 2015 Edition",
        "Modern Masters 2017":"Modern Masters 2017 Edition",
        # For some stupid reason the TCGPlayer app groups all Duel Deck Anthology 
        # cards into the "Duel Deck Anthology" set instead of the deck spesific sets.
        "Duel Decks: Anthology": "Duel Decks Anthology, Divine vs. Demonic",
        # This replaces all of them with the DvsD set which seems to be enough for
        # Deckbox to import the cards, though the set will be "undefined" so you'll
        # have to fix that by hand ;__; sorry
        "Launch Party & Release Event Promos":"Launch Parties",
        "Ravnica Allegiance: Guild Kits":"Ravnica Allegiance Guild Kit",
        "Guilds of Ravnica: Guild Kits":"Guilds of Ravnica Guild Kit",
        "Magic Game Night":"Game Night",
        "Coldsnap Theme Deck Reprints":"Coldsnap Theme Decks",
        "Timeshifted":"Time Spiral \"Timeshifted\""
        },inplace=True)
    
    #Remove bracketed ()[] parts from card names
    tcgList["Name"].replace(to_replace=r'[\[\(].*[\]\)]', value="", inplace=True, regex=True)

    tcgList["Foil"].replace({"Normal":""},inplace=True)

    tcgList.to_csv(output, index=False)
    print ("DONE")

else:
    print("Usage:")
    print("tcg2deckb.py [input] [output]")
