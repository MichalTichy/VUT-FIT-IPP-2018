<?php

require_once("Validators\ValidatorBase.php");
class SymbolValidator extends ValidatorBase
{
    public function Is($input){
        $varValidator=new VariableValidator();
        $constValidator=new ConstantValidator();

        return $constValidator->Is($input) || $varValidator->Is($input);
    }
}