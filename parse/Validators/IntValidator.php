<?php

require_once("./Validators/ValidatorBase.php");
class IntValidator extends ValidatorBase
{
    public function Is($input){
        return preg_match("/^int@[\x2B\x2D]?[0-9]*$/",$input);
    }
}