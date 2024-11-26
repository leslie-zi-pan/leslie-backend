from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    """Handles incoming requests to the Cloud Run service."""
    if request.method == 'POST':
        # Process POST request data (if any)
        data = request.get_json()

        # ... process the data ...
        return f'Data received and processed! {data}', 200

    # For GET requests or other methods
    return 'Hello from Cloud Run!', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))