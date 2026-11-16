# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from deep_translator import GoogleTranslator

# app = Flask(__name__)
# CORS(app)

# LANGUAGES = {
#     "auto": "Auto Detect", "en": "English", "hi": "Hindi",
#     "fr": "French", "de": "German", "es": "Spanish",
#     "it": "Italian", "pt": "Portuguese", "ja": "Japanese",
#     "ko": "Korean", "zh-CN": "Chinese (Simplified)",
#     "ar": "Arabic", "ru": "Russian", "nl": "Dutch",
#     "tr": "Turkish", "pl": "Polish", "sv": "Swedish",
#     "da": "Danish", "fi": "Finnish", "no": "Norwegian"
# }

# @app.route("/")
# def home():
#     return send_from_directory(".", "index.html")

# @app.route("/languages")
# def get_languages():
#     return jsonify(LANGUAGES)

# @app.route("/translate", methods=["POST"])
# def translate():
#     data = request.get_json()
#     text = data.get("text", "").strip()
#     source = data.get("source", "auto")
#     target = data.get("target", "en")

#     if not text:
#         return jsonify({"error": "Please enter some text."}), 400
#     if source == target:
#         return jsonify({"error": "Please select two different languages."}), 400

#     try:
#         result = GoogleTranslator(source=source, target=target).translate(text)
#         return jsonify({"translation": result})
#     except Exception as error:
#         return jsonify({"error": str(error)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)

LANGUAGES = {
    "auto": "Auto Detect",
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-CN": "Chinese (Simplified)",
    "ar": "Arabic",
    "ru": "Russian",
    "nl": "Dutch",
    "tr": "Turkish",
    "pl": "Polish",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "no": "Norwegian"
}

# Convert language codes into names supported by deep-translator
LANGUAGE_NAMES = {
    "en": "english",
    "hi": "hindi",
    "fr": "french",
    "de": "german",
    "es": "spanish",
    "it": "italian",
    "pt": "portuguese",
    "ja": "japanese",
    "ko": "korean",
    "zh-CN": "chinese simplified",
    "ar": "arabic",
    "ru": "russian",
    "nl": "dutch",
    "tr": "turkish",
    "pl": "polish",
    "sv": "swedish",
    "da": "danish",
    "fi": "finnish",
    "no": "norwegian bokmål"
}

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/languages")
def get_languages():
    return jsonify(LANGUAGES)


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data.get("text", "").strip()
    source = data.get("source", "auto")
    target = data.get("target", "en")

    if not text:
        return jsonify({"error": "Please enter some text."}), 400

    if source == target:
        return jsonify({
            "error": "Please select two different languages."
        }), 400

    if target not in LANGUAGE_NAMES:
        return jsonify({"error": "Invalid target language."}), 400

    if source != "auto" and source not in LANGUAGE_NAMES:
        return jsonify({"error": "Invalid source language."}), 400

    try:
        source_name = (
            "auto" if source == "auto"
            else LANGUAGE_NAMES[source]
        )

        target_name = LANGUAGE_NAMES[target]

        result = GoogleTranslator(
            source=source_name,
            target=target_name
        ).translate(text)

        return jsonify({"translation": result})

    except Exception as error:
        print("Translation error:", error)
        return jsonify({
            "error": "Translation failed. Please try again later."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
