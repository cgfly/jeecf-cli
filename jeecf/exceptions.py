class JeecfNotLoginException(Exception):
    def __str__(self):
        return "You need run 'jeecf login' first!"
