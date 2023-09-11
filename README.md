# Pysislab - CRISiSLab Seismometer Network Client

## Description

This is a client for CRISiSLab's Seismometer Network API using WebSockets and MessagePack.

## Installation

```bash
pip install pysislab
```

### Usage

To list all stations:

```bash
pysislab --list
```

To watch live data in real time for a particular seismometer:

```bash
pysislab --tail <seismometer id>
```
