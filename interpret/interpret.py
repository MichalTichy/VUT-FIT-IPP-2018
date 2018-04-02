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
        raise NotImplementedError;
    def Execute(self):
        raise NotImplementedError;

class SymbolTable(object):
    def __init__(self,parentSymbolTable):
        self.parentSymbolTable = parentSymbolTable;
        return super().__init__()
    def Insert(self,symbol):
        self._InsertIntoSpecificTable(symbol,self);
    def _InsertIntoSpecificTable(self,symbol,targetSymbolTable:SymbolTable):
        raise NotImplementedError;
    def Get(self,symbolName):
        raise NotImplementedError;
    def PushFrame(self):
        self=SymbolTable(self);
    def PopFrame(self):
        self=self.parentSymbolTable;

class DataType(Enum):
    INT = 1,
    BOOL = 2,
    STRING = 3

class Symbol(object):
    def __init__(self,name,type:DataType):
        self.name=name
        self.type=type

def GetPathToXml():
    raise NotImplementedError;

import xml.etree.ElementTree as ElementTree
class XmlParser(object):
    def Parse(self,xmlPath):
        tree=ElementTree.parse(xmlPath)
        root=tree.getroot();
        self.__CheckRoot(root)
        for instruction in root:
            yield self.__CreateInstruction(instruction);
    def __CheckRoot(self,rootElement):
        raise NotImplementedError;
    def __CreateInstruction(self,instructionElemment):
        raise NotImplementedError;

    