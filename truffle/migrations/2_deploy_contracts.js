// migrations/2_deploy_contracts.js
const info = artifacts.require("userInfo");

module.exports = function (deployer) {
  deployer.deploy(info);
};
