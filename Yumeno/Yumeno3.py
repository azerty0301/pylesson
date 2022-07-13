import markovify
import pandas as pd
import re



with open("model/text_model.json") as f:
    model = markovify.NewlineText.from_json(f.read())
    print(re.sub(" ","", model.make_short_sentence(100, tries=100)))
