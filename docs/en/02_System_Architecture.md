# System Architecture

## Overview

Industrial AI Engineer follows a modular and layered architecture designed for industrial environments where data security, maintainability and scalability are critical requirements.

The system is developed as an **On-Premise** application, meaning that all sensitive engineering and production information remains inside the company network.

Instead of relying on a single AI model, the platform adopts a **Multi-Agent Architecture**, where specialized agents perform individual engineering tasks while being coordinated by a central orchestration engine.

---

# High-Level Architecture

```text
                               Industrial AI Engineer

┌─────────────────────────────────────────────────────────────────────────────┐
│                                   GUI Layer                                │
│                                                                             │
│ Dashboard │ Digital Twin Library │ Experiments │ Reports │ AI Assistant     │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Industrial AI Engine                           │
│                                                                             │
│ Task Router │ Agent Orchestrator │ Decision Engine │ Event Manager          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
            ┌─────────────────────────┼──────────────────────────┐
            ▼                         ▼                          ▼

┌────────────────┐        ┌────────────────┐          ┌─────────────────────┐
│ Digital Twin   │        │ AI Platform    │          │ Engineering Engine  │
│ Platform       │        │                │          │                     │
└────────────────┘        └────────────────┘          └─────────────────────┘
            │                         │                          │
            └──────────────┬──────────┴──────────────┬───────────┘
                           ▼                         ▼
                  ┌─────────────────────────────────────────────┐
                  │               Data Layer                    │
                  └─────────────────────────────────────────────┘
```

---

# Architectural Layers

The application is divided into six independent layers.

## 1. Presentation Layer

Responsible only for user interaction.

Responsibilities:

- User Interface
- Product Library
- Experiment Management
- AI Chat
- Reports
- Visualization

This layer does not contain any business logic.

---

## 2. Core Layer

The Core Layer acts as the operating system of the application.

Main responsibilities:

- task routing
- agent orchestration
- workflow execution
- communication between modules
- configuration
- logging
- exception handling

All communication between modules passes through the Core Layer.

---

## 3. Digital Twin Platform

The Digital Twin Platform is the central component of the application.

It manages the complete lifecycle of industrial products.

Hierarchy:

```text
Project

    │

    ▼

Product

    │

    ▼

Version

    │

    ▼

Experiment

    │

    ▼

Analysis Result
```

Each Digital Twin contains:

- CAD models
- Images
- Material
- Technology
- Manufacturing parameters
- Economic parameters
- Experiment history
- Reports

---

## 4. AI Platform

The AI Platform consists of specialized intelligent agents.

Each agent performs a dedicated engineering task.

Current agents:

- Research Agent
- AI Engineer
- Economics Agent
- Production Agent
- Vision Agent

Future agents:

- Maintenance Agent
- Robot Programming Agent
- Energy Optimization Agent
- Quality Prediction Agent

The AI Platform does not communicate directly with the GUI.

All communication is managed through the Core Layer.

---

## 5. Engineering Engine

Unlike AI agents, this module contains deterministic engineering logic.

It provides:

- engineering formulas
- manufacturing rules
- material rules
- production rules
- optimization algorithms

The Engineering Engine guarantees deterministic calculations.

Artificial Intelligence is used only to interpret the results.

---

## 6. Data Layer

The Data Layer stores all project information.

Supported data:

- Digital Twins
- Materials
- Technologies
- Experiments
- Reports
- Images
- CAD files
- Machine Learning datasets
- AI Knowledge Base

Storage technologies:

- SQLite
- JSON
- CSV
- Local file system

Future support:

- PostgreSQL
- SQL Server

---

# Agent Communication

All AI agents communicate only through the Agent Orchestrator.

```text
User

   │

   ▼

GUI

   │

   ▼

Industrial AI Engine

   │

   ▼

Agent Orchestrator

   │

   ├────────► Economics Agent

   ├────────► Production Agent

   ├────────► Vision Agent

   ├────────► Research Agent

   └────────► AI Engineer
```

This architecture ensures:

- modularity
- maintainability
- scalability
- security

---

# Security Concept

The application follows an On-Premise architecture.

Sensitive company information never leaves the local network.

The system separates AI agents into two categories.

## External Agent

Capabilities:

- Internet access
- Public information retrieval
- Material prices
- Manufacturing technologies
- Public engineering knowledge

Restrictions:

- No access to Digital Twins
- No access to production database
- No access to confidential company data

---

## Internal AI Engineer

Capabilities:

- Local reasoning
- Product analysis
- Experiment comparison
- Engineering recommendations

Restrictions:

- No Internet access
- No cloud services
- Local LLM only

This separation minimizes the risk of confidential information leakage.

---

# Scalability

The architecture allows new AI agents to be added without modifying existing modules.

Example:

```text
Industrial AI Engine

        │

        ▼

Agent Orchestrator

        │

        ├── Economics Agent

        ├── Vision Agent

        ├── Research Agent

        ├── AI Engineer

        └── Energy Agent (future)
```

Each new agent implements a common communication interface.

---

# Benefits

The proposed architecture provides:

- modular design
- high maintainability
- clear separation of responsibilities
- secure local deployment
- easy scalability
- support for Digital Twins
- support for Artificial Intelligence
- support for Computer Vision
- support for Machine Learning

The architecture has been designed to support future integration with industrial automation systems such as PLCs, robots, MES and ERP platforms.