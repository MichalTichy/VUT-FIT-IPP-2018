<?php

require_once("Validators\ValidatorBase.php");
class SymbolValidator extends ValidatorBase
{
    public function Is($input){
        $varValidator=new VariableValidator();
        $constValidator=new ConstantValidator();

        return $varValidator->Is($input) || $constValidator->Is($input);
    }
}