import re


def GetPathToXml():
    raise NotImplementedError;


def main(args):
    parser = XmlParser();
    pathToXml = GetPathToXml()
    instructions = parser.Parse(pathToXml)

    instructionProcessor = InstructionProcessor(instructions);
    instructionProcessor.Execute();


class InstructionProcessor(object):
    def __init__(self, instructionsList):
        self.instructions = instructionsList
        super().__init__()

    def __GetInstruction(self):
        raise NotImplementedError

    def Execute(self):
        raise NotImplementedError


class SymbolTable(object):
    def __init__(self):
        self.symbols = dict()
        return super().__init__()

    def Insert(self, symbol):
        if symbol.name in self.symbols.keys:
            raise SystemError
        self.symbols[symbol.name] = symbol;

    def Get(self, symbolName):
        if symbolName in self.symbols.keys:
            return self.symbols[symbolName]
        return SystemError


from enum import Enum


class DataType(Enum):
    INT = 1,
    BOOL = 2,
    STRING = 3


class Symbol(object):
    def __init__(self, name, type: DataType):
        self.name = name
        self.type = type

    def __eq__(self, other):
        return self.name == other.name


import xml.etree.ElementTree as ElementTree


class XmlParser(object):
    def Parse(self, xmlPath):
        tree = ElementTree.parse(xmlPath)

        root = tree.getroot();
        self.__CheckRoot(root)
        for instruction in root:
            if instruction.tag == 'name' or instruction.tag == 'description':
                continue
            if instruction.tag == 'instruction':
                yield self.__CreateInstruction(instruction);
            raise SyntaxError

    def __CheckRoot(self, rootElement):
        if rootElement.tag != 'program' or len(rootElement.attrib) != 1 or rootElement.attrib.get(
                'language') != 'IPPcode18':
            raise SyntaxError

    def __CreateInstruction(self, instructionElemment):
        instrucitonCode = instructionElemment.get("opcode")
        if instrucitonCode == "MOVE":
            raise NotImplemented
        elif instrucitonCode == "CREATEFRAME":
            raise NotImplemented
        elif instrucitonCode == "PUSHFRAME":
            raise NotImplemented
        elif instrucitonCode == "POPFRAME":
            raise NotImplemented
        elif instrucitonCode == "DEFVAR":
            raise NotImplemented
        elif instrucitonCode == "CALL":
            raise NotImplemented
        elif instrucitonCode == "RETURN":
            raise NotImplemented
        elif instrucitonCode == "PUSHS":
            raise NotImplemented
        elif instrucitonCode == "POPS":
            raise NotImplemented
        elif instrucitonCode == "ADD":
            raise NotImplemented
        elif instrucitonCode == "SUB":
            raise NotImplemented
        elif instrucitonCode == "MUL":
            raise NotImplemented
        elif instrucitonCode == "IDIV":
            raise NotImplemented
        elif instrucitonCode == "LT":
            raise NotImplemented
        elif instrucitonCode == "GT":
            raise NotImplemented
        elif instrucitonCode == "EQ":
            raise NotImplemented
        elif instrucitonCode == "AND":
            raise NotImplemented
        elif instrucitonCode == "OR":
            raise NotImplemented
        elif instrucitonCode == "NOT":
            raise NotImplemented
        elif instrucitonCode == "INT2CHAR":
            raise NotImplemented
        elif instrucitonCode == "STRI2INT":
            raise NotImplemented
        elif instrucitonCode == "READ":
            raise NotImplemented
        elif instrucitonCode == "WRITE":
            raise NotImplemented
        elif instrucitonCode == "CONCAT":
            raise NotImplemented
        elif instrucitonCode == "STRLEN":
            raise NotImplemented
        elif instrucitonCode == "GETCHAR":
            raise NotImplemented
        elif instrucitonCode == "SETCHAR":
            raise NotImplemented
        elif instrucitonCode == "TYPE":
            raise NotImplemented
        elif instrucitonCode == "LABEL":
            raise NotImplemented
        elif instrucitonCode == "JUMP":
            raise NotImplemented
        elif instrucitonCode == "JUMPIFEQ":
            raise NotImplemented
        elif instrucitonCode == "JUMPIFNEQ":
            raise NotImplemented
        elif instrucitonCode == "DPRINT":
            raise NotImplemented
        elif instrucitonCode == "BREAK":
            raise NotImplemented
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
        return re.match(r"^([a-zA-Z]|-|[_$&%*])([a-zA-Z]|-|[_$&%*]|[0-9]+)*$", inputData) is not None


class IntArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return re.match(r"^[\x2B\x2D]?[0-9]*$", inputData) is not None


class StringArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return re.match(r"^((true)|(false))$", inputData) is not None


class BoolArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return re.match(r"^([a-zA-Z\u0021\u0022\u0024-\u005B\u005D-\uFFFF|(\\\\[0-90-90-9])*$", inputData) is not None


class LabelArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return VarNameValidator().Is(inputData)


class TypeArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        return inputData == "int" | inputData == "string" | inputData == "bool"


class VarArgumentValidator(ValidatorBase):
    def Is(self, inputData: str):
        inputParts = inputData.split("@")
        if inputParts.count() < 2:
            return False

        if inputParts[1].find("@") != -1:
            identifier = input[:inputData.find("@") + 1]
        else:
            identifier = inputParts[1]

        return (inputParts[0] == "LF" | inputParts[0] == "TF" | inputParts[0] == "GF") & VarNameValidator().Is(
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

    def Execute(self):
        raise NotImplementedError("This method is abstract")

    def _GetAttributeType(self, element):
        if element.tag != "arg1" | element.tag != "arg2" | element.tag != "arg3":
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

    def _GetAttributeValue(self, element, expectedType):
        type = self._GetAttributeType(element)
        if expectedType == AttributeType.SYMBOL:
            if type != AttributeType.INT & type != AttributeType.BOOL & type != AttributeType.STRING & type != AttributeType.VAR:
                raise SyntaxError
        elif expectedType != type:
            raise SyntaxError

        innerText = element.itertext()

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
            VarNameValidator().Validate(innerText)
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
        if attrs.count() != expectedCount:
            raise SyntaxError
        return attrs


class MoveInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.symbol = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class CreateFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class PushFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class PopFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class DefVarInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class DefVarInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class CallInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.label = self._GetAttributeValue(attributes[0], AttributeType.LABEL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class ReturnInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class PushsInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.sym = self._GetAttributeValue(attributes[0], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class PopsInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class AddInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class SubInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class MulInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class IDivInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class LTInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class GTInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class EQInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class AndInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class OrInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class NotInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class IntToCharInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 2)
        self.var = self._GetAttributeValue(attributes[0], AttributeType.VAR)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class LabelInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.label = self._GetAttributeValue(attributes[0], AttributeType.LABEL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class JumpInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.label = self._GetAttributeValue(attributes[0], AttributeType.LABEL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class JumpIfEqInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.label = self._GetAttributeValue(attributes[0], AttributeType.LABEL)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class JumpIfNotEqInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 3)
        self.label = self._GetAttributeValue(attributes[0], AttributeType.LABEL)
        self.sym1 = self._GetAttributeValue(attributes[1], AttributeType.SYMBOL)
        self.sym2 = self._GetAttributeValue(attributes[2], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class DprintInstruction(Instruction):
    def __init__(self, xmlElement):
        attributes = self._GetAttributes(xmlElement, 1)
        self.sym = self._GetAttributeValue(attributes[0], AttributeType.SYMBOL)

    def Execute(self):
        raise NotImplementedError("This method is abstract")

class BreakFrameInstruction(Instruction):
    def __init__(self, xmlElement):
        self._GetAttributes(xmlElement, 0)

    def Execute(self):
        raise NotImplementedError("This method is abstract")