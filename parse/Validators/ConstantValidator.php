<?php

require_once("Validators\ValidatorBase.php");
class ConstantValidator extends ValidatorBase
{
    public function Is($input){
        $stringValidator=new StringValidator();
        $intValidator=new IntValidator();
        $boolValidator=new BoolValidator();

        return $stringValidator->Is($input) || $intValidator->Is($input) || $boolValidator->Is($input);
    }
}