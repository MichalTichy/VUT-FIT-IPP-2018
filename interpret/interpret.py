import re
import xml.etree.ElementTree as ElementTree

def GetPathToXml():
    return r"C:\Users\email\Desktop\input.xml"

class InstuctionPoiner(object):
    def __init__(self):
        self.IP=0;
        self.labels=dict()
        self.callStack=list()
    def RegisterLabel(self,Label:str):
        if Label in self.labels:
            raise SystemError
        self.labels[Label]=self.IP
    def GoToLabel(self,Label:str):
        if Label not in self.labels:
            raise SystemError
        self.callStack.append(self.IP)
        self.IP=self.labels[Label]
    def Return(self):
        self.IP=self.callStack.pop()

class InstructionProcessor(object):
    def __init__(self, instructionsList):
        self.instructions = instructionsList
        self.symTable=SymbolTable()
        self.InstuctionPoiner=InstuctionPoiner()
        self.stack=list()
        super().__init__()

    def __GetInstruction(self):
        return self.instructions[self.InstuctionPoiner.IP]

    def Execute(self):
        currentInstruction=self.__GetInstruction()
        while currentInstruction is not None:
            currentInstruction.Execute()
            currentInstruction=self.__GetInstruction()


class SymbolTable(object):
    def __init__(self):
        self.GlobalSymbols = dict()
        self.TemporarySymbols=None
        self.LocalSymbols=list()
        return super().__init__()

    def getRequestedSymbolTable(self,symbol:str):
        symbolSourceName = symbol.split("@")[0]
        if symbolSourceName=="TF":
            return self.TemporarySymbols
        elif symbolSourceName=="GF":
            return self.GlobalSymbols
        elif symbolSourceName=="LF":
            return self.LocalSymbols[-1]
        else:
            raise SyntaxError

    def Insert(self, symbolName:str):
        symbolTable=self.getRequestedSymbolTable(symbolName)
        symbol=Symbol(symbolName)
        if symbolTable==None:
            raise SystemError
        if symbol.name in symbolTable.keys:
            raise SystemError
        symbolTable[symbol.name] = symbol;

    def Get(self, symbolName,expectedType=None):        
        symbolTable=self.getRequestedSymbolTable(symbolName)
        
        symbolName = symbolName[name.index('@'):]
        if symbolTable==None:
            raise SystemError

        if symbolName in symbolTable.keys:
            symbol = symbolTable[symbolName]
            if expectedType!=None and symbol.type!=expectedType:
                raise SystemError
        return SystemError
    def CreateFrame(self):
        self.TemporarySymbols=dict()
    def PushFrame(self):
        if self.TemporarySymbols==None:
            raise SystemError
        self.LocalSymbols.append(self.TemporarySymbols)
        self.TemporarySymbols=None
    def PopFrame(self):
        if len(self.LocalSymbols)==0:
            raise SystemError
        self.TemporarySymbols=LocalSymbols.pop()


from enum import Enum


class DataType(Enum):
    INT = 1,
    BOOL = 2,
    STRING = 3


class Symbol(object):
    def __init__(self, name: str):
        self.name = name[name.index('@'):]
        self.type = None
        self.value = None
    def __eq__(self, other):
        return self.name == other.name

    def SetValue(self,value):
        if isinstance(value,Symbol):
            type=value.type
            self.value=value.value
        elif IntArgumentValidator().Is(value):
            type=DataType.INT
            self.value=int(value)
        elif BoolArgumentValidator.Is(value):            
            self.type=DataType.BOOL
            self.value= value != "false"
        elif StringArgumentValidator().Is(value):            
            self.type=DataType.STRING
            self.value=value
        elif isinstance(value,int):
            type=DataType.INT
            self.value=value
        elif isinstance(value,bool):            
            self.type=DataType.BOOL
            self.value=value
        elif isinstance(value,str):            
            self.type=DataType.STRING
            self.value=value
        else:
            raise SystemError


    def ExtractValue(value,symTable:SymbolTable,RequiredType:DataType):
        if VarArgumentValidator(value):
            sym=symTable.Get(value,RequiredType)
            if sym.type == None:
                return None
            return sym.value
        if isinstance(value,int):
            if RequiredType!=None and RequiredType != DataType.INT:
                raise SystemError
            return value
        if isinstance(value,str):
            if RequiredType!=None and RequiredType != DataType.STRING:
                raise SystemError
            return value
        if isinstance(value,bool):
            if RequiredType!=None and RequiredType != DataType.BOOL:
                raise SystemError
            return value
        raise SystemError

