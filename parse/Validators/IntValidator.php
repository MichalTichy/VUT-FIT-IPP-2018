<?php

require_once("Validators\ValidatorBase.php");
class IntValidator extends ValidatorBase
{
    public function Is($input){
        return preg_match("/^int@(-|\+)?[0-9]*$/",$input);
    }
}