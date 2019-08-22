from collections import defaultdict


class ApiError(Exception):
    def __init__(self, value="UnKnow Reason", op="", data=None):
        self.value = str(value)
        # 统一处理的时候加上data属性，方便统一返回
        self.data = data
        self.op = str(op)
        if op:
            self.value = "{cls}.{op}: {value}".format(cls=self.__class__.__name__, op=self.op, value=self.value)
        else:
            self.value = "{value}".format(value=self.value)
        super().__init__(self.value)


class NoAccessError(ApiError):
    def __init__(self, value="No Access Error", data=None, op=""):
        super().__init__(value=value, op=op, data=data)


class AuthFailureError(ApiError):
    def __init__(self, value="Auth Failure Error", data=None, op=""):
        super().__init__(value=value, op=op, data=data)


class NotExistError(ApiError):
    def __init__(self, value="Not Exist Error", data=None, op=""):
        super().__init__(value=value, op=op, data=data)


class InputError(ApiError):
    def __init__(self, value="Input Error", data=None, op=""):
        if isinstance(value, dict):
            value = "\n".join([str(k) + " " + ".".join(v) for k, v in value.items()])
        super().__init__(value=value, op=op, data=data)


class ReturnDataError(ApiError):
    def __init__(self, value="Return Data Error", data=None, op=""):
        super().__init__(value, op, data)


class NeedRecordError(ApiError):
    def __init__(self, value="Need Record Error", data=None, op=""):
        super().__init__(value, op, data)


class InternalError(ApiError):
    def __init__(self, value="Internal Error", data=None, op=""):
        super().__init__(value, op, data)


class NotFoundError(ApiError):
    def __init__(self, value="Not Found Error", data=None, op=""):
        super().__init__(value, op, data)


class DataBaseError(ApiError):
    def __init__(self, value="Data Base Error", data=None, op=""):
        super().__init__(value, op, data)


class GitLabAuthError(ApiError):
    def __init__(self, value="GitLab Auth Error", data=None, op=""):
        super().__init__(value, op, data)


class K8sError(ApiError):
    def __init__(self, value="UnKnow Reason", op="UnKnow operator", data=None):
        if isinstance(value, dict):
            value_default = defaultdict(lambda: "UnKnow Reason", value)
            self.value = value_default["message"]
            self._exist = value_default["reason"] == "AlreadyExists"
            self._noexist = value_default["reason"] == "NotFound"
        else:
            self.value = value
        self.data = data
        super().__init__(self.value, op)


class GitError(ApiError):
    def __init__(self, value="UnKnow Reason", op="UnKnow Operator", data=None):
        if isinstance(value, dict):
            value_default = defaultdict(lambda: "UnKnow Reason", value)
            value = '. '.join(["%s error: %s" % (k, ','.join(v)) for k, v in value_default.items() if v])
            self._exist = (value_default["name"][0] == "has already been taken" or value_default["path"][
                0] == 'has already been taken')
        elif isinstance(value, str):
            self._exist = value == "Branch Already Exists"
        super().__init__(value, op, data)


class DevopsBusyError(ApiError):
    def __init__(self, value="DevopsBusy", data=None, op=""):
        super().__init__(value, op, data)
