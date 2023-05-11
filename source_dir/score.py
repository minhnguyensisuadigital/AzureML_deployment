import json
from flair.data import Sentence
from flair.models import SequenceTagger
import os

def init():
    global model
    model = SequenceTagger.load(
        os.path.join(os.getenv("AZUREML_MODEL_DIR"), "flair_sample_model.pt")
    )


def run(request):
    print(request)
    text = json.loads(request)

    # Run inference
    sentence = Sentence(text["query"])
    model.predict(sentence)
    return sentence.to_tagged_string()
