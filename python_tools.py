"""Provides the functions for the buttons!"""

def tip_notifier() -> None:
    """Sends a randomized tip."""
    from win10toast import ToastNotifier
    from typing import List
    from random import randint
    tips_list: List[str] = ["Use your school calendar for more than hw!!! It will force you to look at what you need to do whenever you look at social plans!", "Study right before you sleep! It is scientifically proven that studying right before you sleep helps your brain process the information!", "Cats are rad!", "If you’ve got a big assignment looming, like a research paper, stay motivated by completing a piece of the project every few days. Write one paragraph each night. Or, do 5 algebra problems from your problem set at a time, and then take a break.", "Come up with a system and keep to it. Do you keep one big binder for all your classes with color-coded tabs? Or do you prefer to keep separate notebooks and a folder for handouts? Keep the system simple—if it’s too fancy or complicated, you are less likely to keep it up everyday.", "When will you make the time to do your homework every day? Find the time of day that works best for you (this can change day-to-day, depending on your schedule!), and make a plan to hit the books.", "A study on workplace distractions found that it takes workers an average of 25 minutes to return to what they were working on pre-interruption. Try turning off your phone notifications or blocking Twitter (temporarily) on your computer so you can concentrate on the homework tasks at hand.", "When you’re looking at the homework you have to get done tonight, be realistic about how long things actually take. Gauging that reading a history chapter will take an hour and writing a response will take another 30 minutes will help you plan how you spend your time.", "Is your teacher finished lecturing, but you still have 10 minutes of class left? Get a jump on your chemistry homework while it’s still fresh in your mind. Or use the time to ask your teacher about concepts that were fuzzy the first time.", "Study a little every day. Cramming Spanish vocabulary for a quiz might work in the short-term, but when comes time to study for midterms, you’ll be back at square 1. You might remember the vocab list long enough to ace the quiz, but reviewing the terms later will help you store them for the long haul.", "A rough start to the semester doesn’t have to sink your GPA. Take proactive steps by checking your grades regularly online and getting a tutor if you need one.", "Make a friend in every class. It gives you a study buddy and someone to hang with after!"]
    tip: str = tips_list[randint(0, (len(tips_list) - 1))]
    toast = ToastNotifier()
    toast.show_toast("Study tip!", tip, duration=20,icon_path="icon.ico")

# def email_sender() -> None:
#    """Sends a zoom link."""
#    import yagmail
#    receiver = "kelter1313@gmail.com", "demarcoal72@gmail.com"
#     body = "" # Zoom link will go here, inputted by the user
#     yag = yagmail.SMTP("studyquarantips@gmail.com", "#hackDuke2020CEN")
#     yag.send(
#        to=receiver,
#        subject="Zoom link for study group!",
#        contents=body, 
#     )

def pomodoro_timer() -> None:
    """Initiates a pomodoro method timer."""
    from win10toast import ToastNotifier
    from time import sleep
    toast = ToastNotifier()
    toast.show_toast("Pomodoro Method!", "Starting a 25 minute pomodoro timer! You'll be sent another notification when the timer is up!", duration=20,icon_path="icon.ico")
    sleep(1500.0)
    toast.show_toast("Pomodoro Method!", "Your 25 minutes are up! Record what you got done and take a five minute break!", duration=20, icon_path="icon.ico")



def email_sender_with_input() -> None:
    """Sends a zoom link."""
    import yagmail
    receiver = input()
    reciever_list = receiver.split(", ")
    body = input() # Zoom link will go here, inputted by the user
    for email in reciever_list:
        yag = yagmail.SMTP("studyquarantips@gmail.com", "#hackDuke2020CEN")
        yag.send(
            to=email,
            subject="Zoom link for study group!",
            contents=body, 
        )

def translation_interactive() -> None:                 #### VERY IMPORTANT : USES PRINT AT END... MUST OUTPUT TEXT TO WEBSITE IF IT IS TO BE USED INSTEAD ####
    """Translation function. Accepts a text, an input language, and an output language from English, Portuguese, Spanish, and Chinese."""
    from translate import Translator
    text: str = input()
    input_language: str = input()
    output_language: str = input()
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