<?php
require_once("./instructions/InstructionBase.php");
class ReadInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,2);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $this->arg2=$parser->ExtractArgument($instructionTextRepresentation,2);

        $variableValidator=new VariableValidator();
        $typeValidator=new TypeValidator();

        $variableValidator->Validate($this->arg1);
        $typeValidator->Validate($this->arg2);

    }
}
