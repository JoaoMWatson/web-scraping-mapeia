from flask import Flask, Response, request, make_response
from PostElements import PostElements

flaskApp = Flask(__name__)

if __name__ == "__main__":
    @flaskApp.route(
        "/api/rotas/",
        methods=['GET']
    )
    def rotas():
        getJsonBody = request.get_json(force=True)

        saida = getJsonBody['saida']
        destino = getJsonBody['destino']
        valorCombustivel = getJsonBody['valorCombustivel']
        consumoCombustivel = getJsonBody['consumoCombustivel']

        postElements = PostElements(saida, destino, valorCombustivel, consumoCombustivel)

        clientResponse = postElements.postElements()

        resp = make_response(clientResponse, 200)

        return resp

    flaskApp.run()
