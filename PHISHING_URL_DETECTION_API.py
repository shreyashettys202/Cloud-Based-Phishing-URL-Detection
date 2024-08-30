from flask import Flask as CustomFlaskApp, request as req_handler, jsonify as json_response
import joblib as job_lib
import pandas as pd_tool

app = CustomFlaskApp(__name__)

phishing_model = job_lib.load('neuralnetwork.sav')
text_vectorizer = job_lib.load('tfidf_vectorizer.sav')

@app.route('/phishing-detection', methods=['POST'])
def detect_phishing():
    request_data = req_handler.json
    target_url = request_data.get('website')
    url_vectorized = text_vectorizer.transform([target_url])
    url_dataframe = pd_tool.DataFrame(url_vectorized.toarray(), 
                                      columns=[f'feature_{i}' for i in range(url_vectorized.shape[1])])
    prediction_result = phishing_model.predict(url_dataframe)
    
    if prediction_result == 0:
        result = "BAD"
    elif prediction_result == 1:
        result = "GOOD"

    return json_response({'detection_result': result})

if __name__ == '__main__':
    app.run(port=8666 ,debug=True)

