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

## Team Code Repos

- https://github.com/wuminzhe/offchain-resolver  
  This is the mono-repo for this project. All the code related is put here.

## Development Roadmap

### Milestone 1

Estimated Duration: 4 ~ 6 weeks

Cost: 1 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Requirement gathering.
2. Contracts  
   1. Implement an OffchainResolver contract.   
   2. Implement a SubnameRegistry contract. 
   3. Audit the contracts.
   4. Deploy to testnet.
3. Gateway  
   1. Implement a gateway to facilitate communication between Ethereum and Darwinia Chain.
   2. Deploy to testnet.
5. UI
    1. Implement a sophiscated wallet connect logic.
    2. Implement logic for
       1. registration with a fixed fee.
       2. transfer.
    3. Deploy to testnet.
6. Production deployment

### Additional Information

#### Future work

1. Cross-chain data fetching with storage proofs.  
   This solution does not require a independent signer. Instead, it uses the data availability feature of Darwinia Chain.  
   Ref: https://github.com/ensdomains/evmgateway

2. Fully offchain subname resolution.  
   This solution will be fully offchain. It will not require any onchain interaction.
