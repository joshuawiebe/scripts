#!/bin/bash

echo "🚀 Starting full installation of Open Interpreter + Ollama (local mode with tinyllama)..."

# Update and install dependencies
sudo apt update && sudo apt install -y python3 python3-venv python3-pip curl

# Create hidden project directory
mkdir -p ~/.open-interpreter
cd ~/.open-interpreter

# Set up virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Open Interpreter locally
echo "⚙️ Installing Open Interpreter with local support..."
pip install --upgrade pip
pip install "open-interpreter[local]"

# Install Ollama if not already installed
if ! command -v ollama &>/dev/null; then
  echo "⬇️ Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
else
  echo "✅ Ollama is already installed."
fi

# Pull tinyllama model
echo "📥 Downloading model 'tinyllama'..."
ollama pull tinyllama

# Set tinyllama as the default model
echo "tinyllama" >~/.ollama/default-model

# Add interpreter alias to .zshrc
echo "" >>~/.zshrc
echo "# Open Interpreter alias (local mode with tinyllama)" >>~/.zshrc
echo "alias interpreter='source ~/.open-interpreter/venv/bin/activate && INTERPRETER_LOCAL=1 interpreter --model tinyllama'" >>~/.zshrc

# Reload shell config
source ~/.zshrc

echo ""
echo "✅ DONE! Just type 'interpreter' in your terminal to start using it!"
