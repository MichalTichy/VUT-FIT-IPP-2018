<?php

require_once("instructions\IInstruction.php");
class WriteInstruction implements IInstruction
{
    protected $arg1;
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,1);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);

        $symbolValidator=new SymbolValidator();

        $symbolValidator->Validate($this->arg1);
    }

    public function ToXmlElement(){

    }
}
