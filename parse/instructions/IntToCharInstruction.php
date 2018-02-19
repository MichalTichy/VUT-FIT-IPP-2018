<?php

class IntToCharInstruction implements IInstruction
{
    protected $arg1;
    protected $arg2;
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,2);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $this->arg2=$parser->ExtractArgument($instructionTextRepresentation,2);

        $variableValidator=new VariableValidator();
        $symbolValidator=new SymbolValidator();

        $variableValidator->Validate($this->arg1);
        $symbolValidator->Validate($this->arg2);

    }

    public function ToXmlElement(){

    }
}
