// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract FindPrimeBetweenNumbers {
    uint[] private prime_arr;
    uint private flag;

    function prime(uint num1, uint num2) public{
        for (uint i = num1; i <= num2; i++){
            if(i == 1 || i == 0){
                continue;
            }

            flag = 1;

            for (uint j = 2; j <= i/2; ++j) {
                if (i % j == 0) {
                    flag = 0;
                    break;
                }
            }

            if(flag == 1){
                prime_arr.push(i); 
            }
        }
    }

    function getPrime() public view returns(uint[] memory) {
        return prime_arr;
    }
}