<?php
class CodeParser implements ICodeParser
{
    public function Parse($input) {
        $instructions=array();
        
        foreach ($input as $line)
        {
            array_push($instructions,$this->CreateInstruction($line));
        }

        return new Program($instructions);
    }


    protected function ExtractInstructionCode($line){
        $arr = explode(' ',trim($line));
        return $arr[0];
    }

    protected function CreateInstruction($line){
        $instructionCode=$this->ExtractInstructionCode($line);
        switch ($instructionCode)
        {
            case "MOVE":
                throw new Exception("NOT IMPLEMENTED");
            case "CREATEFRAME":
                throw new Exception("NOT IMPLEMENTED");
            case "PUSHFRAME":
                throw new Exception("NOT IMPLEMENTED");
            case "POPFRAME":
                throw new Exception("NOT IMPLEMENTED");
            case "DEFVAR":
                throw new Exception("NOT IMPLEMENTED");
            case "CALL":
                throw new Exception("NOT IMPLEMENTED");
            case "RETURN":
                throw new Exception("NOT IMPLEMENTED");
            case "PUSHS":
                throw new Exception("NOT IMPLEMENTED");
            case "POPS":
                throw new Exception("NOT IMPLEMENTED");
            case "ADD":
                throw new Exception("NOT IMPLEMENTED");
            case "SUB":
                throw new Exception("NOT IMPLEMENTED");
            case "MUL":
                throw new Exception("NOT IMPLEMENTED");
            case "IDIV":
                throw new Exception("NOT IMPLEMENTED");
            case "LT":
                throw new Exception("NOT IMPLEMENTED");
            case "GT":
                throw new Exception("NOT IMPLEMENTED");
            case "EQ":
                throw new Exception("NOT IMPLEMENTED");
            case "AND":
                throw new Exception("NOT IMPLEMENTED");
            case "OR":
                throw new Exception("NOT IMPLEMENTED");
            case "NOT":
                throw new Exception("NOT IMPLEMENTED");
            case "INT2CHAR":
                throw new Exception("NOT IMPLEMENTED");
            case "STRI2INT":
                throw new Exception("NOT IMPLEMENTED");
            case "READ":
                throw new Exception("NOT IMPLEMENTED");
            case "WRITE":
                throw new Exception("NOT IMPLEMENTED");
            case "CONCAT":
                throw new Exception("NOT IMPLEMENTED");
            case "STRLEN":
                throw new Exception("NOT IMPLEMENTED");
            case "GETCHAR":
                throw new Exception("NOT IMPLEMENTED");
            case "SETCHAR":
                throw new Exception("NOT IMPLEMENTED");
            case "TYPE":
                throw new Exception("NOT IMPLEMENTED");
            case "LABEL":
                throw new Exception("NOT IMPLEMENTED");
            case "JUMP":
                throw new Exception("NOT IMPLEMENTED");
            case "JUMPIFEQ":
                throw new Exception("NOT IMPLEMENTED");
            case "JUMPIFNEQ":
                throw new Exception("NOT IMPLEMENTED");
            case "DPRINT":
                throw new Exception("NOT IMPLEMENTED");
            case "BREAK":
                throw new Exception("NOT IMPLEMENTED");
        	default:
                throw new LexicalException($instructionCode + " is an invalid instruction code.");
        }

    }
}