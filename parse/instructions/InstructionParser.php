<?php
require_once("SyntaxException.php");
class InstructionParser
{

    public function ExtractArgument($instruction,$argumentNumber ){
        $arr = explode(' ',trim($instruction));
        if ((count($arr)-1)<$argumentNumber)
        {
        	throw new SyntaxException("Instruction " . $arr[0] . " does not have argument number ". $argumentNumber);
        }

        return $arr[$argumentNumber];
    }

    public function CheckIfInstructionHaveAllParameters($instruction,$requiredCountOfParameters){
        $arr = explode(' ',trim($instruction));
        if ((count($arr)-1)!=$requiredCountOfParameters)
        {
        	throw new SyntaxException("Instruction " . $arr[0] . " does not have required number parameters.");
        }
    }

    public function ConvertArgumentToXmlNode($arg,$NodeName,$XmlDocument){
        $node=$XmlDocument->createElement($NodeName);

        $intValidator=new IntValidator();
        $boolValidator=new BoolValidator();
        $stringValidator=new StringValidator();
        $labelValidator=new LabelValidator();
        $typeValidator=new TypeValidator();
        $varValidator=new VariableValidator();

        if($intValidator->Is($arg))
        {
            $node->setAttribute("type","int");
            $node->nodeValue=explode('@',$arg)[1];
        }
        else if($stringValidator->Is($arg))
        {
            $node->setAttribute("type","string");
            $node->nodeValue=explode('@',$arg)[1];
        }
        else if($boolValidator->Is($arg))
        {
            $node->setAttribute("type","bool");
            $node->nodeValue=strtolower(explode('@',$arg)[1]);
        }
        else if($labelValidator->Is($arg))
        {
            $node->setAttribute("type","label");
            $node->nodeValue=$arg;
        }
        else if($typeValidator->Is($arg))
        {
            $node->setAttribute("type","type");
            $node->nodeValue=$arg;
        }
        else if($varValidator->Is($arg))
        {
            $node->setAttribute("type","var");

            $argParts=explode('@',$arg);
            $node->nodeValue=strtoupper($argParts[0])."@".$argParts[1];
        }
        else
        {
            throw new SyntaxException("Unable to parse instucion argument");
        }

        return $node;
    }
}