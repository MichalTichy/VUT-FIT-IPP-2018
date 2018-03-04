<?php
require_once("IProgram.php");
class Program implements IProgram
{
    protected $instructions;
    function __construct(array $instructions){
        $this->instructions=$instructions;
    }
    public function ConvertToXml(){
        $domTree=new DOMDocument('1.0', 'UTF-8');

        $root = $domTree->createElement("program");
        $root->setAttribute("language","IPPcode18");

        $counter=1;
        foreach($this->instructions as $instruction){
            $instructionNode=$instruction->ToXmlElement($domTree);
            $instructionNode->setAttribute("order",$counter++);
            $root->appendChild($instructionNode);
        }

        $domTree->appendChild($root);

        return $domTree;
    }
}