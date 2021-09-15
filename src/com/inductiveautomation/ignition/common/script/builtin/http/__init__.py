__all__ = ["JythonHttpClient"]

from java.lang import Object


class JythonHttpClient(Object):
    """A Jython-optimized wrapper around the base HttpClient available
    in Java 11+.

    Mostly, through convenience functions that make things easier to use
    from Jython.
    """

    def delete(self, *args, **kwargs):
        pass

    def deleteAsync(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def getAsync(self, *args, **kwargs):
        pass

    def getConnectTimeout(self):
        pass

    def getCookieManager(self):
        pass

    def getJavaClient(self):
        pass

    def getRedirectPolicy(self):
        pass

    def head(self, *args, **kwargs):
        pass

    def headAsync(self, *args, **kwargs):
        pass

    def options(self, *args, **kwargs):
        pass

    def parseChart(self, contentType):
        pass

    def patch(self, *args, **kwargs):
        pass

    def patchAsync(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def postAsync(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def putAsync(self, *args, **kwargs):
        pass

    def request(self, *args, **kwargs):
        pass

    def requestAsync(self, *args, **kwargs):
        pass

    def setGson(self, gson):
        pass

    def trace(self, *args, **kwargs):
        pass

    def traceAsync(self, *args, **kwargs):
        pass
