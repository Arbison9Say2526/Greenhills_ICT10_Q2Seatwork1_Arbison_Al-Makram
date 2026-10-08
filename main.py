from pyscript import display, document

destinations = ['Sulu', 'El Nido', 'Bohol', 'Cebu', 'Boracay']
nicknames = ['Land of Pearls','Heaven on Earth','Jewel of the Philippines','Queen City of the South','Island Born of Paradise']

def get_nickname(e):
    index = int(document.getElementById('destinationSelect').value)

    place = destinations[index]
    nickname = nicknames[index]

    if place == 'El Nido':
        result_text = f"Yep, that's {place}, \"{nickname}.\""

    else:
        result_text = f"Yep, that's {place}, The \"{nickname}.\""

        # i used conditionals because simply i disliked the grammar on el nido's "the 'heaven on earth.'". 
    

    display(result_text, target='div1', append=False) 
    
    # Sir, i used append=False because the previous output had
    # the tendency to display multiple times when clicked. This append=false makes sure that only one output is shown.