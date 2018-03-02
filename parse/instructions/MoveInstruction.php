<?php
require_once("instructions\IInstruction.php");
class MoveInstruction implements IInstruction
{
    protected $arg1;
    protected $arg2;
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,2);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $this->arg2=$parser->ExtractArgument($instructionTextRepresentation,2);

        $varValidator=new VariableValidator();
        $varValidator->Validate($this->arg1);

        $symbValidator=new SymbolValidator();
        $symbValidator->Validate($this->arg2);
    }

    public function ToXmlElement(){

    }
}