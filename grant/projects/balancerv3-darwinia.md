## Balancer V3 on Darwinia Network

### Project Description

This grant aims to bring the widely-used and mature AMM solution, Balancer V3, to the Darwinia Chain. Balancer V3 ([https://balancer.fi/](https://balancer.fi/)) offers a robust set of AMM functionalities and a user-friendly interface. The primary goal is to provide a comprehensive AMM solution for Darwinia, leveraging the capabilities of Balancer V3.

The core functionalities of the AMM, including Pool Creation and Adding Liquidity, will be based on the Balancer V3 contracts ([https://github.com/balancer/balancer-v3-monorepo](https://github.com/balancer/balancer-v3-monorepo)). While the necessary contracts will be deployed by Echo, the official Balancer UI does not currently support Darwinia. Therefore, this project involves forking and adapting the required Balancer repositories to enable support for the Darwinia Chain.

### Engineering Implementation

**1. Create Pool Functionality:**

- Balancer's pool creation is handled by a separate application: [https://pool-creator.balancer.fi/v3](https://pool-creator.balancer.fi/v3).
- We will need to fork the [https://github.com/balancer/pool-creator](https://github.com/balancer/pool-creator) repository to add support for Darwinia Chain. The approach will be similar to how other chains are supported in the existing codebase.

**2. Add Liquidity Functionality:**

- The `pool-creator` repository is relatively independent but lacks the UI for adding liquidity.
- We will fork the [https://github.com/balancer/frontend-monorepo](https://github.com/balancer/frontend-monorepo), which is the official Balancer frontend UI.
- For Darwinia, we only require the "Pools" module from this monorepo. Swap functionality will be implemented by Helixbox using the Balancer Smart Order Router (SOR) ([https://docs.balancer.fi/tools/core/smart-order-router.html](https://docs.balancer.fi/tools/core/smart-order-router.html)).
- Other modules in the Balancer official UI can be removed, retaining only the "Pools" section.

**3. Other Considerations:**

- The `pool-creator` and `frontend-monorepo` are dependent on [https://github.com/balancer/b-sdk](https://github.com/balancer/b-sdk) and [https://github.com/balancer/backend](https://github.com/balancer/backend). These repositories will need to be handled first, including configuring Balancer contract addresses.
- Forked repositories will be hosted under the [https://github.com/ringecosystem](https://github.com/ringecosystem) organization, with assistance from Yalin Cai.
- Indexing and deployment needs during this period will be assisted by Yalin Cai.
- Contract configurations (though contracts themselves should not require modification) will be assisted by Echo Hu.
- Reference material for Balancer contracts: [https://github.com/balancer/scaffold-balancer-v3](https://github.com/balancer/scaffold-balancer-v3).

### Team

- [Snoopy1412](https://github.com/snoopy1412)
- [Bear Wang](https://github.com/boundless-forest) from Helixbox
- [Echo Hu](https://github.com/hujw77) from Helixbox
- [Yalin Cai](https://github.com/fewensa) from Helixbox

### Team Code Repos

- Forked repositories will be under: [https://github.com/ringecosystem](https://github.com/ringecosystem)
  - `ringecosystem/pool-creator` (fork of `balancer/pool-creator`)
  - `ringecosystem/frontend-monorepo` (fork of `balancer/frontend-monorepo`)
  - `ringecosystem/b-sdk` (fork of `balancer/b-sdk`)
  - `ringecosystem/backend` (fork of `balancer/backend`)

## Grant Information

**Key Contributor**: Snoopy1412, Helixbox (Bear Wang, Echo Hu, Yalin Cai)

### **Phase 1**

- **Estimated Duration**: 5 weeks
- **Cost**: 2000 USD
- **Address**: 0x3d6d656c1bf92f7028Ce4C352563E1C363C58ED5

#### Tasks:

1.  **Repository Forking and Setup:**

    - **Objective**: Fork the necessary Balancer repositories (`pool-creator`, `frontend-monorepo`, `b-sdk`, `backend`) into the `ringecosystem` GitHub organization.
    - **Implementation Focus**: Initial setup, build configurations, and dependency management for the forked repositories.

2.  **Darwinia Chain Integration for `b-sdk` and `backend`:**

    - **Objective**: Configure and adapt the `b-sdk` and `backend` repositories to support the Darwinia Chain.
    - **Implementation Focus**: Add Darwinia network configurations, update contract addresses, and ensure basic interaction with Darwinia nodes.

3.  **`pool-creator` Adaptation for Darwinia:**

    - **Objective**: Modify the forked `pool-creator` application to enable pool creation on the Darwinia Chain.
    - **Tech Stack**: Based on the existing `pool-creator` stack.
    - **Implementation Focus**: UI adjustments for Darwinia, integration with the Darwinia-configured `b-sdk`, and contract interaction logic for pool deployment.

4.  **`frontend-monorepo` Adaptation for Darwinia (Pools Module):**

    - **Objective**: Adapt the "Pools" module within the forked `frontend-monorepo` to display and manage liquidity pools on Darwinia.
    - **Tech Stack**: Based on the existing `frontend-monorepo` stack (likely React/Vue or similar).
    - **Implementation Focus**: UI to list pools, view pool details, and interface for adding/removing liquidity, connecting to the Darwinia-configured `b-sdk` and `backend`. Remove unnecessary modules.

5.  **Testing and Deployment:**
    - **Objective**: Thoroughly test the integrated solution on Darwinia testnet and prepare for mainnet deployment.
    - **Implementation Focus**: Unit tests, integration tests, user acceptance testing (UAT), and deployment scripts/documentation.

## Additional Information

This project is a significant undertaking to enhance the DeFi capabilities of the Darwinia network. The Itering team, with its experience in the Darwinia ecosystem, is well-suited to execute this grant. Collaboration with the Balancer community and leveraging their existing open-source components will be key to successful delivery. The grant will cover the development effort required to fork, adapt, integrate, and test these components for the Darwinia Chain
