from flask import Flask, make_response
from web_scraping import postContent

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
                 consumoDeCombustivel):

        headers = {"Content-Type": "application/json",
                   "Access-Control-Allow-Origin": "*",
                   "Access-Control-Allow-Methods": "GET"}

        content = postContent(saida, destino, valorCombustivel, consumoCombustivel)

        return make_response(content, 200, headers=headers)
    
    flaskApp.run()
