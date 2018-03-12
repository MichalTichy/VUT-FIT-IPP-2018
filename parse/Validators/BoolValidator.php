<?php

require_once("./Validators/ValidatorBase.php");
class BoolValidator extends ValidatorBase
{
    public function Is($input){
        return preg_match("/^bool@((true)|(false))$/",$input);
    }
}