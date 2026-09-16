---

applicant: Helixbox
type: Research, Development, Community Building, Security Audit, and Application Coordination
timeline: 2026-Q4
costs: 18,000 USD + 1,500 USD * runtime upgrade + 500 USD * hotfix
payment: 0xa8a0b5bEA167E9cDBaAAB52D9EF745Ea3c9fc73D (Ethereum, Base, Arbitrum, Optimism)

---

Draft for review — September 16, 2026. The service period is October–December 2026, and the progress summary covers June 16–September 16, 2026.

# Overview

Helixbox proposes to continue supporting the RingDAO ecosystem in Q4 2026, with a focus on security, reducing the burden of chain maintenance, and developing DeGov's governance tools and data services.

Over the past three months, we continued improving DeGov and the DeGov Agent API, supported the RingDAO–KtonDAO unwinding process, and worked on ecosystem maintenance and the response to the KTON bridge incident. In the upcoming quarter, our priorities are to migrate KTON to Ethereum, research a possible transition of Darwinia to an Ethereum-based token model, and continue DeGov development.

The requested base budget for this quarter is 18,000 USD, plus 1,500 USD per runtime upgrade and 500 USD per hotfix.

# Team Information

## Members and Roles

- [Denny Wang](https://github.com/hackfisher) Architect & Security Specialist
- [Echo Hu](https://github.com/hujw77) Smart Contract Developer & Security Auditor
- [Bear Wang](https://github.com/boundless-forest) Core Developer & Community Coordinator
- [YaLin Cai](https://github.com/fewensa) Core Developer & DevOps
- [Xavier Lau](https://github.com/AurevoirXavier) Core Developer

## Contact Information

- Contact name: Bear Wang
- Contact email: bear.wang@helixbox.ai

## Legal Structure

- Company Name: Helixbox Labs

# Completed Work and Recent Progress

The following highlights summarize our work over the past three months:

1. Continued improving DeGov's governance experience, including proposal drafts, indexing reliability, and fixes to proposal and voting data. We also updated the DeGov Square interface to make browsing DAOs and navigating governance services more consistent. Examples include [proposal draft support](https://github.com/ringecosystem/degov/pull/1101) and the [Square interface update](https://github.com/ringecosystem/degov-apps/pull/328).
2. Advanced [DeGov Atlas](https://atlas.degov.ai) and the DeGov Agent API beyond the initial preview, improving DAO search, governance feeds, proposal and voter data, and the reliability of data processing. We also improved API access for agents and partners, maintained the governance research and proposal security skills, and updated the [documentation](https://docs.degov.ai/) to reflect the product's development.
3. Supported the RingDAO–KtonDAO unwinding process through governance coordination and implementation work. This included [disabling new RING deposits for KTON](https://github.com/darwinia-network/DIP-7/pull/40) while retaining the existing withdrawal functions, alongside [staking interface updates](https://github.com/ktondao/kton-staking-ui/pull/13) explaining the phase-out of new RING rewards and continued access to previously earned rewards.
4. Continued bridge maintenance and supported the response to the September KTON bridge incident, including investigation, a runtime security fix, partial fund recovery, and recovery planning. The [published postmortem](https://github.com/orgs/ktondao/discussions/56) documents the partial recovery and completed runtime upgrade. Bridge reconciliation and the remaining recovery work were still ongoing in the latest records reviewed for this draft.

# Services Planned for the Upcoming Quarter

## KTON Migration to Ethereum

For security reasons, we plan to migrate KTON from Darwinia to Ethereum during Q4. The goal is to reduce KTON's dependence on Darwinia's runtime and cross-chain infrastructure while preserving token holders' balances and rights.

The work will include reconciling KTON supply and balances across both chains, accounting for staking and contract-held positions, preparing and testing the migration mechanism, and coordinating the necessary governance actions. We will also update the relevant applications and provide clear instructions for holders. The migration plan will account for the bridge incident's outstanding recovery obligations.

## Research into a Darwinia Transition to Ethereum

We will investigate the technical requirements for moving from operating the Darwinia chain to supporting RING as an ERC-20 token on Ethereum.

As AI capabilities continue to improve, we expect the security demands and maintenance costs of running a separate blockchain to increase. We therefore believe it is worth evaluating whether an Ethereum-based model could reduce this burden and allow more resources to go toward applications such as DeGov.

The research will cover token balances and supply, staking and locked positions, bridge reserves, governance, and the treatment of existing applications. We will compare migration approaches and prepare a technical assessment covering feasibility, risks, dependencies, and a possible implementation sequence. The Q4 deliverable is this assessment; any decision to carry out the broader migration will require a separate community discussion and governance process.

## Continued DeGov and DeGov Agent API Development

We will continue developing and maintaining DeGov, DeGov Square, DeGov Atlas, and the DeGov Agent API. Our priorities are to improve governance data accuracy and coverage, make proposals and voting activity easier to understand, and provide reliable access for AI agents and partner integrations.

This includes ongoing improvements to indexing and data processing, user interfaces, agent skills, and documentation, together with bug fixes and security updates. We will also continue the necessary maintenance and technical support for Darwinia and existing ecosystem services while the migration and research work progresses.
