<?php

require_once("./Validators/ValidatorBase.php");
class StringValidator extends ValidatorBase
{

    public function Is($input){

        return preg_match
            (
                "/^string@([a-zA-Z\x{0021}\x{0022}\x{0024}-\x{005B}\x{005D}-\x{FFFF}|(\\\\[0-90-90-9])*$/u"
                ,$input
            );
    }
}