//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract FactorialUsingForLoop{
    /*int private num; 

    function setNumber(int _num) public{
        num = _num;
    }*/
    
    function factorial(int num) pure public returns (int res){

        if (num == 0){
            res = 1;
        }
        else{
            int facto = 1;
            for(int i = 1; i <= num; i++){
                facto = facto*i;
            }
            res = facto;
        }
        return res;
    }

}