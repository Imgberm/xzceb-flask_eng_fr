import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # implement a method that uses the appropriate translation function through the package you created in the previous part. The function should take the English text as input through the request parameter and return a string.
    translatedText = translator.englishToFrench(textToTranslate)
    return "Translated text to French: " + translatedText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.frenchToEnglish(textToTranslate)
    return "Translated text to English: " + translatedText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
