# XAccount

## Project Overview
Inspired by Impersonator XAccount aims to solve usability problem of governance actions.
Sometimes actions can be complex especially with cross-chain operations, which creates barrier for participants to join governance.
XAccount solves problem by providing account abstraction UI for executing different actions cross-chain, user can interact with different dapps yet having full control of process managing dapp transactions.

## Team

- [Cometsheepboy](https://github.com/cometsheepboy)

## Team Code repos

- https://github.com/ringecosystem/xaccount-ui

## Grant Information

- **Key Contributor**: Cometsheepboy
- **Estimated Duration**: 10 Days
- **Budget**: 2500 USDC
- **Payee Wallet Address**: 0x3fdA56D2c2926E2027aF19F1D58C0Dd4b3b0E20b

### Tasks

#### Infrastructure and Core Feature development

1. **Build minimal User Interface for XAccount contracts**

   - Build project's initial architecture using React, Typescript, Tailwind and Wagmi
   - Add support of XAccount contract to generate actions and create XAccount via factory
   - Add wallets support using rainbow kit providers
   - Estimate performance bottlenecks using iFrame as vendor service providor display and find the best
     approach to render vendor dapps.
   - Add two chains for cross chain tests

2. **Cross-chain stage**

   - Add more chains support, investigate possible gas and rpc issues
   - Debug each chain pair to properly work with vendor dapps
   - Add support to wallet connect links

3. **Wallet connect iFrame implementation**

  - Focus on handling full user flow in vendor dapps via wallet connect links
  - Add action tracking for latest action performed

4. **Indexing backend and action history**

  - Implement initial backend using Nodejs and Postgres to index each XAccount with corresponding
    EOA address created it, make it securely accessible via UI
  - Add features for action history handling to each used dapp, once user made some action this action is going to be stored on the backend side

5. **Sub-accounts**

   - Implement XAccount subaccount feature to manage multi-account XACcount wallets
     it might require additional backend services implementation and UI improvements

