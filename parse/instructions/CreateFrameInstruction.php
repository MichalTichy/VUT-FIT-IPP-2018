<?php
require_once("./instructions/InstructionBase.php");
class CreateFrameInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,0);
    }
}