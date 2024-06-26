
from starlette.responses import JSONResponse
from starlette import status


# Status Responses

# COLLECTION FOR ROUTER  - responses=ROUTER_API_RESPONSES_OPEN_API
ROUTER_API_RESPONSES_OPEN_API = {
        status.HTTP_200_OK: {
            "description": "OK",
        },
        status.HTTP_201_CREATED: { 
            "description": "CREATED",
        },
        status.HTTP_202_ACCEPTED: {  
            "description": "ACCEPTED",
        },
        status.HTTP_204_NO_CONTENT: {  
            "description": "NO_CONTENT",
        },
        status.HTTP_401_UNAUTHORIZED: {  
            "description": "UNAUTHORIZED",
        },
    }

class OkJSONResponse(JSONResponse):
    def __init__(self):
        super().__init__(self)
        self.status_code = status.HTTP_200_OK
        self.background = None
        self.content = {"datail": "OK"}

class CreatedJSONResponse(JSONResponse):
    def __init__(self):
        super().__init__(self)
        self.status_code = status.HTTP_200_OK
        self.background = None
        self.content = {"datail": "CREATED"}
class NoContentJSONResponse(JSONResponse):
    def __init__(self):
        super().__init__(self)
        self.status_code = status.HTTP_204_NO_CONTENT
        self.background = None
        self.content = {"datail": "NO_CONTENT"}

class AcceptedJSONResponse(JSONResponse):
    def __init__(self):
        super().__init__(self)
        self.status_code = status.HTTP_202_ACCEPTED
        self.background = None
        self.content = {"datail": "ACCEPTED"}

class BadRequestJSONResponse(JSONResponse):
    def __init__(self):
        super().__init__(self)
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.background = None
        self.content = {"datail": "BAD_REQUEST"}