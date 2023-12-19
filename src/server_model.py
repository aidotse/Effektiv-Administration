from flask import Flask, request, jsonify
from flask_cors import CORS

from model_wrapper import prompt_model
from utils.query.query import preform_query
app = Flask(__name__)
CORS(app)  


@app.route('/prompt', methods=['POST'])
def post_example():
    data = request.get_json()  # Assuming the incoming data is in JSON format
    if 'prompt' not in data:
        return jsonify({"error: no prompt received!"})

    usr_prompt = data['prompt']
    # You can process the received data here
    query_string = usr_prompt
    result = preform_query(query_string)
    #print("dokument som hittades: ",[res["filepath"] for res in result])
    doc_names = [file['filepath'][12:] for file in result]
    # print("results:")
    print(str(result))
    res = prompt_model(str(result), usr_prompt)

    # Responding back
    response_data = {'answer': res, 'prompt': usr_prompt, 'doc_names': doc_names}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
