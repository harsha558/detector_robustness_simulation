# Robustness of Text Detectors Against Rephrasing (Simulation)
mirroring the idea of robustness testing without complexity.

## Overview

This project simulates how a basic text detection system may respond to
rephrased inputs.

Instead of using a trained AI model, a simple rule-based detector is
implemented to illustrate the concept of robustness testing.

## Concept

Detection systems often rely on patterns or features within text.
Rephrasing can change surface structure while preserving meaning,
which may influence detector behaviour.

## Experiment

The program:

- Defines an original sentence
- Generates rephrased variations
- Applies a simple detector function
- Observes differences in outputs

## Purpose

To demonstrate the idea of robustness evaluation in a controlled,
simplified environment.

## Important Note

This is a conceptual simulation designed for educational purposes.
It does not represent a real AI detection model.

## How to Run

python detector_text.py
