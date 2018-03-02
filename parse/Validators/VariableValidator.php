<?php
require_once("Validators\ValidatorBase.php");
class VariableValidator extends ValidatorBase
{
    public function Is($input){
        $varNameValidator=new VarNameValidator();
        $arr = explode('@',$input);
        if (count($arr)!=2)
        {
            return false;
        }

        return ($arr[0]=="LF" || $arr[0]=="TF" || $arr[0]=="GF") && $varNameValidator->Is($arr[1]);

    }
}