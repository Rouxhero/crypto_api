"""Class routes for the server."""

class ServerRoutes(dict):
    """Top level class for server routes."""

    def __init__(self,url,function,methods):
        """
        Constructor for ServerRoutes

        Args:
            url (str): dest URL
            function (callable): Called function
            methods (str): accepted HTTP method
        """
        self["rule"] = url
        self["view_func"] = function
        self["methods"] = [methods]

class GetRoutes(ServerRoutes):
    """Class for GET routes."""

    def __init__(self,url,function):
        """
        Constructor for GetRoutes

        Args:
            url (str): dest URL
            function (callable): Called function
        """
        super().__init__(url,function,"GET")

class PostRoutes(ServerRoutes):
    """Class for POST routes."""

    def __init__(self,url,function):
        """
        Constructor for PostRoutes

        Args:
            url (str): dest URL
            function (callable): Called function
        """
        super().__init__(url,function,"POST")

class PutRoutes(ServerRoutes):
    """Class for PUT routes."""

    def __init__(self,url,function):
        """
        Constructor for PutRoutes

        Args:
            url (str): dest URL
            function (callable): Called function
        """
        super().__init__(url,function,"PUT")

class DeleteRoutes(ServerRoutes):
    """Class for DELETE routes."""

    def __init__(self,url,function):
        """
        Constructor for DeleteRoutes

        Args:
            url (str): dest URL
            function (callable): Called function
        """
        super().__init__(url,function,"DELETE")