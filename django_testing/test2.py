import sys

def main() -> None:
    """Entrypoint to program"""
    tip_notifier()
    print("doneeee!!")


def tip_notifier() -> None:
    """Sends a randomized tip."""
    from win10toast import ToastNotifier
    from typing import List
    from random import randint
    tips_list: List[str] = ["Use your school calendar for more than hw!!! It will force you to look at what you need to do whenever you look at social plans!", "Study right before you sleep! It is scientifically proven that studying right before you sleep helps your brain process the information!", "If you’ve got a big assignment, like a final paper, complete a bit of the project every few days. Write a paragraph or two each night.", "Come up with a system! Do you keep one big binder for all your classes with sorted pages or separate notebooks?", "When will you do your hw? Find the best time for YOU.", "It takes workers an average of 25 minutes to get back to the task at hand after an interruption. Turn off your phone!", "Be honest with yourself about how long things actually take.", "Spare time after class? Use the time to ask your teacher about tricky concepts and to do a little homework.", "Study a little every day. You might remember the vocab list long enough to ace the quiz when you cram, but you can't possibly cover the whole semester at once.", "A rough start to the semester can be coped with. Check your grades regularly online and get a tutor if you need one.", "Make a friend in every class. It gives you a study buddy and someone to hang with after!", "Spaced repitition involves breaking up information into small chunks and reviewing them over a long period of time. Do this!", "Turn the details you need to remember into an easy-to-recite acronym! PEMDAS is an excellent example!", "Write your notes! Research suggests we store information better if we write it by hand than when we type it.", "Quizzing yourself is a great way to prepare for evaluations! Use a stopwatch to simulate the test time limit.", "Reward yourself after a tough study session! Knowing there’s something to look forward to makes it easier to keep going!", "Get some caffeine! Whether it's coffee, soda, or tea, research suggests the amount of caffeine in a cup or two of coffee boosts attention and alertness.", "When there’s a textbook full of equations to memorize, it can be tempting to stay up all night. Resist this. Though it sounds smart, it increases forgetfulness and stress.", "Some people are early birds, some are night owls. Some people need a study buddy, while others prefer to study alone. Experiment to find what study method is most effective for you", "Drink lots of water! Hydration improves memory and focus!"]
    tip: str = tips_list[randint(0, (len(tips_list) - 1))]
    toast = ToastNotifier()
    toast.show_toast("Study tip!", tip, duration=20,icon_path="icon.ico")


if __name__ == "__main__":
    main()