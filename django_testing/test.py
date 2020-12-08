import sys

def main() -> None:
    """Entrypoint to program"""
    email_sender2()
    print("sent!")


def email_sender2() -> None:
    """Sends a zoom link."""
    import yagmail
    receiver: str = " %s " % (sys.argv[2])
    receiver_list = receiver.split(", ")
    body = " %s " % (sys.argv[1]) # Zoom link will go here, inputted by the user
    for email in receiver_list:
        yag = yagmail.SMTP("studyquarantips@gmail.com", "#hackDuke2020CEN")
        yag.send(
            to=email,
            subject="Zoom link for study group!",
            contents=body, 
        )

if __name__ == "__main__":
    main()