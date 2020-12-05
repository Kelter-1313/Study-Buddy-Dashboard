"""This is the program which controls the sending of study tips!"""

def email_sender() -> None:
    import yagmail
    receiver = "kelter1313@gmail.com", "demarcoal72@gmail.com"
    body = "This is the body"

    yag = yagmail.SMTP("studyquarantips@gmail.com", "#hackDuke2020CEN")

    yag.send(
        to=receiver,
        subject="This is Christian!",
        contents=body, 
    )