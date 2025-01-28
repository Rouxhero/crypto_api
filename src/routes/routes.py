"""Route definitions for the application."""
from src.core.server_routes import GetRoutes, PostRoutes, PutRoutes, DeleteRoutes
from src.controllers import *

routes = [

    GetRoutes("/", HomeControllerInstance.index),
    PostRoutes("/register", AuthControllerInstance.register),

]