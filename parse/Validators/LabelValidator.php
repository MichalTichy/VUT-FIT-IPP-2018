<?php

class LabelValidator extends ValidatorBase
{
    public function Is($input){

        $varNameValidator=new VarNameValidator();
        return $varNameValidator->Is($input);
    }
}