# Degov Phase 3: Advanced DAO Agent System

## Description
This project aims to develop an advanced DAO agent system that enhances governance participation through automated proposal monitoring, intelligent voting strategies. The system will leverage AI and blockchain technology to create a more efficient and inclusive DAO governance process.

## Team
- [Nada](https://github.com/casinoyoda)
- [Bear Wang](https://github.com/boundless-forest) from Itering
- [Echo](https://github.com/hujw77) from Itering
- [Yalin Cai](https://github.com/fewensa) from Itering
- [Yuqi Lau](https://github.com/DreUncle) from Itering

### Code Repositories
- https://github.com/casinoyoda/degovagent

## Grant Information
- Estimatd Duration: 6 weeks
- Cost: 3000 USD

## Proposal Details

### Deliveries
1. Open Source Code Repository
   - Complete source code for the DAO agent system
   - Build and deployment scripts
   - Integration tests

2. Comprehensive Documentation
   - Detailed system architecture documentation
   - Step-by-step installation guide
   - API documentation and usage examples
   - Deployment guide

## Technology Stack

- **Programming Language**: Python 3.12+
- **LLM**: Claude & MCP
- **Knowledge**: [Cognee](https://github.com/topoteretes/cognee)
- **Database**: PostgreSQL
- **MCP servers**:
  - [Twitter](https://github.com/adhikasp/mcp-twikit)
  - [Cognee](https://github.com/topoteretes/cognee/tree/main/cognee-mcp): Agent memory
  - Degov MCP: Proposal scraping, voting on chain

## System Architecture

### High-Level Components

```mermaid
graph TD
    CAS[Core Agent System] --> MCP[MCP Router]
    MCP <--> KB[Knowledge Base MCP]
    MCP <--> OA[On-Chain Action MCP]
    MCP <--> Twitter[Twitter MCP]
    
    Scheduler[Task Scheduler] --> CAS
    CAS --> Scheduler
```

### Component Description

1. **Core Agent System**
   - Manages LLM interactions via Claude API
   - Communicates with MCP Server to trigger external actions
   - Receives and processes task requests from the Task Scheduler
   - Maintains and updates memory for proposal-related tasks

2. **Task Scheduler**
   - Periodically triggers the agent to perform specific tasks
   - Tasks include:
     - Scraping new proposals
     - Publishing proposal updates on Twitter
     - Responding to Twitter comments
     - Collecting community opinions on proposals and executing votes accordingly

3. **Cognee MCP**
   - Maintains agent memory
   - Provides relevant context for agents

4. **Degov MCP**
   - Maintains proposals in the DB
   - Supports voting on-chain
   - Scrapes proposals

## Workflow Designs

### 1. Proposal Status Update Workflow

```mermaid
sequenceDiagram
    participant TS as Task Scheduler
    participant A as Agent
    participant KB as Cognee MCP
    participant OA as Degov MCP
    participant TW as Twitter MCP
    participant DB as Database

    Note over TS: Update Proposals
    TS->>A: Request Status Update
    A->>OA: Update Proposals
    KB->>A: Task ID
    OA->>DB: Store New Proposals
```

### 2. Handling New Proposal Workflow

```mermaid
sequenceDiagram
    participant TS as Task Scheduler
    participant A as Agent
    participant KB as Cognee MCP
    participant DB as Database

    Note over TS: Process New Proposals
    TS->>A: Request to Process New Proposal
    A->>KB: Retrieve Context
    KB->>DB: Query DB
    DB->>KB: Return the Proposal
    KB->>A: Return
    A->>KB: Generate Summary and knowledge graph
    KB->>DB: Save
```

### 3. Publish Proposal Updates on Twitter

```mermaid
sequenceDiagram
    participant TS as Task Scheduler
    participant A as Agent
    participant KB as Cognee MCP
    participant TW as Twitter MCP
    participant DB as Database

    Note over TS: Publish updates on Twitter
    TS->>A: Request to Publish Proposal Updates
    A->>KB: Retrieve Context
    KB->>DB: Query DB
    DB->>KB: Return the Proposal
    KB->>A: Relatded Proposal
    A->>TW: Post Tweets
    TW-->>A: Tweets IDs
    A->>KB: Save Tweet IDs
```

### 4. On-Chain Voting Workflow

```mermaid
sequenceDiagram
    participant TS as Task Scheduler
    participant A as Agent
    participant KB as Cognee MCP
    participant TW as Twitter MCP
    participant OA as Degov MCP

    Note over TS: Voting on Chain
    TS->>A: Request to Vote on Chain
    A->>KB: Query Realted Tweets IDs
    KB-->>A: Return
    A->>TW: Query Votes and Comments
    TW->>A: Return
    A->>A: Make Decision
    A->>OA: Vote on Chain
``` 

### 5. Twitter Comments Interaction Workflow

```mermaid
sequenceDiagram
    participant TS as Task Scheduler
    participant A as Agent
    participant KB as Cognee MCP
    participant TW as Twitter MCP
    participant OA as Degov MCP

    Note over TS: Monitor Comments
    TS->>A: Check Comments
    A->>TW: Query Comments
    TW-->>A: Return
    A-->>KB: Retrieve Context
    KB->>A: Return
    A->>A: Generate Reply with Context
    A->>TW: Reply
```
