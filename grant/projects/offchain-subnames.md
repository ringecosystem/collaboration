# Offchain Subnames on Darwinia Chain

## Project Description

This project aims to implement an offchain subnames solution for the 'ringdao.eth' Ethereum Name Service (ENS) domain but keeps the subname records on Darwinia Chain. 

It leverages the EIP-3668 specification to enable efficient and cost-effective management of subname-address mappings off the Ethereum mainnet. By storing these mappings on Darwinia Chain, the project offers a scalable approach to handle a large number of subdomains without incurring high gas fees.

The solution utilizes a customized OffchainResolver contract on Ethereum, which works with a gateway service connected to the Darwinia Chain. This setup allows for seamless resolution of subnames (e.g., 'foo.ringdao.eth') while maintaining the security and decentralization benefits of the ENS.

<!-- Key features of the project include:
1. Offchain storage of subname-address mappings on Darwinia Chain
2. Integration with ENS on Ethereum using EIP-3668 for secure offchain data retrieval
3. A gateway service to facilitate communication between Ethereum and Darwinia Chain
4. User-friendly UIs for subname registration, update, and resolution.
5. Admin UI for subname management. -->

This project addresses the need for efficient subdomain management within the Darwinia ecosystem, as outlined in the RFP (https://github.com/ringecosystem/collaboration/issues/61), and demonstrates the potential for cross-chain interoperability in domain name services.

### This project will benefit the Darwinia ecosystem in the following ways:

1. It will provide a more efficient and cost-effective way to manage subdomains on the Darwinia Chain, reducing the need for users to pay high gas fees on Ethereum.
2. It will enhance the usability of the 'ringdao.eth' domain by allowing users to register, update, and resolve subnames with reduced costs and improved performance.
3. It will demonstrate the potential for cross-chain interoperability in domain name services, opening up new possibilities for collaboration and innovation within the Darwinia ecosystem.

## Team

- Aki Wu([wuminzhe](https://github.com/wuminzhe))  
  A full stack developer focused on the web3 space. He has been working on darwinia ecosystem for a long time.

- Echo([Echo](https://github.com/hujw77))  
  Contracts developer from Itering.


## Team Code Repos

- https://github.com/wuminzhe/basenames
  The repo for the basenames contracts.

- https://github.com/wuminzhe/offchain-resolver  
  1. the offchain gateway.
  2. the offchain resolve client.

- https://github.com/wuminzhe/subnames-ui
  The repo for the UI.

## Development Roadmap

### Milestone 1

Estimated Duration: 2 weeks

Cost: 0.25 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Contracts pre research & implementation.  
2. Adjust the contracts to align with Darwinia Chain.
3. Deploy to testnet(Darwinia Koi).

Deliverables:

- The contracts source code in MIT license.
- The deployed contracts address.

### Milestone 2

Estimated Duration: 2 weeks

Cost: 0.25 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Gateway  
   1. Implement the EIP-3668 offchain gateway to query the subname-address mappings from Darwinia Chain.
   2. Deploy to testnet(Darwinia Koi).

Deliverables:

- The gateway source code in MIT license.
- The deployed online gateway service.

### Milestone 3

Estimated Duration: 2 weeks

Cost: 0.25 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Implement frontend logic for
    1. wallet connect including customizing it to support subname.
    2. register including reverse register and fee calculation
    3. renew/extend
2. Deploy to testnet(Darwinia Koi).

Deliverables:

- The frontend source code in MIT license.
- The deployed online frontend ui.

### Milestone 4

Estimated Duration: 2 weeks

Cost: 0.25 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Deploy to mainnet(Darwinia Chain).

Deliverables:

- The contracts addresses on Darwinia Chain.
- The gateway service targetting Darwinia Chain.
- The frontend ui on Darwinia Chain.

## Additional Information

1. The deployed contracts's owner will be transferred to RingDAO which means RingDAO will manage the contracts.
2. The price of subname:
   - 3 letters: 100000 RING per year.
   - 4 letters: 10000 RING per year.
   - 5~9 letters: 1000 RING per year.
   - 10 letters or longer: 100 RING per year.
3. 100% of total subname sale income of the first year will be transferred to Aki. 
4. This grant includes contracts and solution contributions from Itering. As Itering’s work is provided separately as a Service Provider to RingDAO, compensation for these efforts is not included in the grant amount. The full grant reward will be allocated to Aki for fulfilling the grant scope, with Itering offering the necessary support.

#### Future plans

1. Cross-chain data fetching with storage proofs.  
   This solution does not require a independent signer. Instead, it uses the data availability feature of Darwinia Chain.  
   Ref: https://github.com/ensdomains/evmgateway

2. Fully offchain subname resolution.  
   This solution will be fully offchain. It will not require any onchain interaction.
