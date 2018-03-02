<?php
require_once("Validators\ValidatorBase.php");
class TypeValidator extends ValidatorBase
{
    public function Is($input){

        return $input=="int" || $input=="string" ||$input=="bool";
    }
}