from ml_models import app, logger as LOG

import spacy
from flask import jsonify

# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_md")


@app.route("/entities/<string:sentence>", methods=['GET'])
def entities(sentence):
    LOG.info("request entities for word:{} ".format(sentence))
    doc = nlp(sentence)

    # document level
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    return jsonify(entities=ents)


@app.route("/compare/<string:word1>/<string:word2>", methods=['GET'])
def compare(word1, word2):
    token1 = nlp(word1)
    token2 = nlp(word2)

    return jsonify(similarity=token1.similarity(token2))
