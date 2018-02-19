<?php

/**
 * IntValidator short summary.
 *
 * IntValidator description.
 *
 * @version 1.0
 * @author email
 */
class IntValidator extends ValidatorBase
{
    protected function Is($input){
        return preg_match("^int@(-)?[0-9]*$",$input);
    }
}