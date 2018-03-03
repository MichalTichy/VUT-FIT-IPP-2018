<?php

require_once("instructions\IInstruction.php");

abstract class InstructionBase implements IInstruction
{
    protected $arg1;
    protected $arg2;
    protected $arg3;
    public  function ToXmlElement(){

    }
}