import sys

def main() -> None:
    """Entrypoint to program"""
    wiki_summarizer()


def wiki_summarizer() -> None:
    import wikipedia
    thing_of_interest = "%s" % (sys.argv[1])
    summary_result: str = wikipedia.summary(thing_of_interest)
    URL: str = (wikipedia.page(thing_of_interest)).url
    print(summary_result.strip())
    print("")
    print("")
    print("Do you want more information? Visit this link!")
    print("")
    print(URL)


# def wiki_summarizer_email() -> None:
#     import wikipedia
#     thing_of_interest: str = " %s " % (sys.argv[1])
#     summary_result: str = wikipedia.summary(thing_of_interest)
#     URL: str = (wikipedia.page(thing_of_interest)).url
#     print(summary_result.strip())
#     print("")
#     print("")
#     print("Do you want more information? Visit this link!")
#     print("")
#     print(URL)


if __name__ == "__main__":
    main()