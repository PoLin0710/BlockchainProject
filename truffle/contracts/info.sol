// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2;

contract Info{
    mapping(address => uint256) public creditPoints;
    mapping(address => bool) public isCreate;
    mapping(address => mapping(address => bool)) voted;

    constructor(){}

    modifier checkNewUser(address user){
        require(!isCreate[user],"This address is created!");
        _;
    }

    modifier checkOldUser(address user){
        require(isCreate[user],"This address isn't created!");
        _;
    }

    modifier checkVoted(address to ,address from){
       require(!voted[to][from],"Is visited!"); 
       _;
    }

    function createInfo(address user) external checkNewUser(user){
        creditPoints[user]=100;
        isCreate[user]=true;
    }

    function vote(address to ,address from,bool like)external checkOldUser(from) checkOldUser(to) checkVoted(to,from){
        if(like)
        creditPoints[to]++;
        else 
        creditPoints[to]--;

        voted[to][from]=true;
    }

}