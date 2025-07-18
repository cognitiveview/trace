# 🚀 RAI Trace Metric API

A lightweight Python API to post ML/AI evaluation metrics from **Evidently**, **DeepEval**, and **Opik** to the TRACE Metric API — enabling seamless tracking and reports aligned with **NIST AI RMF**, **EU AI Act**,  and other AI governance frameworks

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
---

## 🌟 Features

- **Multi-Provider Support**: Seamlessly integrate with DeepEval, Evidently, and Opik
- **Unified Metrics API**: Send evaluation metrics to TRACE Metric API with a single function
- **Provider-Specific Functions**: Individual functions for each provider with tailored configurations
- **Type Safety**: Full type hints and comprehensive documentation
- **Extensible Architecture**: Plugin-based system for easy provider integration
- **Ready-to-Use Examples**: Complete tutorials and quickstart guides
- **Financial Use Cases**: Specialized examples for finance domain applications

---

## 📂 Project Structure

```
trace/
├── src/
│   └── rai_trace/
│       ├── __init__.py                 # Main package exports
│       ├── trace_metrics_api.py        # TRACE API integration
│       ├── docs/                       # Documentation
│       │   ├── QuickStart/            # Provider quickstart guides
│       │   │   ├── DeepEval.ipynb
│       │   │   ├── Evidently.ipynb
│       │   │   └── Opik.ipynb
│       │   └── Tutorial/              # Comprehensive tutorials
│       │       └── Finance_use.ipynb  # Finance domain example
│       ├── examples/                   # Example scripts
│       │   ├── main.py                # Basic usage example
│       │   └── metrics_example.py     # Advanced metrics example
│       ├── plugins/                    # Plugin modules
│       │   └── sample.py              # Sample plugin implementation
│       ├── providers/                  # Provider integrations
│       │   ├── deepeval/
│       │   │   ├── __init__.py
│       │   │   └── deepeval.py        # DeepEval-specific functions
│       │   ├── evidently/
│       │   │   ├── __init__.py
│       │   │   └── evidently.py       # Evidently-specific functions
│       │   └── opik/
│       │       ├── __init__.py
│       │       └── opik.py            # Opik-specific functions
│       └── tests/                      # Test suite
├── pyproject.toml                      # Project configuration
├── test_package.py                     # Package validation
└── README.md                          # This file
```

---

## ⚙️ Installation

### Option 1: Clone and Install (Development)

```bash
git clone <your-repository-url>
cd trace
pip install -e .
```


## 🚀 Quick Start

### Unified API Usage

```python
from rai_trace.trace_metrics_api import post_metrics_to_TRACE_Metric_API

# Your credentials
AUTH_TOKEN = "your-subscription-key"  # Your subscription key from CognitiveView

# Metric results from your evaluation
metric_results = {
        "AnswerRelevancyMetric": 85,
        "ContextualPrecisionMetric": 92,
        "ContextualRecallMetric": 78,
        "ContextualRelevancyMetric": 88,
        "ConversationCompletenessMetric": 95,
        "ConversationRelevancyMetric": 82
    }

# Post to TRACE API
response = post_metrics_to_TRACE_Metric_API(
    metric_results=metric_results,
    auth_token=AUTH_TOKEN,
    provider="deepeval",
    application_name="my-chatbot",
    version="1.0.0",
    use_case="customer_support"
)

print(response)
```

### Provider-Specific Usage

#### DeepEval Integration

```python
from rai_trace.providers.deepeval.deepeval import post_deepeval_metrics_to_TRACE_Metric_API

AUTH_TOKEN = "your-subscription-key"  # Your subscription key from CognitiveView

metric_results = {
    "AnswerRelevancyMetric": 85,
    "ContextualPrecisionMetric": 92,
    "ContextualRecallMetric": 78,
}

response = post_deepeval_metrics_to_TRACE_Metric_API(
    metric_results=metric_results,
    auth_token=AUTH_TOKEN,
    application_name="my-chatbot",
    version="1.0.0",
    use_case="customer_support"
)
```

#### Evidently Integration

```python
from rai_trace.providers.evidently.evidently import post_evidently_metrics_to_TRACE_Metric_API

AUTH_TOKEN = "your-subscription-key"  # Your subscription key from CognitiveView

metric_results = {
    "FaithfulnessLLMEval": 0.15,
    "ContextRelevance": 0.88,
    "BLEU": 0.12
}

response = post_evidently_metrics_to_TRACE_Metric_API(
    metric_results=metric_results,
    auth_token=AUTH_TOKEN,
    application_name="fraud-detection-model",
    version="2.1.0",
    use_case="finance"
)
```

#### Opik Integration

```python
from rai_trace.providers.opik.opik import post_opik_metrics_to_TRACE_Metric_API

AUTH_TOKEN = "your-subscription-key"  # Your subscription key from CognitiveView

metric_results = {
    "Equals": 0.91,
    "Moderation": 0.87,
}

response = post_opik_metrics_to_TRACE_Metric_API(
    metric_results=metric_results,
    auth_token=AUTH_TOKEN,
    application_name="recommendation-engine",
    version="3.2.1",
    use_case="e-commerce"
)
```


## 📚 Documentation & Examples

### QuickStart Guides

- **[DeepEval Integration](src/rai_trace/docs/QuickStart/DeepEval.ipynb)**: Complete guide for DeepEval metrics
- **[Evidently Integration](src/rai_trace/docs/QuickStart/Evidently.ipynb)**: LLM evaluation with Evidently
- **[Opik Integration](src/rai_trace/docs/QuickStart/Opik.ipynb)**: Getting started with Opik

