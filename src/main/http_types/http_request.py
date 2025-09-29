class HttpRequest():
    def __init__(self, body: dict, params: dict, headers: dict):
        self.body = body
        self.params = params
        self.headers = headers