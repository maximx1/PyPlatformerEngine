class ClassLoaderUtils:
    
    """
        Utility to get a class by name and module.
    """
    def importClass(self, moduleName, className):
        mod = __import__(str(moduleName), fromlist=[str(className)])
        return getattr(mod, str(className))