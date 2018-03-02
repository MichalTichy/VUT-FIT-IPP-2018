<?php

require_once("Validators\ValidatorBase.php");
class MoveInstructionValidator extends ValidatorBase
{
    public function Is($input){
        return preg_match("/^bool@((true)|(false))$/",$input);
    }
}