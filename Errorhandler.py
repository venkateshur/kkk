import requests
import logging


class ErrorHandler(object):
    def __init__(self, api: str, client_code: str = "", product_code: str = ""):
        self.api = api
        self.client_code = client_code
        self.product_code = product_code
        self.exception_type = None
        self.exception_message = None
        self.exception_type = None
        self.exception = None
        self.logger = None

    def format_exception(self):
        self.exception = {"type": self.exception_type, "error": self.exception_message}

    def init_logger(self) -> logging:
        logger = logging.getLogger("ErrorHandler")
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
        logger.addHandler(handler)
        self.logger = logger

    def post_error(self):
        try:
            self.format_exception()
            response = requests.post(self.api, json=self.exception)
            print(response.status_code)
        except Exception as ex:
            print(ex)
            self.logger("Post call failed with error: " + str(ex))
            raise ex



