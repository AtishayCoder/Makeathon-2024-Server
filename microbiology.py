import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from nltk.chunk import RegexpParser

# Downloading resources
nltk.download('words')


def micro(text_):

    # Word Tokenization
    words = word_tokenize(text_)

    # Stop Words Removal
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Part of Speech (POS) Tagging
    pos_tags = pos_tag(filtered_words)
    print("POS Tags:", pos_tags)
    start_processing(pos_tags)

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


def start_processing(pos_list):
    # Calculate time
    time = ""
    index = 0
    for i in pos_list:
        if i[1] == "CD":
            n_index = index + 1
            after_word = pos_list[n_index][0].lower()
            match after_word:
                case "day":
                    time += f"{i[0]} {after_word.lower()}"
                case "days":
                    time += f"{i[0]} {after_word.lower()}"
                case "week":
                    time += f"{i[0]} {after_word.lower()}"
                case "weeks":
                    time += f"{i[0]} {after_word.lower()}"
                case "month":
                    time += f"{i[0]} {after_word.lower()}"
                case "months":
                    time += f"{i[0]} {after_word.lower()}"
                case "year":
                    time += f"{i[0]} {after_word.lower()}"
                case "years":
                    time += f"{i[0]} {after_word.lower()}"
                case default:
                    print("Error, " + after_word.lower())
        index += 1

    print(time)

micro("I have backache for 2 months.")
