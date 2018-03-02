<?php

require_once("instructions\IInstruction.php");
class LabelInstruction implements IInstruction
{
    protected $arg1;
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,1);
        $this->arg1=$parser->ExtractArgument($instructionTextRepresentation,1);

        $labelValidator=new LabelValidator();

        $labelValidator->Validate($this->arg1);

    }

    public function ToXmlElement(){

    }
}
