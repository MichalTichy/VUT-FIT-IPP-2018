<?php

class Program implements IProgram
{
    protected $instructions;
    function __construct(array $instructions){
        $this->instructions=$instructions;
    }
    public function ConvertToXml(){
        
    }
}