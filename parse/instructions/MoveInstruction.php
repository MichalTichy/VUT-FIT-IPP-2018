<?php
class MoveInstruction implements IInstruction
{
    protected $arg1;
    protected $arg2;
    public function __construct($instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,2);
        $arg1=$parser->ExtractArgument($instructionTextRepresentation,1);
        $arg2=$parser->ExtractArgument($instructionTextRepresentation,2);

        $varValidator=new VariableValidator();
        $varValidator->Validate($arg1);

        $symbValidator=new SymbolValidator();
        $symbValidator->Validate($arg2);
    }

    public function ToXmlElement(){

    }
}