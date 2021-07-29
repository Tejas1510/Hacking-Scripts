
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer
import spacy
import neologdn


class EnglishCorpus:
    # Preparation of morphological analyzer
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    # Pre-processing of line breaks and special characters
    def preprocessing(self, text: str) -> str:
        text = text.replace("\n", "")
        text = neologdn.normalize(text)

        return text

    # Divide sentences into sentences while retaining the results of morphological analysis
    def make_sentence_list(self, sentences: str) -> list:
        doc = self.nlp(sentences)
        self.ginza_sents_object = doc.sents
        sentence_list = [s for s in doc.sents]

        return sentence_list

    # Put a space between words
    def make_corpus(self) -> list:
        corpus = []
        for s in self.ginza_sents_object:
            tokens = [str(t) for t in s]
            corpus.append(" ".join(tokens))

        return corpus


def summarize_sentences(sentences: str, language="english") -> list:
    # Preparation sentences
    corpus_maker = EnglishCorpus()
    preprocessed_sentences = corpus_maker.preprocessing(sentences)
    preprocessed_sentence_list = corpus_maker.make_sentence_list(
        preprocessed_sentences)
    corpus = corpus_maker.make_corpus()
    parser = PlaintextParser.from_string(" ".join(corpus), Tokenizer(language))

    # Call the summarization algorithm and do the summarization
    summarizer = LexRankSummarizer()
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(document=parser.document,
                         sentences_count=len(corpus) * 2 // 10)

    return summary

def main():
    filepath = input("please input text's filepath->")
    with open(filepath) as f:
        sentences = f.readlines()
    sentences = ' '.join(sentences)

    summary = summarize_sentences(sentences)

    filepath_index = filepath.find('.txt')
    outputpath = filepath[:filepath_index] + '_summary.txt'

    with open(outputpath, 'w') as w:
        for sentence in summary:
            w.write(str(sentence) + '\n')


if __name__ == "__main__":
    main()