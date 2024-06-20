// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2;

contract UserInfo{
    struct UserData {
        bool kyc_Confirm;
        string[] links;
    }

    mapping(address => bool) public isCreate;
    mapping(address => UserData) users;

    constructor(){}

    modifier checkNewUser(address user){
        require(!isCreate[user],"This address is created!");
        _;
    }

    modifier checkOldUser(address user){
        require(isCreate[user],"This address isn't created!");
        _;
    }

    function createInfo(string[] calldata links) external checkNewUser(msg.sender) {
        isCreate[msg.sender]=true;
        UserData storage user = users[msg.sender];
        user.kyc_Confirm = false;
        for (uint i = 0; i < links.length; i++) {
            user.links.push(links[i]);
        }
    }

    function getInfo() external view checkOldUser(msg.sender) returns(UserData memory) {
        return users[msg.sender];
    }

    function kycCheck() external checkOldUser(msg.sender){
        require(users[msg.sender].kyc_Confirm==false,"is confirm");
        users[msg.sender].kyc_Confirm=true;
    }

    function getLinks() external view checkOldUser(msg.sender) returns (string[] memory links){
        return users[msg.sender].links;
    }

    function removeLink(uint256 index) external checkOldUser(msg.sender){
       require(index > 0 && index < users[msg.sender].links.length,"index is isvaild");
        delete users[msg.sender].links[index];
    }

    function addLink(string calldata link) external checkOldUser(msg.sender){
        users[msg.sender].links.push(link);
    }
}