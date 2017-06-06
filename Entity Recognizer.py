import pycrfsuite
import shutil,io
import spacy
#import Span
nlp = spacy.load('en')

def _from_json_to_crf(json_eg, spacy_nlp):
        # type: (Tuple[Text, List[Tuple[int, int, Text]]], Language) -> List[Tuple[Text, Text, Text]]
        """Takes the json examples and switches them to a format which crfsuite likes."""
        from spacy.language import Language
        from spacy.gold import GoldParse
        print (json_eg)

        doc = spacy_nlp(json_eg[0].decode('utf-8'))
        entity_offsets = json_eg[1]
        gold = GoldParse(doc, entities=entity_offsets)
        ents = [l[5] for l in gold.orig_annot]
        BILOU_flag=False#True
        if not BILOU_flag:
            def ent_clean(entity):
                if entity.startswith('B-') or entity.startswith('I-') or entity.startswith('U-') or entity.startswith(
                        'L-'):
                    return entity[2:]
                else:
                    return entity
        else:
            def ent_clean(entity):
                return entity

        crf_format = [(doc[i].text, doc[i].tag_, ent_clean(ents[i])) for i in range(len(doc))]
        return crf_format
