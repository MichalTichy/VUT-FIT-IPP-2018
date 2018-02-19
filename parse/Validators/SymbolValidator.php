<?php
class SymbolValidator
{
    public function Is($input){
        $varValidator=new StringValidator();
        $constValidator=new IntValidator();

        return $varValidator->Is($input) || $constValidator->Is($input);
    }
}