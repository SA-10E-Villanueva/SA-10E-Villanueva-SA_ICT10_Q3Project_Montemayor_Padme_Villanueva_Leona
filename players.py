from pyscript import document

players_visible = False

players = [
    "ALOTAYA, Margaux J.",
    "ALWIT, David Andrew K.",
    "AQUINO, Shean Terrenze O.",
    "BRAR, Opdesh S.",
    "CHAVEZ, Cen Mar Gabriel D.",
    "CHUA, Reese Blesilda W.",
    "DE LOS SANTOS, Samuel Joshua",
    "ESTABILLO, Carl Jaden M.",
    "FANER, Janinna Arelie F.",
    "FERNANDEZ, Lesvie Mae A.",
    "GALE, Benjamin Miguel B.",
    "GARCIA, Joshua Melroy",
    "GILL, Ekamnoor K.",
    "KAUR, Simrat",
    "LAEDA, Lewis Ezekiel B.",
    "LUSICA, Alyza Kate O.",
    "MACALA, Sophia Issabel C.",
    "MACAS, Zaia Chryzelle D.",
    "MARANAN, Kaitlin Pia G.",
    "MONTEMAYOR, Padme Havilah A.",
    "MUSOR, Hanna Yasmin M.",
    "OMNES, Wilwen Benedict P.",
    "OREIRO, Rochel M.",
    "PLATON, Travis Reiley",
    "RAMIREZ, Aion P.",
    "RAZONABLE, Matt Sky L.",
    "SALVADOR, Eris Russell I.",
    "SALVADOR, Toni Rianne M.",
    "SILLEZA, Lucilind A.",
    "TIWARI, Kushdeep S.",
    "VILLANUEVA, Sofia Leona S."
]

def toggle_players(event):
    global players_visible

    output = document.getElementById("output")
    button = document.getElementById("toggleBtn")

    if not players_visible:
        player_list = "<br>".join([f"{i+1}. {name}" for i, name in enumerate(players)])
        output.innerHTML = player_list
        button.innerText = "HIDE PLAYERS"
        players_visible = True
    else:
        output.innerHTML = ""
        button.innerText = "SHOW PLAYERS"
        players_visible = False