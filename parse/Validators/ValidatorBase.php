<?php
abstract class ValidatorBase implements IValidator
{

    public function Validate($input){
        if (!$this->Is($input))
        {
        	throw new SyntaxException("Argument validation failed.");
        }
    }

    protected abstract function Is($input);
}