<?php



class TypeValidator
{
    public function Is($input){

        return $input=="int" || $input=="string" ||$input=="bool";
    }
}