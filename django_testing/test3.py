import sys

def main() -> None:
    """Entrypoint to program"""
    translation_interactive()


def translation_interactive() -> None:                 #### VERY IMPORTANT : USES PRINT AT END... MUST OUTPUT TEXT TO WEBSITE IF IT IS TO BE USED INSTEAD ####
    """Translation function. Accepts a text, an input language, and an output language from English, Portuguese, Spanish, and Chinese."""
    from translate import Translator
    words = sys.argv[1]
    lang1 = sys.argv[2]
    lang2 = sys.argv[3]
    text: str = "%s" % (words)
    input_language: str = "%s" % (lang1)
    output_language: str = "%s" % (lang2)
    if output_language == "english" or output_language == "English":
        output_language = "en"
    elif output_language == "Spanish" or output_language == "spanish":
        output_language = "es"
    elif output_language == "portuguese" or output_language == "Portuguese":
        output_language = "pt"
    elif output_language == "chinese" or output_language == "Chinese" or output_language == "Mandarin" or output_language == "mandarin":
        output_language = "zh"
    else:
        if output_language != "en" and output_language != "es" and output_language != "pt" and output_language != "zh":
            print("Invalid language : Our choices are English, Spanish, Portuguese, and Chinese.")
    if input_language == "english" or input_language == "English":
        input_language = "en"
    elif input_language == "Spanish" or input_language == "spanish":
        input_language = "es"
    elif input_language == "portuguese" or input_language == "Portuguese":
        input_language = "pt"
    elif input_language == "chinese" or input_language == "Chinese" or input_language == "Mandarin" or input_language == "mandarin":
        input_language = "zh"
    else:
        if input_language != "en" and input_language != "es" and input_language != "pt" and input_language != "zh":
            print("Invalid language : Our choices are English, Spanish, Portuguese, and Chinese.")
    translator= Translator(from_lang = input_language, to_lang = output_language)
    translation = translator.translate(text)
    print(translation)


# def email_sender2() -> None:
#     """Sends a zoom link."""
#     import yagmail
#     receiver: str = " %s " % (sys.argv[2])
#     receiver_list = receiver.split()
#     body = " %s " % (sys.argv[1]) # Zoom link will go here, inputted by the user
#     for email in receiver_list:
#         yag = yagmail.SMTP("studyquarantips@gmail.com", "#hackDuke2020CEN")
#         yag.send(
#             to=email,
#             subject="Zoom link for study group!",
#             contents=body, 
#         )




if __name__ == "__main__":
    main()