class Phone():
    pass
class NFCReader():
    pass
class RemoteControl():
    pass
class Myphone(Phone,NFCReader,RemoteControl)   : #左优先 谁在左边，谁的优先级更高，优先调用该属性
    pass