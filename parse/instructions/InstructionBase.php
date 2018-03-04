<?php

require_once("instructions\IInstruction.php");

abstract class InstructionBase implements IInstruction
{
    protected $arg1;
    protected $arg2;
    protected $arg3;

    public  function ToXmlElement($XmlDocument){
        $parser=new InstructionParser();

        $instructionNode=$XmlDocument->createElement("instruction");
        $instructionNode->setAttribute("opcode",strtoupper($this->GetInstrucionName()));

        if($this->arg1!=null){
            $instructionNode->appendChild($parser->ConvertArgumentToXmlNode($this->arg1,"arg1",$XmlDocument));
        }
        if($this->arg2!=null){
            $instructionNode->appendChild($parser->ConvertArgumentToXmlNode($this->arg2,"arg2",$XmlDocument));
        }
        if($this->arg3!=null){
            $instructionNode->appendChild($parser->ConvertArgumentToXmlNode($this->arg3,"arg3",$XmlDocument));
        }

        return $instructionNode;
    }

    private function GetInstrucionName(){
        $input=get_class($this);
        if(strpos($input, "Instruction")===false){
            throw new Exception("Unable to extract instruction name from " . $input);
        }
        return substr($input, 0, strpos($input, "Instruction"));
    }
}