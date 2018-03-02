<?php

require_once("instructions\IInstruction.php");
class BreakInstruction implements IInstruction
{
    protected $arg1;
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,0);

    }

    public function ToXmlElement(){

    }
}
