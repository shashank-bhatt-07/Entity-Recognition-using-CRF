import pycrfsuite
import shutil,io
import spacy
from data import getData
from words_to_feature import sent2features,sent2labels
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

train_data=getData()
##convert the train data into crf format i.e tagging of each word in each document of train data
dataset = [_from_json_to_crf(q, nlp) for q in train_data]

print (sent2features(dataset[0])[0])


#convert text to features and labels i.e entitys 
x = [sent2features(s) for s in dataset]
y = [sent2labels(s) for s in dataset]


trainer = pycrfsuite.Trainer(verbose=False)

for X, Y in zip(x, y):
    trainer.append(X,Y)


trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 50,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
})

print (trainer.params())

trainer.train('entity_model.crfsuite')
print (trainer.logparser.last_iteration)


# Make Predictions

tagger = pycrfsuite.Tagger()
tagger.open('entity_model.crfsuite')


doc = nlp('update email of google account'.decode('utf-8'))##id,Id
crf_format = [(doc[i].text, doc[i].tag_,'N/A') for i in range(len(doc))]
print(crf_format)


print("Predicted:", ' '.join(tagger.tag(sent2features(crf_format))))


# print the word and entity associated with it
ents=tagger.tag(sent2features(crf_format))
for i in range(0,len(crf_format)):
    if ents[i]!='O':
        print (crf_format[i][0])
        print (ents[i])




