class MsgConst(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        # 判断是否已经被赋值，如果是则报错
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        # 判断所赋值是否是全部大写，用来做第一次赋值的格式判断，也可以根据需要改成其他判断条件
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value


msg_const = MsgConst()
msg_const.APPLICATION_404 = "项目找不到了"
msg_const.APPLICATION_403 = "项目禁止访问"

