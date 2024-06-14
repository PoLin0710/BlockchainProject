module.exports = {
  networks: {
    development: {
      host: "ganache",
      port: 8545,
      network_id: "*" // Match any network id
    }
  },
  compilers: {
    solc: {
      version: "0.8.2" // Fetch exact version from solc-bin (default: truffle's version)
    }
  }
};
