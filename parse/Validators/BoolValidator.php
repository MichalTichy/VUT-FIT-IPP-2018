<?php

class BoolValidator extends ValidatorBase
{
    protected function Is($input){
        return preg_match("^bool@((true)|(false))$",$input);
    }
}