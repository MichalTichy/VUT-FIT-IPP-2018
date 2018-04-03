def main(args):
    pathToXml = GetPathToXml()
    instructions = Parse(pathToXml)

    instructionProcessor=InstructionProcessor(instructionsList);
    instructionProcessor.Execute();

class InstructionProcessor(object):
    def __init__(self, instructionsList):
        self.instructions = instructionsList
        return super().__init__()
    def __GetInstruction(self):        
        raise NotImplementedError
    def Execute(self):
        raise NotImplementedError

class SymbolTable(object):
    def __init__(self):
        self.parentSymbolTable = parentSymbolTable;
        self.symbols=dict()
        return super().__init__()
    def Insert(self,symbol):        
        if symbol.name in self.symbols.keys:
            raise SystemError
        self.symbols[symbol.name]=symbol;
    def Get(self,symbolName):
        if symbolName in self.symbols.keys:
            return self.symbols[symbolName]
        return SystemError

class DataType(Enum):
    INT = 1,
    BOOL = 2,
    STRING = 3

class Symbol(object):
    def __init__(self,name,type:DataType):
        self.name=name
        self.type=type
    def __eq__(self, other): 
        return self.name==other.name
def GetPathToXml():
    raise NotImplementedError;

import xml.etree.ElementTree as ElementTree
class XmlParser(object):
    def Parse(self,xmlPath):
        tree=ElementTree.parse(xmlPath)
        root=tree.getroot();
        self.__CheckRoot(root)
        for instruction in root:
            if instruction.tag == 'name' or instruction.tag == 'description':
                continue
            if instruction.tag == 'instruction':
                yield self.__CreateInstruction(instruction);
            raise SyntaxError
    def __CheckRoot(self,rootElement):
        if rootElement.tag!='program' or len(rootElement.attrib)!=1 or rootElement.attrib.get('language')!='IPPcode18':
            raise SyntaxError
    def __CreateInstruction(self,instructionElemment):
        raise NotImplementedError;

    