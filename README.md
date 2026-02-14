Intelligent Monitoring Ground Station (GCS)

A production-grade AI-powered Ground Station web application for intelligent monitoring and inspection of agricultural fields and powerline infrastructure using computer vision.

This system allows users to upload inspection footage (video or images) and automatically generates structured insights including object detection, segmentation overlays, anomaly detection, and actionable summary reports.

Overview

This project rebuilds and modernizes my final-year UAV intelligent monitoring system into a scalable, web-based architecture. Instead of running directly onboard a drone, the intelligence is deployed as a backend ML inference engine integrated into a Ground Station-style web application.

The platform simulates real inspection workflows by processing uploaded footage and returning:

Annotated inspection video

Frame-level detection logs

Weed coverage analysis (farmland)

Component detection & defect flagging (powerlines)

JSON + PDF summary reports

Confidence scores and event timelines

Core Capabilities
🌾 Agriculture Monitoring

Weed vs crop segmentation

Weed coverage percentage calculation

Hotspot detection

Visual overlays for precision farming insights

⚡ Powerline Inspection

Detection of poles, insulators, joints, and conductors

Vegetation encroachment detection

Visible defect identification

Anomaly detection for rare/unseen faults

📊 Ground Station Interface

Video upload & job queue system

Real-time processing status

Annotated playback

Timeline-based event viewer

Exportable inspection reports

Architecture
Backend

Django + Django REST Framework

Celery + Redis for async video processing

PyTorch-based ML inference

YOLO / Segmentation / Anomaly detection pipelines

Modular ML registry & pipeline abstraction

PostgreSQL (metadata & inspection logs)

Frontend

React (Vite)

Ground-station style UI

Upload dashboard

Job monitoring & results visualization

Machine Learning Stack

PyTorch

Ultralytics YOLO (object detection)

DeepLab / Mask2Former (segmentation)

Anomaly detection pipeline (PatchCore-style)

ONNX export ready for acceleration

Modular pipeline architecture for easy model swapping

Design Philosophy

This project is built as:

Modular

Production-oriented

Extensible to UAV edge deployment

Suitable for research, portfolio demonstration, or commercialization

It demonstrates full-stack AI system engineering — from ML model design to scalable web integration.

Future Extensions

Real-time drone feed integration

Edge deployment (Jetson / Coral)

Geospatial mapping with PostGIS

Temporal change detection

Multi-drone swarm coordination

Security & critical infrastructure monitoring