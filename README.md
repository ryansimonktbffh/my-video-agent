# Local AI Video Agent 🎬

An experimental, locally running AI video-generation system designed to turn natural-language ideas into cinematic videos using open-source AI models and local GPU inference.

## 🚀 Project Overview

The goal of this project is to build a personal AI video agent that can transform a simple text idea into a multi-shot video with minimal manual intervention.

The system combines a locally hosted language model for creative planning with an AI video-generation model for visual content creation.

**Current milestone:** Successfully generated a video locally using Wan2.1 Text-to-Video 1.3B.

## 🧠 Planned Architecture

```text
Natural-Language Idea
        ↓
Local LLM — Llama 3.2 3B
        ↓
Storyboard & Shot Prompts
        ↓
Wan2.1 — Text-to-Video
        ↓
Generated Video Clips
        ↓
FFmpeg — Video Assembly
        ↓
Final Video
```

## 🛠️ Technology Stack

- **Python** — application logic and orchestration
- **Ollama** — local language-model runtime
- **Llama 3.2 3B** — storyboard and prompt generation
- **WanGP / Wan2.1 1.3B** — local AI video generation
- **PyTorch** — deep-learning inference
- **CUDA** — NVIDIA GPU acceleration
- **FFmpeg** — planned video assembly

## 💻 Hardware

Developed and tested on:

- NVIDIA GeForce RTX 3050 Laptop GPU (6 GB VRAM)
- Intel Core i7-13620H
- 16 GB RAM
- Windows

## ✅ Current Progress

- [x] Set up the local Python development environment
- [x] Run Llama 3.2 3B through Ollama
- [x] Generate a storyboard from a natural-language idea
- [x] Configure PyTorch for NVIDIA GPU inference
- [x] Set up WanGP and Wan2.1 Text-to-Video 1.3B
- [x] Successfully generate a video locally
- [ ] Connect the storyboard generator to the video-generation interface
- [ ] Automate multi-shot generation
- [ ] Assemble clips automatically with FFmpeg
- [ ] Build a unified interface for the complete workflow
- [ ] Explore local narration and sound generation

## 🎯 Project Goals

- Keep inference local wherever practical, avoiding per-generation API charges.
- Automate the transition from an idea to a sequence of video shots.
- Explore AI orchestration and video generation on consumer hardware.
- Build a reproducible workflow with minimal manual intervention.

## ⚠️ Current Limitations

This is a work in progress. The language-model planning and video-generation components have been tested, but the complete automated pipeline is not yet integrated. Generation speed and output quality depend on the hardware, model configuration, and input prompts.

## 📌 Roadmap

The next milestone is to connect the local language model to the video generator so the system can create multiple shots automatically, then combine them into a finished video.

## 📄 License

Licensing for the application code and the underlying models may differ. Check the applicable licenses before redistributing code, model weights, or generated assets.
