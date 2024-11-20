import nltk
# noinspection PyUnresolvedReferences
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
# noinspection PyUnresolvedReferences
from nltk import pos_tag, ne_chunk
# noinspection PyUnresolvedReferences
from nltk.chunk import RegexpParser
import requests as r
from requests import session

# Downloading resources
nltk.download('words')
ENDPOINT = "https://api.endlessmedical.com/v1/"
session_id = None


def do_stuff(text):
    global session_id
    time, pos_tag_list = process(text)

    # Start API session
    session_id = r.get(f"{ENDPOINT}dx/InitSession")
    if session_id.status_code == 200:
        session_id = session_id.json()["SessionID"]
        def accept_terms():
            params = {
                "SessionID": str(session_id),
                "passphrase": "I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com"
            }
            terms = r.post(f"{ENDPOINT}dx/AcceptTermsOfUse", params=params)
            if terms.status_code == 200:
                pass
            else:
                accept_terms()
        accept_terms()
    handle_api()


def process(text_):

    # Word Tokenization
    words = word_tokenize(text_)

    # Stop Words Removal
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Part of Speech (POS) Tagging
    pos_tags = pos_tag(filtered_words)
    print("POS Tags:", pos_tags)
    return calculate_time(pos_tags), pos_tags

    # Optional Stuff if needed later


    # Named Entity Recognition (NER)
    # named_entities = ne_chunk(pos_tags, binary=True)

    # Chunking for Specific Patterns
    # pattern = "NP: {<NNP>+}"  # Custom pattern to capture proper nouns
    # parser = RegexpParser(pattern)
    # chunked = parser.parse(pos_tags)

    # # Extracting Matches from Chunks
    # for subtree in chunked.subtrees():
    #     if subtree.label() == "NP":
    #         pass  # Placeholder if further processing is needed


def calculate_time(pos_list):
    # Calculate time
    time = ""
    index = 0
    for i in pos_list:
        if i[1] == "CD":
            n_index = index + 1
            after_word = pos_list[n_index][0].lower()
            match after_word:
                case "day":
                    print("In first day loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "days":
                    print("In second day loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "week":
                    print("In first week loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "weeks":
                    print("In second week loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "month":
                    print("In first month loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "months":
                    print("In second month loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "year":
                    print("In first year loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case "years":
                    print("In second year loop")
                    time += f"{i[0]} {list(after_word.lower())[0]}"
                    break
                case _:
                    print("Didn't match! Going to next loop.")
                    if pos_list[n_index][1] == "CD":
                        next_word = pos_list[n_index + 1][0].lower()
                        match next_word:
                            case "day":
                                print("In third day loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "days":
                                print("In fourth day loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "week":
                                print("In third week loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "weeks":
                                print("In fourth week loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "month":
                                print("In third month loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "months":
                                print("In fourth month loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "year":
                                print("In third year loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case "years":
                                print("In fourth year loop")
                                time += f"{i[0]} {list(next_word.lower())[0]}"
                                break
                            case _:
                                print("No time given.")
                                break
                    break

        index += 1
    if time is not None:
        print(time)
        return time
    else:
        pass


def handle_api():
    possible_symptoms = r.get(f"{ENDPOINT}dx/GetFeatures")
