from flask import Flask, make_response
from PostElements import PostElements

flaskApp = Flask(__name__)
flaskApp.config["DEBUG"] = True

if __name__ == "__main__":
    @flaskApp.route(
        "/api/rotas/<string:saida>/<string:destino>/<float:valorCombustivel>/<float:consumoCombustivel>",
        methods=['GET']
    )
    def rotas(saida,
              destino,
              valorCombutivel,
              consumoCombustivel):

        headers = {"Content-Type": "application/json",
                   "Access-Control-Allow-Origin": "*",
                   "Access-Control-Allow-Methods": "GET"}

        content = PostElements(saida, destino, valorCombutivel, consumoCombustivel)

        return make_response(content, 200, headers=headers)

    flaskApp.run()
