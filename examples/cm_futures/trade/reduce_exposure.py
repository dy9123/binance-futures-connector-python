import logging
from binance.cm_futures import CMFutures
from binance.error import ClientError

# Create a client instance with API key and secret
key = ""
secret = ""

client = CMFutures(key=key, secret=secret)

try:
    # Call reduce_exposure function with appropriate parameters
    response = client.monitor_risk_exposure(symbol="BTCUSD_PERP", portion=0.5, threshold = 50)
    # Log the response from reduce_exposure function
    logging.info(response)
except ClientError as error:
    # Handle ClientError exceptions and log error details
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
