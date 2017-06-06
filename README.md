# Entity-Recognition-using-CRF
Create a customized model to identity the user defined entitys from the text
This CRF model is created for the user input where user wants to update his email id to some new email for a specific account name and we have to retrieve that account name and email from the text.

There are 3 files -

In data.py we are creating the dataset for entitys account name and email. Please stick to the format of the dataset. If it is wrong then predictions will be wrong.

In words_to_feature.py we are converting words to features as well as to labels i.e our entitys.

In Entity Recognizer.py we are creating the model.
