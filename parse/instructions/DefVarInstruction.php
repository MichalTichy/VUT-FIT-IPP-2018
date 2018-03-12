<?php
require_once("./instructions/InstructionBase.php");
class DefVarInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,1);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $varValidator=new VariableValidator();
        $varValidator->Validate($this->arg1);
    }
}
