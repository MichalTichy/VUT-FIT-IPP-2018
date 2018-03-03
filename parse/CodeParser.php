<?php

require_once("ICodeParser.php");
require_once("LexicalException.php");
class CodeParser implements ICodeParser
{
    public function __construct(){

        foreach (glob("instructions/*.php") as $filename)
        {
            require_once($filename);
        }
    }

    public function Parse($input) {
        $instructions=array();

        foreach ($input as $instruction)
        {            
            array_push($instructions,$this->CreateInstruction($instruction));
        }

        return new Program($instructions);
    }


    protected function ExtractInstructionCode($line){
        $arr = explode(' ',trim($line));
        return strtoupper($arr[0]);
    }

    protected function CreateInstruction($line){
        $instructionCode=$this->ExtractInstructionCode($line);
        switch ($instructionCode)
        {
            case "MOVE":
                return new MoveInstruction($line);
            case "CREATEFRAME":
                return new CreateFrameInstruction($line);
            case "PUSHFRAME":
                return new PushFrameInstruction($line);
            case "POPFRAME":
                return new PopFrameInstruction($line);
            case "DEFVAR":
                return new DefVarInstruction($line);
            case "CALL":
                return new CallInstruction($line);
            case "RETURN":
                return new ReturnInstruction($line);
            case "PUSHS":
                return new PushsInstruction($line);
            case "POPS":
                return new PopsInstruction($line);
            case "ADD":
                return new AddInstruction($line);
            case "SUB":
                return new SubInstruction($line);
            case "MUL":
                return new MulInstruction($line);
            case "IDIV":
                return new IDivInstruction($line);
            case "LT":
                return new LTInstruction($line);
            case "GT":
                return new GTInstruction($line);
            case "EQ":
                return new EQInstruction($line);
            case "OR":
                return new OrInstruction($line);
            case "NOT":
                return new NotInstruction($line);
            case "INT2CHAR":
                return new IntToCharInstruction($line);
            case "STRI2INT":
                return new StringToIntInstruction($line);
            case "READ":
                return new ReadInstruction($line);
            case "WRITE":
                return new WriteInstruction($line);
            case "CONCAT":
                return new ConcatInstruction($line);
            case "STRLEN":
                return new StrLenInstruction($line);
            case "GETCHAR":
                return new GetCharInstruction($line);
            case "SETCHAR":
                return new SetCharInstruction($line);
            case "TYPE":
                return new TypeInstruction($line);
            case "LABEL":
                return new LabelInstruction($line);
            case "JUMP":
                return new JumpInstruction($line);
            case "JUMPIFEQ":
                return new JumpIfEqInstruction($line);
            case "JUMPIFNEQ":
                return new JumpIfNEqInstruction($line);
            case "DPRINT":
                return new DPrintInstruction($line);
            case "BREAK":
                return new BreakInstruction($line);
        	default:
                throw new LexicalException($instructionCode + " is an invalid instruction code.");
        }

    }
}