//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract PositiveNegative{
    int private num; 

    function setNumber(int _num) public{
        num = _num;
    }  
    
    function PosNeg() public view returns (string memory res){
        if (num < 0){
            res = "This number is negative";
        }
        else{
            res = "This number is positive";
        }
        return res;
    }  

}