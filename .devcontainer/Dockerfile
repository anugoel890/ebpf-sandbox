FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install all required BCC dependencies and Python bindings
RUN apt-get update && apt-get install -y \
    bison build-essential cmake flex git libedit-dev \
    libllvm15 llvm-15-dev libclang-15-dev clang-15 \
    libelf-dev zlib1g-dev libfl-dev python3-setuptools \
    liblzma-dev libzstd-dev libboost-dev python3-pip \
    linux-headers-$(uname -r) curl \
 && git clone https://github.com/iovisor/bcc.git /tmp/bcc \
 && cd /tmp/bcc && mkdir build && cd build \
 && cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DPYTHON_CMD=python3 -DENABLE_LLVM_NATIVECODEGEN=OFF \
 && make -j$(nproc) && make install \
 && cd ../src/python && pip install . \
 && rm -rf /tmp/bcc
