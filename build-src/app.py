from flask import Flask, send_file, request, Response
from prometheus_client import start_http_server, Counter, generate_latest, Gauge
import logging
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

get_balance_gauge = Gauge('bitcoin_balance', 'The total balance of prod bitcoin wallet.')
get_block_number_gauge = Gauge('bitcoin_block_number', 'The block number of bitcoin.')


@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""

    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    RPCUSER = os.environ.get("RPCUSER")
    RPCPASSWORD = os.environ.get("RPCPASSWORD")

    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(RPCUSER, RPCPASSWORD, HOST, PORT))
    
    bitcoingetbalance = rpc_connection.getbalance()
    bitcoingetblocknumber = rpc_connection.getblockcount()


    try:
        get_balance_gauge.set(bitcoingetbalance)
        get_block_number_gauge.set(bitcoingetblocknumber)
    except Exception as e:
        logger.error("Failed to get balance metric. Exception: {}".format(e))

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')