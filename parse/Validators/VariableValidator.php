<?php
class VariableValidator extends ValidatorBase
{
    public function Is($input){
        $varNameValidator=new VarNameValidator();
        $arr = explode('@',$input);
        if (count($arr)!=2)
        {
        	throw new SyntaxException("Not a variable name");
        }
        
        return ($arr[0]=="LF" || $arr[0]=="TF" || $arr[0]=="GF") && $varNameValidator->Is($arr[1]);

    }
}