#!/bin/bash

set -e  # Stop on error

# Remove broken iovisor repo if present
sudo rm -f /etc/apt/sources.list.d/iovisor.list
sudo apt update

# Install required packages
sudo apt install -y \
  bison build-essential cmake flex git libedit-dev \
  libllvm14 llvm-14-dev libclang-14-dev clang-14 \
  libelf-dev zlib1g-dev libfl-dev python3-setuptools \
  liblzma-dev libzstd-dev libboost-dev python3-pip \
  linux-headers-$(uname -r)

# Clone BCC repo (skip if exists)
if [ ! -d bcc ]; then
  git clone https://github.com/iovisor/bcc.git
fi
cd bcc

# Create build directory and build
mkdir -p build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
         -DPYTHON_CMD=python3 \
         -DENABLE_LLVM_NATIVECODEGEN=OFF

make -j$(nproc)
sudo make install

# Activate virtual environment (adjust path if different)
source /workspaces/ebpf-sandbox/venv/bin/activate

# Upgrade pip/setuptools/wheel inside venv
pip install --upgrade pip setuptools wheel

# Install Python bindings from generated build folder
cd src/python/bcc-python3
pip install .

# Return to project root
cd /workspaces/ebpf-sandbox
