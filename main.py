from pathlib import Path
import os

from flask import Flask, jsonify, request, send_file

# Keep the original conversion classes in process.py.
from process import Decimal, Binary, Octal, HexaDecimal

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "konverter_bilangan.html"

app = Flask(__name__)

CONVERTER_CLASSES = {
    "decimal": Decimal,
    "binary": Binary,
    "octal": Octal,
    "hexadecimal": HexaDecimal,
}


@app.get("/")
def home():
    """Serve the single-file HTML interface."""
    if not HTML_FILE.is_file():
        return (
            "konverter_bilangan.html tidak ditemukan. "
            "Letakkan file HTML di folder yang sama dengan main.py.",
            500,
        )
    return send_file(HTML_FILE, mimetype="text/html")


@app.post("/api/convert")
def convert():
    """Receive JSON from the browser and call the original process.py class."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "success": False,
            "error": "Permintaan tidak valid. Data harus dikirim sebagai JSON.",
        }), 400

    selected_base = payload.get("base")
    raw_value = payload.get("value")

    if selected_base not in CONVERTER_CLASSES:
        return jsonify({"success": False, "error": "Basis input tidak dikenal."}), 400
    if not isinstance(raw_value, str) or not raw_value.strip():
        return jsonify({"success": False, "error": "Masukkan angka terlebih dahulu."}), 400
    if len(raw_value) > 4096:
        return jsonify({"success": False, "error": "Input terlalu panjang."}), 400

    try:
        converter = CONVERTER_CLASSES[selected_base](raw_value.strip())
        results = converter.output()

        if not results:
            return jsonify({
                "success": False,
                "error": "Input tidak sesuai dengan aturan basis yang dipilih.",
            }), 400

        return jsonify({
            "success": True,
            "source_base": selected_base,
            "source_value": converter.raw,
            "results": results,
        })
    except (ValueError, TypeError, KeyError, IndexError):
        return jsonify({
            "success": False,
            "error": "Input tidak sesuai dengan aturan basis yang dipilih.",
        }), 400
    except Exception:
        app.logger.exception("Unexpected conversion error")
        return jsonify({
            "success": False,
            "error": "Terjadi kesalahan saat melakukan konversi.",
        }), 500


if __name__ == "__main__":
    # Local development only. Vercel imports the top-level `app` object.
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="127.0.0.1", port=port, debug=False)
