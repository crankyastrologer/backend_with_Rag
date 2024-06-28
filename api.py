from init import cross_origin,app,request,jsonify
from RAG_chain import load,getResponse
rag_chain = load()
@app.route('/api', methods=['POST','OPTIONS','GET'])
@cross_origin()
def getans():
    data = request.get_json()
    print(data)
    if 'question' in data:
        question = str(data['question'])
        ans = getResponse(question,rag_chain)
        print(question)
        response = {
            'response': f'{ans}'
        }
        response = jsonify(response)

        return response

    else:
        return 403, "Question not found"


if __name__ == '__main__':

    app.run(debug=True)
