from flask import Flask, make_response
from PostElements import PostElements

flaskApp = Flask(__name__)

if __name__ == "__main__":
    @flaskApp.route(
        "/api/rotas/<saida>/<destino>/<valorCombustivel>/<consumoCombustivel>/",
        methods=['GET']
    )
    def rotas(saida, destino, valorCombustivel, consumoCombustivel):

        headers = {"Content-Type": "application/json",
                   "Access-Control-Allow-Origin": "*",
                   "Access-Control-Allow-Methods": "GET"}

        content = PostElements(
            saida, destino, valorCombustivel, consumoCombustivel)

        response_json = content.postElements()

        response = flaskApp.make_response(response_json, 200)

        return response

    flaskApp.run()
