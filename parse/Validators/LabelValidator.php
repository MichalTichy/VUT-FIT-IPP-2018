<?php

require_once("Validators\ValidatorBase.php");
class LabelValidator extends ValidatorBase
{
    public function Is($input){

        $varNameValidator=new VarNameValidator();
        return $varNameValidator->Is($input);
    }
}