class XmlParser(object):
    def Parse(self, xmlPath):
        tree = ElementTree.parse(xmlPath)

        root = tree.getroot();
        self.__CheckRoot(root)
        instructions=list()
        for instruction in root:
            if instruction.tag == 'name' or instruction.tag == 'description':
                continue
            if instruction.tag == 'instruction':
                if int(instruction.get("order"))!=len(instructions)+1:
                    raise SyntaxError
                instructions.append(self.__CreateInstruction(instruction))
            else:
                raise SyntaxError
        return instructions

    def __CheckRoot(self, rootElement):
        if rootElement.tag != 'program' or len(rootElement.attrib) != 1 or rootElement.attrib.get(
                'language') != 'IPPcode18':
            raise SyntaxError

    def __CreateInstruction(self, instructionElemment):
        instrucitonCode = instructionElemment.get("opcode")
        if instrucitonCode == "MOVE":
            return MoveInstruction(instructionElemment)
        elif instrucitonCode == "CREATEFRAME":
            return CreateFrameInstruction(instructionElemment)
        elif instrucitonCode == "PUSHFRAME":
            return PushFrameInstruction(instructionElemment)
        elif instrucitonCode == "POPFRAME":
            return PopFrameInstruction(instructionElemment)
        elif instrucitonCode == "DEFVAR":
            return DefVarInstruction(instructionElemment)
        elif instrucitonCode == "CALL":
            return CallInstruction(instructionElemment)
        elif instrucitonCode == "RETURN":
            return ReturnInstruction(instructionElemment)
        elif instrucitonCode == "PUSHS":
            return PushsInstruction(instructionElemment)
        elif instrucitonCode == "POPS":
            return PopsInstruction(instructionElemment)
        elif instrucitonCode == "ADD":
            return AddInstruction(instructionElemment)
        elif instrucitonCode == "SUB":
            return SubInstruction(instructionElemment)
        elif instrucitonCode == "MUL":
            return MulInstruction(instructionElemment)
        elif instrucitonCode == "IDIV":
            return IDivInstruction(instructionElemment)
        elif instrucitonCode == "LT":
            return LTInstruction(instructionElemment)
        elif instrucitonCode == "GT":
            return GTInstruction(instructionElemment)
        elif instrucitonCode == "EQ":
            return EQInstruction(instructionElemment)
        elif instrucitonCode == "AND":
            return AndInstruction(instructionElemment)
        elif instrucitonCode == "OR":
            return OrInstruction(instructionElemment)
        elif instrucitonCode == "NOT":
            return NotInstruction(instructionElemment)
        elif instrucitonCode == "INT2CHAR":
            return IntToCharInstruction(instructionElemment)
        elif instrucitonCode == "STRI2INT":
            return StringToIntInstruction(instructionElemment)
        elif instrucitonCode == "READ":
            return ReadInstruction(instructionElemment)
        elif instrucitonCode == "WRITE":
            return WriteInstruction(instructionElemment)
        elif instrucitonCode == "CONCAT":
            return ConcatInstruction(instructionElemment)
        elif instrucitonCode == "STRLEN":
            return StrLenInstruction(instructionElemment)
        elif instrucitonCode == "GETCHAR":
            return GetCharInstruction(instructionElemment)
        elif instrucitonCode == "SETCHAR":
            return SetCharInstruction(instructionElemment)
        elif instrucitonCode == "TYPE":
            return TypeInstruction(instructionElemment)
        elif instrucitonCode == "LABEL":
            return LabelInstruction(instructionElemment)
        elif instrucitonCode == "JUMP":
            return JumpInstruction(instructionElemment)
        elif instrucitonCode == "JUMPIFEQ":
            return JumpIfEqInstruction(instructionElemment)
        elif instrucitonCode == "JUMPIFNEQ":
            return JumpIfNotEqInstruction(instructionElemment)
        elif instrucitonCode == "DPRINT":
            return MoveInstruction(instructionElemment)
        elif instrucitonCode == "BREAK":
            return DPrintInstruction(instructionElemment)
        else:
            raise SyntaxError


class ValidatorBase(object):
    def Validate(self, inputData: str):
        if not self.Is(inputData):
            raise SyntaxError

    def Is(self, inputData: str):
        raise NotImplemented


class VarNameValidator(ValidatorBase):
    def Is(self, inputData: str):
        return re.match(r"^([a-zA-Z]|-|[_$&%*])([a-zA-Z]|-|[_$&%*]|[0-9]+)*$$", inputData) is not None


class IntArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return re.match(r"^[\x2B\x2D]?[0-9]*$", inputData) is not None


class StringArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return re.match(r"^([a-zA-Z\u0021\u0022\u0024-\u005B\u005D-\uFFFF|(\\\\[0-90-90-9])*$", inputData) is not None


class BoolArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return inputData=="true" or inputData=="false"


class LabelArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return VarNameValidator().Is(inputData)


class TypeArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return inputData == "int" or inputData == "string" or inputData == "bool"


class VarArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        inputParts = inputData.split("@")
        if len(inputParts) < 2:
            return False

        if inputParts[1].find("@") != -1:
            identifier = input[:inputData.find("@") + 1]
        else:
            identifier = inputParts[1]

        return (inputParts[0] == "LF" or inputParts[0] == "TF" or inputParts[0] == "GF") and VarNameValidator().Is(
            identifier)


class AttributeType(Enum):
    INT = 0,
    BOOL = 1,
    STRING = 2,
    LABEL = 3,
    TYPE = 4,
    VAR = 5
    SYMBOL = 6


class Instruction(object):
    def __init__(self, xmlElement):
        pass

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        raise NotImplementedError("This method is abstract")

    def _GetAttributeType(self, element):
        if element.tag != "arg1" and element.tag != "arg2" and element.tag != "arg3":
            raise SyntaxError
        typeAttr = element.get("type")
        if typeAttr == "int":
            return AttributeType.INT
        elif typeAttr == "bool":
            return AttributeType.BOOL
        elif typeAttr == "string":
            return AttributeType.STRING
        elif typeAttr == "label":
            return AttributeType.LABEL
        elif typeAttr == "type":
            return AttributeType.TYPE
        elif typeAttr == "var":
            return AttributeType.VAR
        else:
            raise SyntaxError

    def GetAttributeValue(self, element, expectedType):
        type = self._GetAttributeType(element)
        if expectedType == AttributeType.SYMBOL:
            if type != AttributeType.INT and type != AttributeType.BOOL and type != AttributeType.STRING and type != AttributeType.VAR:
                raise SyntaxError
        elif expectedType != type:
            raise SyntaxError

        innerText = element.text
        if innerText==None:
            innerText=""

        if type == AttributeType.INT:
            IntArgumentValidator().Validate(innerText)
            return int(innerText)
        elif type == AttributeType.BOOL:
            BoolArgumentValidator().Validate(innerText)
            return bool(innerText)
        elif type == AttributeType.STRING:
            StringArgumentValidator().Validate(innerText)
            return innerText
        elif type == AttributeType.VAR:
            VarArgumentValidator().Validate(innerText)
            return innerText
        elif type == AttributeType.TYPE:
            TypeArgumentValidator().Validate(innerText)
            return innerText
        elif type == AttributeType.LABEL:
            LabelArgumentValidator().Validate(innerText)
            return innerText
        else:
            SyntaxError

    def _GetAttributes(self, element, expectedCount):
        attrs = list(element);
        if len(attrs) != expectedCount:
            raise SyntaxError
        return attrs


class MoveInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.symbol = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        if VarArgumentValidator().Is(self.symbol):
            value=SymbolTable.Get(self.symbol)
        else:
            value=self.symbol
        target=SymbolTable.Get(self.var)
        target.SetValue(value)

class CreateFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        SymTable.CreateFrame()

class PushFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        SymTable.PushFrame()

class PopFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        SymbolTable.PopFrame()

class DefVarInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        SymTable.Insert(self.var)
        
class CallInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.label = self.GetAttributeValue(attributes[0], AttributeType.LABEL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        IP.GoToLabel(self.label)

class ReturnInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        IP.Return()

class PushsInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.sym = self.GetAttributeValue(attributes[0], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        
        op1=Symbol.ExtractValue(self.sym,SymTable,None)
        Stack.append(op1)

class PopsInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        SymTable.Get(self.var).SetValue(Stack.pop())

class AddInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.INT)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.INT)
        SymTable.Get(self.var).SetValue(op1+op2)

class SubInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.INT)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.INT)
        SymTable.Get(self.var).SetValue(op1-op2)

class MulInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.INT)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.INT)
        SymTable.Get(self.var).SetValue(op1*op2)

class IDivInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.INT)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.INT)
        SymTable.Get(self.var).SetValue(op1/op2)

class LTInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,None)
        op2=Symbol.ExtractValue(self.sym1,SymTable,None)

        if type(op1) is not type(op2):
            raise SystemError

        SymTable.Get(self.var).SetValue(op1<op2)        

class GTInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,None)
        op2=Symbol.ExtractValue(self.sym1,SymTable,None)

        if type(op1) is not type(op2):
            raise SystemError

        SymTable.Get(self.var).SetValue(op1>op2)

class EQInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,None)
        op2=Symbol.ExtractValue(self.sym1,SymTable,None)

        if type(op1) is not type(op2):
            raise SystemError

        SymTable.Get(self.var).SetValue(op1==op2)        

class AndInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.BOOL)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.BOOL)
        SymTable.Get(self.var).SetValue(op1 and op2)

class OrInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.BOOL)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.BOOL)
        SymTable.Get(self.var).SetValue(op1 or op2)

class NotInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.BOOL)
        SymTable.Get(self.var).SetValue( not op1)

class IntToCharInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.INT)
        
        try:
            char=chr(op1)
        except ValueError:
            raise SystemError

        SymTable.Get(self.var).SetValue(char)



class StringToIntInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.STRING)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.INT)

        if (len(op1)-1)<op2 or (len(op1)-1)>op2:
            raise SystemError

        SymTable.Get(self.var).SetValue(ord(op1[op2]))

class ReadInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.type = self.GetAttributeValue(attributes[1], AttributeType.TYPE)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):        
        inData = input()
        sym=SymTable.Get(self.var)
        if type=="bool":
            data = inData == "true"
        elif type=="int":
            if IntArgumentValidator().Is(inData):
                data = int(inData);
            else:
                data = ""
        elif type=="string":
            if StringArgumentValidator().Is(inData):
                data=inData
            else:
                data=""
        sym.SetValue(data)


class WriteInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.sym = self.GetAttributeValue(attributes[0], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        val = Symbol.ExtractValue(self.sym)
        if isinstance(val,bool):
            if val:
                val="true"
            else:
                val="false"
        print(val)


class ConcatInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.STRING)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.STRING)
        SymTable.Get(self.var).SetValue(op1+op2)


class StrLenInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.STRING)
        SymTable.Get(self.var).SetValue(len(op1))


class GetCharInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.STRING)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.INT)

        if (len(op1)-1)<op2 or (len(op1)-1)>op2:
            raise SystemError

        SymTable.Get(self.var).SetValue(op1[op2])

class TypeInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        val = Symbol.ExtractValue(self.sym1)
        if val==None:
            SymTable.Get(self.var).SetValue("")
        elif type(val)==int:            
            SymTable.Get(self.var).SetValue("int")
        elif type(val)==str:            
            SymTable.Get(self.var).SetValue("string")
        elif type(val)==bool:            
            SymTable.Get(self.var).SetValue("bool")
        else:
            raise SystemError

class SetCharInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self.GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,DataType.INT)
        op2=Symbol.ExtractValue(self.sym2,SymTable,DataType.STRING)
        varString=Symbol.ExtractValue(self.var,SymbolTable,DataType.STRING)
        if (len(varString)-1)<op1 or (len(varString)-1)>op1:
            raise SystemError

        varString[op1]=op2[0]
        SymTable.Get(self.var).SetValue(varString)

class LabelInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.label = self.GetAttributeValue(attributes[0], AttributeType.LABEL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        IP.RegisterLabel(self.label)

class JumpInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.label = self.GetAttributeValue(attributes[0], AttributeType.LABEL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        IP.GoToLabel(self.label)

class JumpIfEqInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.label = self.GetAttributeValue(attributes[0], AttributeType.LABEL)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,None)
        op2=Symbol.ExtractValue(self.sym2,SymTable,None)
        if op1==op2:
            IP.GoToLabel(self.label)

class JumpIfNotEqInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.label = self.GetAttributeValue(attributes[0], AttributeType.LABEL)
        self.sym1 = self.GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self.GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        op1=Symbol.ExtractValue(self.sym1,SymTable,None)
        op2=Symbol.ExtractValue(self.sym2,SymTable,None)
        if op1!=op2:
            IP.GoToLabel(self.label)

class DPrintInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.sym = self.GetAttributeValue(attributes[0], AttributeType.SYMBOL)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        sys.stderr.write(Symbol.ExtractValue(self.sym))
        sys.stderr.write("\n")
        
class BreakFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self,IP:InstuctionPoiner,SymTable:SymbolTable,Stack:list):
        sys.stderr.write("IP = " + IP)
        sys.stderr.write("\n")



    
parser = XmlParser()
pathToXml = GetPathToXml()
instructions = parser.Parse(pathToXml)

instructionProcessor = InstructionProcessor(instructions)
instructionProcessor.Execute()