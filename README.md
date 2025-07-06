#  AI Threat Detection 

This project shows you how to build a simple, practical threat detection system using machine learning. It’s designed to catch malicious network traffic in real time kind of like a personal security guard for your network using Python and free tools.

It works in two steps:

Train a model to recognize attacks

Use that model to scan live network traffic for suspicious packets

Think of it as a tiny but mighty intrusion detection system you can fully understand, modify, and run on your own machine.

## What’s Inside?
A trained Random Forest model (no fancy cloud fees)
A packet sniffer using Scapy (to watch your network live)
A detection script that raises alerts when it spots suspicious activity
Simple, readable code and notes to help you learn as you go

## How It Works
### Train the model (Phase 1):

Load the dataset (UNSW-NB15)

Train a Random Forest to tell normal vs. malicious packets

Save the model for later

### Detect in real time (Phase 2):
Use Scapy to sniff packets on your machine

Extract simple features (packet size, protocol, etc.)

Ask the trained model: “Is this normal?”

Print an alert if something looks fishy

### Why You Might Like It
100% free, no paid servers.
Runs on your own laptop.
Based on popular open-source libraries.
Easy to understand and extend.


