
#Tenis
class TenisException(Exception):
    def __init__(self):
        self.default = 'default'
class TenisNotFoundError(TenisException):
    def __init__(self):
        self.status_code = 404
        self.detail = "TENIS_NAO_ENCONTRADO"

class TenisAlreadyExistError(TenisException):
    def __init__(self):
        self.status_code = 409
        self.detail = "TENIS_DUPLICADO"

#Fornecedor
class FornecedorException(Exception):
    def __init__(self):
        self.default = 'default'
class FornecedorNotFoundError(FornecedorException):
    def __init__(self):
        self.status_code = 404
        self.detail = "FORNECEDOR_NAO_ENCONTRADO"

class FornecedorAlreadyExistError(FornecedorException):
    def __init__(self):
        self.status_code = 409
        self.detail = "FORNECEDOR_DUPLICADO"