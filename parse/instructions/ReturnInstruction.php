<?php

require_once("instructions\IInstruction.php");
class ReturnInstruction implements IInstruction
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,0);
    }

    public function ToXmlElement(){

    }
}
