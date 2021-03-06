"""Provides the functions for the buttons!"""

def tip_notifier() -> None:
    """Sends a randomized tip."""
    from win10toast import ToastNotifier
    from typing import List
    from random import randint
    tips_list: List[str] = ["Use your school calendar for more than hw!!! It will force you to look at what you need to do whenever you look at social plans!", "Study right before you sleep! It is scientifically proven that studying right before you sleep helps your brain process the information!", "If you’ve got a big assignment, like a final paper, complete a bit of the project every few days. Write a paragraph or two each night.", "Come up with a system! Do you keep one big binder for all your classes with sorted pages? Or do you prefer separate notebooks and a folder for handouts? Keep it simple! This will help you continue to use the system over time.", "When will you do your hw? Find the best time for YOU.", "It takes workers an average of 25 minutes to get back to the task at hand after an interruption. Turn off your phone and silence social media so you can concentrate on the homework tasks at hand.", "Be honest with yourself about how long things actually take. Estimating that reading a history chapter will take an hour and a response will take thirty more minutes will help you plan how you spend your time.", "Spare time after class? Use the time to ask your teacher about tricky concepts and to do a little homework.", "Study a little every day. You might remember the vocab list long enough to ace the quiz when you cram, but you can't possibly cover the whole semester at once.", "A rough start to the semester can be coped with. Check your grades regularly online and get a tutor if you need one.", "Make a friend in every class. It gives you a study buddy and someone to hang with after!", "Spaced repitition involves breaking up information into small chunks and reviewing them over a long period of time. Learn a few bits of knowledge each day and review each lesson before starting anything new.", "Turn the details you need to remember into an easy-to-recite acronym! PEMDAS is an excellent example!", "Write your notes! Research suggests we store information better if we write it by hand than when we type it. Consider recopying the most important notes from the semester onto a new sheet of paper as method of studying!", "Quizzing yourself is a great way to prepare for evaluations! Use a stopwatch to simulate the test time limit.", "Reward yourself after a tough study session! Knowing there’s something to look forward to makes it easier to keep going!", "Get some caffeine! Whether it's coffee, soda, or tea, research suggests the amount of caffeine in a cup or two of coffee boosts attention and alertness.", "When there’s a textbook full of equations to memorize, it can be tempting to stay up all night. Resist this. Though it sounds smart, it actually can lead to a greater sensitivity to stress and a higher rate of forgetfulness.", "Some people are early birds, some are night owls. Some people need a study buddy, while others prefer to study alone. Experiment to find what study method is most effective for you", "Drink lots of water! Hydration improves memory and focus!"]
    tip: str = tips_list[randint(0, (len(tips_list) - 1))]
    toast = ToastNotifier()
    toast.show_toast("Study tip!", tip, duration=20,icon_path="icon.ico")


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


def wiki_summarizer() -> None:
    import wikipedia
    thing_of_interest: str = input()
    summary_result: str = wikipedia.summary(thing_of_interest)
    URL: str = (wikipedia.page(thing_of_interest)).url
    print(summary_result.strip())
    print("")
    print("")
    print("Do you want more information? Visit this link!")
    print("")
    print(URL)

# Something must be said in a use situation in which it is explained that if wikipedia turns up numerous results, they need to be more specific. Also, uses print, so this must be fixed.

# Consideration... Simpl...ish button series which says some of the best places to study at UNC, NCState, and Duke?