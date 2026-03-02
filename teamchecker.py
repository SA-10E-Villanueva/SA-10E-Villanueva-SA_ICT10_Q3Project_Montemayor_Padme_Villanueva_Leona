from pyscript import display, document

def check_intrams(e):

    document.getElementById("output").innerHTML = ""
    document.getElementById("image").innerHTML = ""

    # User input
    reg_status = document.querySelector('input[name="reg_status"]:checked').value
    med_status = document.querySelector('input[name="med_status"]:checked').value
    grade = int(document.getElementById("grade").value)
    section = document.getElementById("class_section").value

    # Eligibility checks
    if reg_status != "yes":
        display(
            "Not eligible: You are not registered for Intramurals. Please ask your PE teacher about the registration.",
            target="output"
        )
    elif med_status != "yes":
        display(
            "Not eligible: Medical clearance is required. Please visit the clinic.",
            target="output"
        )
    elif grade < 7 or grade > 10:
        display(
            "Not eligible: Only students in grades 7–10 can join Intramurals.",
            target="output"
        )
    else:
        # Chiikawa images for each team
        teams = {
            "emerald": {
                "msg": "Congratulations! You are part of Chiikawa!",
                "img": "https://i.pinimg.com/736x/75/c9/6f/75c96f4bff188b0efe21c821239d14b9.jpg"
            },
            "ruby": {
                "msg": "Congratulations! You are part of Hachiware!",
                "img": "https://i.pinimg.com/736x/32/d3/21/32d321735aada71a6ae251894240d901.jpg"
            },
            "sapphire": {
                "msg": "Congratulations! You are part of Usagi!",
                "img": "https://i.pinimg.com/736x/48/98/dc/4898dccac48a64dd6edc0ec9108d3c7f.jpg"
            },
            "topaz": {
                "msg": "Congratulations! You are part of Momonga!",
                "img": "https://i.pinimg.com/736x/e8/f7/5a/e8f75a054eaf530fb07e1251514b5182.jpg"
            }
        }

        # Display the message
        display(teams[section]["msg"], target="output")

        # Display the team image
        document.getElementById("image").innerHTML = f'''
            <img src="{teams[section]["img"]}" 
                 alt="Team Image" 
                 width="150" 
                 style="border-radius:15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
        '''
