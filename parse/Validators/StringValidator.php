<?php

class StringValidator extends ValidatorBase
{

    public function Is($input){
        return preg_match
            (
                "^string@([a-zA-Z\u0021\u0022\u0024-\u005B\u005D-\uFFFF]|(\\0([0-2][0-9])|(\\03[0-2]))|(\\035)|(\\092))*$"
                ,$input
            );
    }
}