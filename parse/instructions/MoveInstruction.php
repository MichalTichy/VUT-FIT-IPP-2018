<?php
class MoveInstruction implements IInstruction
{
    public function __construct(array $instructionTextRepresentation){
        $parser=new InstructionParser();
        $parser->CheckIfInstructionHaveAllParameters($instructionTextRepresentation,2);
    }

    public function ToXmlElement(){
        
    }
}