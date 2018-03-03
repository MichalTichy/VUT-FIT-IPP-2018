<?php
require_once("instructions\InstructionBase.php");
class DPrintInstruction extends InstructionBase
{
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,1);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);

        $symbolValidator=new SymbolValidator();

        $symbolValidator->Validate($this->arg1);

    }
}
