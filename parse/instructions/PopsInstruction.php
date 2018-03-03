<?php
require_once("instructions\InstructionBase.php");
class PopsInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,1);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $variableValidator=new VariableValidator();
        $variableValidator->Validate($this->arg1);
    }
}
