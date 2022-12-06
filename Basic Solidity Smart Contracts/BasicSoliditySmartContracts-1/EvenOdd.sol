//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract EvenOdd{
    int private num; 

    function setNumber(int _num) public{
        num = _num;
    }  
    
    function Even_Odd() public view returns (string memory res){
        if (num%2 == 0){
            res = "This number is even";
        }
        else{
            res = "This number is odd";
        }
        return res;
    }  

}