# 🏠 AI-Powered Smart Home Digital Twin & Agentic IoT System

A real-time **Digital Twin** ecosystem that connects an **AI Agent (LLM)** with a 3D virtual environment. This project enables natural language interaction to control a smart home simulation, featuring high-performance communication between **Unity (C#)** and **AWS-hosted backend**.

![Unity](https://img.shields.io/badge/Unity-2022.3+-black?logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-DotNet-239120?logo=dotnet&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Infrastructure-FF9900?logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)

---

## 🏗 System Architecture

The project bridges the gap between **Cloud AI** and **3D Simulation**:
1. **Unity Client (The Body)**: Captures voice, renders the digital twin, and executes physical actions.
2. **WebSocket Bridge (The Nerve System)**: Low-latency data transfer using FastAPI and Redis.
3. **LLM Agent (The Brain)**: Processes intent using **Qwen2.5-7B** and generates JSON-based IoT commands.

---

## 🛠 My Contributions (Simulation & Integration)

As the **Unity & Integration Lead** (Barış Bideci), I developed the following core components:

### 1. 3D Digital Twin Development (Unity/C#)
* **Virtual Environment**: Designed a comprehensive smart home layout with interactive IoT objects like HVAC and lighting.
* **State Synchronization**: Developed a C# state-management system to sync cloud-based device statuses with the 3D simulation in real-time.
* **Audio Pipeline**: Implemented a system to capture microphone input, convert `.wav` data into **byte arrays**, and stream it via WebSockets for STT processing.

### 2. High-Performance Bridge & Logic
* **Asynchronous C# Integration**: Built a non-blocking WebSocket client in Unity to ensure the simulation frame rate remains stable during heavy data I/O.
* **JSON Command Mapping**: Engineered a parser to translate LLM-generated JSON into specific C# events within the game engine.
* **Dynamic UI/UX**: Created real-time visual feedback for the LLM's status, observing system changes in real-time within the Unity environment.

---

## 🧠 AI & Backend Stack

* **Models**: 
    * **STT**: Faster-Whisper (Optimized for low latency).
    * **LLM**: Qwen2.5-7B-BF16 via **Ollama**.
    * **TTS**: Coqui TTS-v2 for natural voice feedback.
* **Infrastructure**: Deployed on **AWS** using **Docker**, **Redis**, and **Traefik** for load balancing and SSL/TLS termination.

---

## 📂 Project Structure

```text
AI-Smart-Home/
├── unity_project/           # Digital Twin (Barış Bideci)
│   └── Assets/
│       └── Scripts/
│           ├── Network/     # WebSocket & Byte Stream Bridge
│           ├── IoT/         # C# Device State Controllers
│           └── Audio/       # Mic Capture & PCM Data Processing
├── server/                  # FastAPI & WebSocket Logic
│   ├── app/
│   │   ├── main.py
│   │   └── connection_manager.py
│   └── Dockerfile
├── terraform/               # Infrastructure as Code (AWS)
│   ├── main.tf
│   └── variables.tf
└── docker-compose.yml       # Orchestration (Redis, Traefik, App)
```
---

## 📝 Performance Highlights

* **Low Latency**: Achieved real-time response times for end-to-end voice-to-action cycles.
* **Scalability**: Used Redis Pub/Sub to allow multiple simulation instances to connect to the same LLM controller.

---

### 🎓 Academic Context
This project was developed as the **BM201 Advanced Programming Lab Project** at **Gazi University**, Computer Engineering Department.
