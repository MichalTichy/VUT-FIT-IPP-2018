<?php
require_once("SyntaxException.php");
class InstructionParser
{   

    public function ExtractArgument($instruction,$argumentNumber ){
        $arr = explode(' ',trim($instruction));
        if ((count($arr)-1)<$argumentNumber)
        {
        	throw new SyntaxException("Instruction " + $arr[0] + " does not have argument number "+$argumentNumber);
        }

        return $arr[$argumentNumber];
    }

    public function CheckIfInstructionHaveAllParameters($instruction,$requiredCountOfParameters){
        $arr = explode(' ',trim($instruction));
        if ((count($arr)-1)!=$requiredCountOfParameters)
        {
        	throw new SyntaxException("Instruction " + $arr[0] + " does not have required number parameters.");
        }
    }
}