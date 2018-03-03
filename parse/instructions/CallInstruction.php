<?php
require_once("instructions\InstructionBase.php");
class CallInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,1);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $labelValidator=new LabelValidator();
        $labelValidator->Validate($this->arg1);
    }
}
