// migrations/2_deploy_contracts.js
const info = artifacts.require("info");

module.exports = function (deployer) {
  deployer.deploy(info);
};
