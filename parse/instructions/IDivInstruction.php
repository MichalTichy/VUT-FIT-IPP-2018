<?php
require_once("./instructions/InstructionBase.php");
class IDivInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,3);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $this->arg2=$parser->ExtractArgument($instructionTextRepresentation,2);
        $this->arg3=$parser->ExtractArgument($instructionTextRepresentation,3);

        $variableValidator=new VariableValidator();
        $symbolValidator=new SymbolValidator();

        $variableValidator->Validate($this->arg1);
        $symbolValidator->Validate($this->arg2);
        $symbolValidator->Validate($this->arg3);

    }
}
