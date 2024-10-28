# ParaLink

## Project Overview

[ParaLink](https://para.link/) is a cross-chain asset exchange tool built on the Polkadot XCM (Cross-Consensus Messaging) technology stack. The project is dedicated to creating a seamless cross-chain experience, supporting asset interoperability between parachains within the Polkadot ecosystem.

## Team

- Snoopy1412 ([@snoopy1412](https://github.com/snoopy1412))

## Team Code Repos

- https://github.com/ringecosystem/paralink

## Development Roadmap

- **Estimated Duration**: 6 weeks
- **Budget**: 2500 USD
- **Wallet Address**: 0x3d6d656c1bf92f7028Ce4C352563E1C363C58ED5

### Tasks

#### Infrastructure and Core Feature Development

1. **User Interface Development**

   - Build the project’s foundational architecture using React, TypeScript, TailwindCSS, and shadcn/ui.
   - Create a user-friendly interface to optimize the user workflow.
   - Implement comprehensive responsive design to ensure compatibility across multiple devices.
   - Integrate TanStack Query for efficient server-side state management.

2. **Web3 Integration**

   - Integrate wagmi, viem, and RainbowKit to enable interactions with EVM-compatible chains.
   - Integrate @polkadot/api and @polkadot/extension-dapp to facilitate interactions with Polkadot chains.
   - Implement intelligent chain type recognition based on user selection, automatically switching to the corresponding wallet login and interaction logic.

3. **Smart XCM Design**

   - **HRMP Channel Smart Detection**

     - Implement **automatic detection of HRMP channels between Polkadot parallel chains** to determine chain pairs eligible for XCM transfers.
     - Utilize on-chain storage data to retrieve information on all currently active parallel chain channels.

   - **Chain Type and Asset Type Smart Recognition**

     - **Automatically detect whether the target chain is an EVM-compatible chain or a Polkadot chain**, dynamically adjusting the cross-chain transfer logic and process.
     - **Automatically detect and identify asset types**, determining whether assets are native tokens, synthetic assets, or tokens on EVM chains.

   - **Automated Asset Information Retrieval**

     - **Automatically add supported asset pairs** to ParaLink, supporting a broader range of assets and reducing manual configuration and communication costs with project teams.
     - Provide querying and filtering functionalities for asset pairs to facilitate users in selecting the assets they wish to transfer.
     - Reference the [XCM Global Registry](https://github.com/colorfulnotion/xcm-global-registry/tree/action/assets/polkadot) to implement the retrieval and parsing of asset Location information.
     - Tailor asset information retrieval to accommodate differences in on-chain asset management modules across various chains.
     - Implement custom handling for **special assets** that cannot be processed automatically, ensuring their support within ParaLink.

   - **Frontend Display Optimization**

     - Handle the display of **Token and Network Logos** on the frontend, prioritizing data acquisition from [Subscan Assets Info](https://github.com/subscan-explorer/assets-info) and using default icons if necessary.
     - Ensure accurate display of asset and network information on the frontend, providing users with clear information.

   - **Cross-Chain Transfer Logic Enhancement**

     - **Implement cross-chain asset transfer logic between EVM chains and Polkadot chains**, enabling users to transfer assets across different types of chains.
     - Manage various potential exceptions during the cross-chain process to ensure asset security.
     - Dynamically adjust the cross-chain transfer logic and process based on automatically detected chain types and asset types.

##### PREPLK Distribution Commitment

To express our gratitude for RingDao's funding support for this project, especially in the early stages, ParaLink has launched an ERC-20 token on the Darwinia mainnet called [PREPLK (Pre ParaLink Token)](https://explorer.darwinia.network/address/0x7ED13f74FD8AE70db03Ae74666d1B443341D8A41), and has committed to distribute 20% of the total supply to the RingDao community. We hope this will help the RingDao community gain more benefits from the project and develop a long-term relationship with ParaLink.