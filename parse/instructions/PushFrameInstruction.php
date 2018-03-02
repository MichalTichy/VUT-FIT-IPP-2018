<?php

require_once("instructions\IInstruction.php");
class PushFrameInstruction implements IInstruction
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,0);
    }

    public function ToXmlElement(){

    }
}