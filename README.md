# 🏠 AI-Powered Smart Home Digital Twin & Agentic IoT System

[cite_start]A real-time **Digital Twin** ecosystem that connects an **AI Agent (LLM)** with a 3D virtual environment[cite: 33, 98]. [cite_start]This project enables natural language interaction to control a smart home simulation, featuring high-performance communication between **Unity (C#)** and **AWS-hosted backend**[cite: 34, 84, 100].

![Unity](https://img.shields.io/badge/Unity-2022.3+-black?logo=unity&logoColor=white)
![C#](https://img.shields.io/badge/C%23-DotNet-239120?logo=dotnet&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Infrastructure-FF9900?logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)

---

## 🏗 System Architecture

[cite_start]The project bridges the gap between **Cloud AI** and **3D Simulation**[cite: 68, 70]:
1. [cite_start]**Unity Client (The Body)**: Captures voice, renders the digital twin, and executes physical actions[cite: 84, 100].
2. [cite_start]**WebSocket Bridge (The Nerve System)**: Low-latency data transfer using FastAPI and Redis[cite: 66, 73, 106].
3. [cite_start]**LLM Agent (The Brain)**: Processes intent using **Qwen2.5-7B** and generates JSON-based IoT commands[cite: 88, 91, 103].

---

## 🛠 My Contributions (Simulation & Integration)

[cite_start]As the **Unity & Integration Lead** (Barış Bideci [cite: 3, 25]), I developed the following core components:

### 1. 3D Digital Twin Development (Unity/C#)
* [cite_start]**Virtual Environment**: Designed a comprehensive smart home layout with interactive IoT objects like HVAC and lighting[cite: 84, 98, 104].
* [cite_start]**State Synchronization**: Developed a C# state-management system to sync cloud-based device statuses with the 3D simulation in real-time[cite: 85, 104].
* [cite_start]**Audio Pipeline**: Implemented a system to capture microphone input, convert `.wav` data into **byte arrays**, and stream it via WebSockets for STT processing[cite: 66, 100].

### 2. High-Performance Bridge & Logic
* [cite_start]**Asynchronous C# Integration**: Built a non-blocking WebSocket client in Unity to ensure the simulation frame rate remains stable during heavy data I/O[cite: 84, 117].
* [cite_start]**JSON Command Mapping**: Engineered a parser to translate LLM-generated JSON into specific C# events within the game engine[cite: 91, 103, 104].
* [cite_start]**Dynamic UI/UX**: Created real-time visual feedback for the LLM's status, observing system changes in real-time within the Unity environment[cite: 68, 69].

---

## 🧠 AI & Backend Stack

* **Models**: 
    * [cite_start]**STT**: Faster-Whisper (Optimized for low latency)[cite: 87, 101].
    * [cite_start]**LLM**: Qwen2.5-7B-BF16 via **Ollama**[cite: 88, 90].
    * [cite_start]**TTS**: Coqui TTS-v2 for natural voice feedback[cite: 93, 105].
* [cite_start]**Infrastructure**: Deployed on **AWS** using **Docker**, **Redis**, and **Traefik** for load balancing and SSL/TLS termination[cite: 73, 76, 78, 81].

---

## 📂 Project Structure
AI-Smart-Home/
├── unity_project/            # My Core Work: The Digital Twin
│   ├── Assets/Scripts/
│   │   ├── Network/          # WebSocket & Byte Stream Logic
│   │   ├── IoT/              # Device Controllers (C#)
│   │   └── Audio/            # Mic Capture & Processing
├── server/                   # FastAPI WebSocket Server
├── terraform/                # Infrastructure as Code
└── docker-compose.yml
---

## 📝 Performance Highlights

* [cite_start]**Low Latency**: Achieved real-time response times for end-to-end voice-to-action cycles[cite: 106].
* [cite_start]**Scalability**: Used Redis Pub/Sub to allow multiple simulation instances to connect to the same LLM controller[cite: 73, 74].

---

### 🎓 Academic Context
[cite_start]This project was developed as the **BM201 Advanced Programming Lab Project** at **Gazi University**, Computer Engineering Department[cite: 6, 7, 8, 9].
