from flask import Flask, request, jsonify
import os
import whisper

app = Flask(__name__)

# Load the Whisper model
# model = None


@app.route("/upload-audio", methods=["POST"])
def upload_audio():

    model = whisper.load_model("base")

    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Save the file
    file_path = os.path.join("/tmp", file.filename)
    file.save(file_path)

    # Transcribe the audio file using Whisper
    try:
        result = model.transcribe(file_path)

        # Clean up the saved file
        os.remove(file_path)

        return jsonify({"transcription": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
