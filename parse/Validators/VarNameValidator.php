<?php
class VarNameValidator extends ValidatorBase
{
    public function Is($input){
        return preg_match
            (
                "^([a-zA-Z]|-|[_$&%*])([a-zA-Z]|-|[_$&%*]|[0-9]+)*$"
                ,$input
            );
    }
}