### Tutorials

- **[Finance Use Case](src/rai_trace/docs/Tutorial/Finance_use.ipynb)**: Comprehensive financial domain example with RAG systems

### Example Scripts

Run the included examples:

```bash
# Basic usage example
python src/rai_trace/examples/main.py

# Advanced metrics example
python src/rai_trace/examples/metrics_example.py
```

---

## 🔧 API Reference

### Unified API Functions

#### `post_metrics_to_TRACE_Metric_API()`

Posts evaluation metrics to the TRACE Metric API with flexible provider support.

**Parameters:**
- `metric_results` (Dict[str, Any]): Dictionary of computed metric scores
- `auth_token` (str): Subscription key for the API (from CognitiveView)
- `provider` (str): Metric provider ('deepeval', 'evidently', 'opik')
- `application_name` (str): Name of your application
- `version` (str): Application version
- `use_case` (str): Use case description

**Returns:**
- `Optional[Dict[str, Any]]`: API response or None if error

### Provider-Specific Functions

#### `post_deepeval_metrics_to_TRACE_Metric_API()`

Posts DeepEval-specific metrics with user-defined application metadata.

**Parameters:**
- `metric_results` (Dict[str, Any]): Dictionary of computed metric scores
- `auth_token` (str): Subscription key for the API (from CognitiveView)
- `application_name` (str): Name of the application posting metrics
- `version` (str): Version of the application
- `use_case` (str): Use case or domain (e.g., "transportation", "finance", "healthcare")

**Returns:**
- `Optional[Dict[str, Any]]`: Response JSON from the API, or None if error

#### `post_evidently_metrics_to_TRACE_Metric_API()`

Posts Evidently-specific metrics with user-defined application metadata.

**Parameters:**
- `metric_results` (Dict[str, Any]): Dictionary of computed metric scores
- `auth_token` (str): Subscription key for the API (from CognitiveView)
- `application_name` (str): Name of the application posting metrics
- `version` (str): Version of the application
- `use_case` (str): Use case or domain (e.g., "transportation", "finance", "healthcare")

**Returns:**
- `Optional[Dict[str, Any]]`: Response JSON from the API, or None if error

#### `post_opik_metrics_to_TRACE_Metric_API()`

Posts Opik-specific metrics with user-defined application metadata.

**Parameters:**
- `metric_results` (Dict[str, Any]): Dictionary of computed metric scores
- `auth_token` (str): Subscription key for the API (from CognitiveView)
- `application_name` (str): Name of the application posting metrics
- `version` (str): Version of the application
- `use_case` (str): Use case or domain (e.g., "transportation", "finance", "healthcare")

**Returns:**
- `Optional[Dict[str, Any]]`: Response JSON from the API, or None if error

## 🔐 Authentication

To get your TRACE API credentials:

1. **Sign in** to [CognitiveView](https://app.cognitiveview.com)
2. **Navigate** to System Settings
3. **Generate** your subscription key
4. **Copy** your subscription key

### API Endpoint Configuration

| Item         | Value                                                      |
|--------------|-----------------------------------------------------------|
| **Base URL** | `https://api.cognitiveview.com`                            |
| **API Path** | `/metrics`                                          |
| **Full URL** | `https://api.cognitiveview.com/metrics`             |
| **Authentication** | `Ocp-Apim-Subscription-Key` header                 |

**Note**: Authentication is handled through the `Ocp-Apim-Subscription-Key` header with your subscription key.

---

## 🎯 Supported Providers

| Provider | Status | Features | Module |
|----------|--------|----------|---------|
| **DeepEval** | ✅ | Answer relevancy, Hallucination, Bias, Faithfulness | [`providers.deepeval`](src/rai_trace/providers/deepeval/deepeval.py) |
| **Evidently** | ✅ | LLM evaluations, Data drift, Model monitoring | [`providers.evidently`](src/rai_trace/providers/evidently/evidently.py) |
| **Opik** | ✅ | Experiment tracking, Model comparison | [`providers.opik`](src/rai_trace/providers/opik/opik.py) |



#### DeepEval Metrics
- **Answer Relevancy**: Measures how relevant the answer is to the question
- **Faithfulness**: Evaluates if the answer is grounded in the given context
- **Hallucination**: Detects factual inconsistencies in responses
- **Bias**: Identifies potential biases in model outputs

#### Evidently Metrics
- **Data Drift**: Monitors changes in input data distribution
- **Model Quality**: Tracks model performance over time
- **Prediction Drift**: Detects shifts in model predictions

#### Opik Metrics
- **Experiment Tracking**: Compare different model versions
- **Performance Monitoring**: Track model metrics across experiments
- **Model Comparison**: Side-by-side evaluation of models

---

### Development Setup

```bash
git clone <your-fork>
cd trace
pip install -e .
pip install pytest black flake8  # Development dependencies
```

### Code Standards

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Include docstrings for public APIs
- Write tests for new features

---



## 🏆 Acknowledgments

- [DeepEval](https://www.deepeval.com/) for comprehensive LLM evaluation metrics
- [Evidently](https://www.evidentlyai.com/) for ML monitoring capabilities
- [Opik](https://www.comet.com/site/products/opik/) for experiment tracking
- [CognitiveView](https://cognitiveview.com/) for the TRACE Metric API

---

