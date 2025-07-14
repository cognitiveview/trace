# 🚀 RAI Trace Metric API Helper

Easily send evaluation metrics (from **Evidently**, **DeepEval**, **Opik**, etc.) to the TRACE Metric API (`https://api.cognitiveview.com`) using a clean, reusable Python helper function.

✨ Includes type hints, docstrings, and ready‑to‑use examples.

---

## 📂 Project Structure

src/
└── rai_trace/
├── docs/ # Documentation (optional)
├── examples/ # Example scripts
│ ├── main.py
│ └── test_package.py
├── plugins/ # Optional: additional plugin modules
├── providers/ # Metric provider integrations
├── init.py
└── trace_metrics_api.py # Core API helper function
.gitignore
.python-version
pyproject.toml
README.md
LICENSE

text

---

## ✅ Features

- Unified function to post metrics from:
  - `evidently`
  - `deepeval`
  - `opik`
- User-defined metadata:
  - `application_name`
  - `version`
  - `url`
  - `use_case`
- Clean JSON payload to the TRACE Metric API
- Example scripts included

---

## ⚙️ Installation

Clone this repository and install dependencies:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt

text

Or, if using `pyproject.toml`:

pip install -e .

text

---

## 🐍 Usage

Example script:

from rai_trace.trace_metrics_api import post_metrics_to_TRACE_Metric_API

AUTH_TOKEN = "your-authorization-token"
USER_ID = "your-user-id"

metric_results = {
"accuracy": 0.92,
"f1_score": 0.88
}

response = post_metrics_to_TRACE_Metric_API(
metric_results=metric_results,
auth_token=AUTH_TOKEN,
user_id=USER_ID,
provider="evidently", # can also be 'deepeval', 'opik', etc.
application_name="chat-application",
version="1.0.0",
url="https://api.example.com/chat",
use_case="transportation"
)

print(response)

text

To see it in action, run:

python src/rai_trace/examples/main.py

text

---

## 📄 License

This project is open source under the MIT License.  
See LICENSE for details.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or pull requests to improve features or add support for more providers.