class TropiPy:
    def __init__(self, option):
        self.cfg = {
            url: '',
            token = 'Bearer';
            contentType = 'application/json';
        }

    def set(self, option):
        self.cfg = option

    def get(self, modname):
        module = __import__(modname)
        modcls = getattr(module, class_name)
        instance = modcls(self.cfg)
        return instance
