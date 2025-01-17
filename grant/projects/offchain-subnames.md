# Offchain Subnames on Darwinia Chain

## Project Description

This project aims to implement an offchain subnames solution for the 'darwinia.eth' Ethereum Name Service (ENS) domain but keeps the subname records on Darwinia Chain. 

It leverages the EIP-3668 specification to enable efficient and cost-effective management of subname-address mappings off the Ethereum mainnet. By storing these mappings on Darwinia Chain, the project offers a scalable approach to handle a large number of subdomains without incurring high gas fees.

The solution utilizes a customized OffchainResolver contract on Ethereum, which works with a gateway service connected to the Darwinia Chain. This setup allows for seamless resolution of subnames (e.g., 'foo.darwinia.eth') while maintaining the security and decentralization benefits of the ENS.

This project addresses the need for efficient subdomain management within the Darwinia ecosystem, as outlined in the RFP (https://github.com/ringecosystem/collaboration/issues/61), and demonstrates the potential for cross-chain interoperability in domain name services.

### This project will benefit the Darwinia ecosystem in the following ways:

1. It will provide a more efficient and cost-effective way to manage subdomains on the Darwinia Chain, reducing the need for users to pay high gas fees on Ethereum.
2. It will enhance the usability of the 'darwinia.eth' domain by allowing users to register, update, and resolve subnames with reduced costs and improved performance.
3. It will demonstrate the potential for cross-chain interoperability in domain name services, opening up new possibilities for collaboration and innovation within the Darwinia ecosystem.

## Team

- Aki Wu([wuminzhe](https://github.com/wuminzhe))  
  A full stack developer focused on the web3 space. He has been working on darwinia ecosystem for a long time.

- Echo([Echo](https://github.com/hujw77))  
  Contracts developer from Itering.

- Bear([Bear](https://github.com/boundless-forest))
  Project Manager from Itering. 
  
- Yuqi(yuqi.liu@itering.io)
  UI Designer from Itering.

## Team Code Repos

- https://github.com/subnames/subnames-contracts
  The repo for the subnames contracts based on [basenames](https://github.com/base-org/basenames).

- https://github.com/subnames/offchain-resolver  
  1. the offchain gateway.
  2. the offchain resolve client.
  3. based on ensdomains's [offchain-resolver](https://github.com/ensdomains/offchain-resolver).

- https://github.com/wuminzhe/subnames-ui
  Frontend User Interface.

## Development Roadmap

### Milestone 1

Estimated Duration: 2 weeks

Cost: 1000 USDT

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Configure the contracts to support "ringdao.eth" domain for testing. 
2. Deploy contracts to testnet(Darwinia Koi).
3. Implement and deploy the offchain gateway.
4. Implement the Wallet Connect button including customizing it to support subname.
5. Support registering subname and fee calculation.
6. Support extend/renew.
7. Support reverse resolution(address to domain).

Deliverables:

- The contracts source code.
- The gateway source code.
- A deployed gateway service targetting Darwinia Koi.
- The deployed contracts addresses on Darwinia Koi.
- The frontend UI for wallet connecting, registering and extend/renew on Darwinia Koi.

** Note: this milestone has done. **

### Milestone 2

Estimated Duration: 2 weeks

Cost: 500 USDT

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Configure the contracts to support "darwinia.eth" domain. 
2. Deploy contracts to Darwinia Crab.
3. Deploy the offchain gateway for Darwinia Crab.
4. An indexer for syncing the subname list from Darwinia Crab.
5. Implement the subname list page.
6. Support primary domain name.
7. Support transfer subname.

Deliverables:

- The UI source code.
- A deployed gateway service targetting Darwinia Crab.
- A deployed subnames indexer for Darwinia Crab.

### Milestone 3

Estimated Duration: 2 weeks

Cost: 500 USDT

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Profile functionality.
   1. Setting/Updating profile including avatar.
   2. Showing profile.
3. Theme to support darwinia design.

Deliverables:

- The UI source code.

### Milestone 4

Estimated Duration: 2 weeks

Cost: 500 USDT

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Deploy to mainnet(L2 Contracts on Darwinia Chain & L1 Resolver on Ethereum).
2. Deploy offchian gateway and subnames indexer
3. Bug fixing.  
4. Improve the already developed features.  

## Additional Information

Please note that this grant includes contract and solution contributions from Itering. As Itering’s work is provided separately as a Service Provider to RingDAO, compensation for these efforts is not included in the grant amount. The full grant reward will be allocated to Aki for fulfilling the grant scope, with Itering offering the necessary support.

#### Future plans

1. Cross-chain data fetching with storage proofs.  
   This solution does not require a independent signer. Instead, it uses the data availability feature of Darwinia Chain.  
   Ref: https://github.com/ensdomains/evmgateway

2. Fully offchain subname resolution.  
   This solution will be fully offchain. It will not require any onchain interaction.
