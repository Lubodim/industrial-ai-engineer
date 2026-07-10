# Industrial AI Engineer

**Industrial AI Engineer** is a local multi-agent AI system for analysis and optimization of digital twins of industrial products.

The project is developed as a master's thesis prototype in the field of Industrial Robotics. Its goal is to support engineers in analyzing product variants, materials, production technologies, cost, quality and manufacturing efficiency.

## Main Idea

The system builds a library of digital twins of manufacturing products.  
Each digital twin can contain:

- CAD model
- Images
- Technical parameters
- Material data
- Manufacturing technology
- Cost parameters
- Production time
- Quality indicators
- Experiments and versions

## Architecture

The system follows a multi-agent architecture:

- **External Research Agent**  
  Searches public information about materials, technologies and market prices.

- **Internal AI Engineer Agent**  
  Works locally without internet access and analyzes internal digital twin data.

- **Economics Agent**  
  Calculates material cost, machine cost, selling price and expected profit.

- **Production Agent**  
  Analyzes production time and manufacturing parameters.

- **Vision Agent**  
  Processes images and CAD-related visual information.

## Security Concept

The project is designed as an on-premise solution.  
Sensitive production data should remain inside the company network.

The external agent has access only to public data, while the internal AI agent works only with local files, local databases and validated research data.

## Current Status

Version: `0.1.0`

Implemented:

- Core digital twin models
- Material model
- Technology model
- Product model
- Experiment model
- Analysis result model
- Basic economic calculations
- Cost calculator agent

## Planned Features

- Industrial AI Engine
- Agent Orchestrator
- Local LLM integration through Ollama
- GUI with PySide6
- Digital twin library
- Experiment comparison
- PDF reports
- Computer vision module
- Machine learning models for cost and quality prediction

doc structure:
Industrial-AI-Engineer/
│
├── docs/
│   ├── 01_Introduction.md
│   ├── 02_System_Architecture.md
│   ├── 03_Digital_Twin_Platform.md
│   ├── 04_AI_Architecture.md
│   ├── 05_Agent_Architecture.md
│   ├── 06_Database_Design.md
│   ├── 07_Engineering_Engine.md
│   ├── 08_GUI_Architecture.md
│   ├── 09_Project_Roadmap.md
│   │
│   ├── diagrams/
│   │   ├── architecture.drawio
│   │   ├── class_diagram.drawio
│   │   ├── use_case.drawio
│   │   ├── sequence.drawio
│   │   └── database.drawio
│   │
│   └── images/
│       ├── architecture.png
│       ├── gui_mockup.png
│       └── logo.png
│
├── research/
│   ├── references.md
│   ├── related_work.md
│   └── papers/